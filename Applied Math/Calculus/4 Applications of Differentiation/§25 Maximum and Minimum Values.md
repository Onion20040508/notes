---
type: section
subject: "[[Calculus]]"
chapter: 4
section: 25
stewart: "4.1"
aliases: ["Stewart 4.1"]
tags: [calculus]
---
← [[§24 Hyperbolic Functions]] · ↑ [[· 4 Applications of Differentiation]] · [[§26 The Mean Value Theorem]] →

*Stewart, Section 4.1.*

Many applications of calculus are optimization problems: find the largest or smallest value of a function. This section separates the largest value overall (absolute extrema) from the largest value nearby (local extrema). The Extreme Value Theorem guarantees that a continuous function on a closed interval has both an absolute maximum and an absolute minimum. Fermat's Theorem says where a local extremum can be: only at a critical number, where $f'$ is $0$ or does not exist. Together they give the Closed Interval Method, which finds the extreme values by comparing finitely many function values.

## Absolute and Local Extreme Values

> [!definition] Definition §25.1: Absolute Maximum and Minimum
> Let $c$ be a number in the domain $D$ of a function $f$. Then $f(c)$ is the
> - **absolute maximum** value of $f$ on $D$ if $f(c) \ge f(x)$ for all $x$ in $D$;
> - **absolute minimum** value of $f$ on $D$ if $f(c) \le f(x)$ for all $x$ in $D$.
>
> An absolute maximum or minimum is also called a **global** maximum or minimum. The maximum and minimum values of $f$ are called the **extreme values** of $f$.
>
> *Stewart: 4.1, Definition 1*

^def-25-1

> [!definition] Definition §25.2: Local Maximum and Minimum
> The number $f(c)$ is a
> - **local maximum** value of $f$ if $f(c) \ge f(x)$ when $x$ is near $c$;
> - **local minimum** value of $f$ if $f(c) \le f(x)$ when $x$ is near $c$.
>
> Here "near $c$" means: for all $x$ in some open interval containing $c$. In particular, a local maximum or minimum cannot occur at an endpoint of the domain.
>
> *Stewart: 4.1, Definition 2*

^def-25-2

A function may have many extreme values or none. $\cos x$ takes its (local and absolute) maximum value $1$ infinitely often, at $x = 2n\pi$, and its minimum value $-1$ at $x = (2n + 1)\pi$, $n \in \mathbb{Z}$. $f(x) = x^2$ has the absolute minimum value $f(0) = 0$, since $x^2 \ge 0$, but no maximum. $f(x) = x^3$ has no extreme values at all, local or absolute.

> [!example] Example §25.1: Local Versus Absolute Extrema
> Find the local and absolute extreme values of $f(x) = 3x^4 - 16x^3 + 18x^2$, $-1 \le x \le 4$.
>
> The derivative is $f'(x) = 12x^3 - 48x^2 + 36x = 12x(x - 1)(x - 3)$. Its sign shows where $f$ falls and rises (the Increasing/Decreasing Test, [[§27 What Derivatives Tell Us About the Shape of a Graph#^thm-27-1|Theorem §27.1]]):
>
> | interval | $(-1, 0)$ | $(0, 1)$ | $(1, 3)$ | $(3, 4)$ |
> |---|---|---|---|---|
> | sign of $f'$ | $-$ | $+$ | $-$ | $+$ |
> | $f$ | decreasing | increasing | decreasing | increasing |
>
> The relevant values are
>
> $$
> f(-1) = 3 + 16 + 18 = 37, \quad f(0) = 0, \quad f(1) = 3 - 16 + 18 = 5, \quad f(3) = 243 - 432 + 162 = -27, \quad f(4) = 768 - 1024 + 288 = 32 .
> $$
>
> - $f(0) = 0$ is a local minimum and $f(1) = 5$ is a local maximum.
> - $f(3) = -27$ is both a local and the absolute minimum.
> - $f(-1) = 37$ is the absolute maximum. It is *not* a local maximum, because it occurs at an endpoint (Definition §25.2).
> - At $x = 4$, $f$ has neither a local nor an absolute maximum: $4$ is an endpoint, and $f(4) = 32 < 37$.
>
> *Stewart: Example 4.1.1*

^ex-25-1

## The Extreme Value Theorem

> [!theorem] Theorem §25.1: The Extreme Value Theorem
> If $f$ is continuous on a closed interval $[a, b]$, then $f$ attains an absolute maximum value $f(c)$ and an absolute minimum value $f(d)$ at some numbers $c$ and $d$ in $[a, b]$.
>
> *Stewart: 4.1, Theorem 3*

^thm-25-1

*Stewart omits the proof ("it is difficult to prove"). It rests on the completeness of the real numbers and is proved in [[§18 Properties of Continuous Functions#^thm-18-1|451 Thm. §18.1]].*

> [!remark]- Connections
> - Rigorous treatment: [[§18 Properties of Continuous Functions#^thm-18-1|451 Thm. §18.1]], via Bolzano–Weierstrass. Hub: [[Extreme Value Theorem]].
> - Topological form: a continuous image of a compact space is compact, [[§15 Compact Spaces#^thm-15-3|590 Thm. §15.3]], and a compact subset of $\mathbb{R}$ is closed and bounded, so it contains its supremum and infimum.

> [!remark] Remark: Both Hypotheses Are Needed
> An extreme value can be attained more than once (as for $\cos x$ on $[0, 4\pi]$). If either hypothesis is dropped, the extreme values may fail to exist (Stewart's Figures 9 and 10 show the two cases).
> - *Not continuous.* On $[0, 2]$ let $f(x) = x$ for $0 \le x < 1$ and $f(x) = 0$ for $1 \le x \le 2$. The values come arbitrarily close to $1$ but never reach it, so $f$ has no maximum value. (It has the minimum value $0$: a discontinuous function *may* have extreme values, it is just not guaranteed.)
> - *Interval not closed.* $g(x) = x$ is continuous on $(0, 2)$, with range $(0, 2)$, and has neither a maximum nor a minimum value.

^rem-25-1

## Critical Numbers and the Closed Interval Method

At a local maximum or minimum of a smooth graph the tangent line looks horizontal. Fermat's Theorem says that this is always so where the derivative exists.

> [!theorem] Theorem §25.2: Fermat's Theorem
> If $f$ has a local maximum or minimum at $c$, and if $f'(c)$ exists, then $f'(c) = 0$.
>
> *Stewart: 4.1, Theorem 4*

^thm-25-2

> [!proof]+ Proof
> **Local maximum.** By Definition §25.2, $f(c) \ge f(x)$ for all $x$ sufficiently close to $c$. So if $h$ is sufficiently close to $0$, positive or negative,
>
> $$
> f(c + h) - f(c) \le 0 . \qquad (5)
> $$
>
> *$h > 0$.* Dividing (5) by $h > 0$ preserves the inequality:
>
> $$
> \frac{f(c + h) - f(c)}{h} \le 0 .
> $$
>
> Limits preserve $\le$ ([[§8 Calculating Limits Using the Limit Laws#^thm-8-6|Theorem §8.6]], Stewart's Theorem 2.3.2), so taking the right-hand limit gives $\displaystyle\lim_{h \to 0^+} \frac{f(c + h) - f(c)}{h} \le 0$. Since $f'(c)$ exists, the two-sided limit defining it equals this right-hand limit ([[§8 Calculating Limits Using the Limit Laws#^thm-8-5|Theorem §8.5]]):
>
> $$
> f'(c) = \lim_{h \to 0} \frac{f(c + h) - f(c)}{h} = \lim_{h \to 0^+} \frac{f(c + h) - f(c)}{h} \le 0 .
> $$
>
> *$h < 0$.* Dividing (5) by $h < 0$ reverses the inequality, so the quotient is $\ge 0$, and taking the left-hand limit,
>
> $$
> f'(c) = \lim_{h \to 0^-} \frac{f(c + h) - f(c)}{h} \ge 0 .
> $$
>
> So $f'(c) \le 0$ and $f'(c) \ge 0$, hence $f'(c) = 0$.
>
> **Local minimum.** (Stewart says "similar"; here is the short route of his Exercise 81.) If $f$ has a local minimum at $c$, then $-f$ has a local maximum at $c$, and $(-f)'(c) = -f'(c)$ exists. By the first case, $-f'(c) = 0$.

^pf-25-2

*Uses:* [[§25 Maximum and Minimum Values#^def-25-2|Def. §25.2]], [[§8 Calculating Limits Using the Limit Laws#^thm-8-6|§8.6]], [[§8 Calculating Limits Using the Limit Laws#^thm-8-5|§8.5]], [[§12 Derivatives and Rates of Change#^def-12-3|Def. §12.3]]

> [!remark]- Connections
> - Rigorous treatment: [[§29 The Mean Value Theorem#^thm-29-1|451 Thm. §29.1]] (Interior Extremum Theorem), with the same sign argument.
> - Several variables (all partial derivatives vanish at an interior extremum): [[§14 Optimization and Lagrange Multipliers#^thm-14-1|452 Thm. §14.1]]; in this subject, [[§96 Maximum and Minimum Values#^thm-96-1|Theorem §96.1]].

The converse of Fermat's Theorem is false, and an extreme value can occur where $f'$ does not exist:

> [!example] Example §25.2: What Fermat's Theorem Does Not Say
> **(a)** $f(x) = x^3$ has $f'(x) = 3x^2$, so $f'(0) = 0$. But $f$ has no maximum or minimum at $0$: $x^3 > 0$ for $x > 0$ and $x^3 < 0$ for $x < 0$. The curve $y = x^3$ has a horizontal tangent at $(0, 0)$ and crosses it there. So $f'(c) = 0$ does not imply an extremum at $c$.
>
> **(b)** $f(x) = |x|$ has its (local and absolute) minimum value $f(0) = 0$ at $0$, since $|x| \ge 0$. But $f'(0)$ does not exist: the difference quotient $\frac{|h| - 0}{h}$ is $1$ for $h > 0$ and $-1$ for $h < 0$ ([[§13 The Derivative as a Function#^ex-13-4|Ex. §13.4]]). So this minimum cannot be found by solving $f'(x) = 0$.
>
> *Stewart: Examples 4.1.5 and 4.1.6*

^ex-25-2

So we should look for extreme values where $f'(c) = 0$ *or* where $f'(c)$ does not exist.

> [!definition] Definition §25.3: Critical Number
> A **critical number** of a function $f$ is a number $c$ in the domain of $f$ such that either $f'(c) = 0$ or $f'(c)$ does not exist.
>
> *Stewart: 4.1, Definition 6*

^def-25-3

> [!example] Example §25.3: Finding Critical Numbers
> Find the critical numbers of (a) $f(x) = x^3 - 3x^2 + 1$ and (b) $f(x) = x^{3/5}(4 - x)$.
>
> **(a)** $f'(x) = 3x^2 - 6x = 3x(x - 2)$ exists for all $x$, so the only critical numbers are the solutions of $f'(x) = 0$: $x = 0$ and $x = 2$.
>
> **(b)** The domain of $f$ is $\mathbb{R}$. By the Product Rule ([[§15 The Product and Quotient Rules#^thm-15-1|Theorem §15.1]]),
>
> $$
> f'(x) = x^{3/5}(-1) + (4 - x)\cdot\tfrac35 x^{-2/5} = -x^{3/5} + \frac{3(4 - x)}{5x^{2/5}} = \frac{-5x + 3(4 - x)}{5x^{2/5}} = \frac{12 - 8x}{5x^{2/5}} .
> $$
>
> (Alternatively, write $f(x) = 4x^{3/5} - x^{8/5}$ first.) So $f'(x) = 0$ when $12 - 8x = 0$, that is, $x = \frac32$, and $f'(x)$ does not exist when $x = 0$. Both are in the domain, so the critical numbers are $\frac32$ and $0$. The graph has a horizontal tangent at $x = \frac32$ and a vertical tangent at $x = 0$.
>
> *Stewart: Example 4.1.7*

^ex-25-3

> [!theorem] Corollary §25.3: Local Extrema Occur at Critical Numbers
> If $f$ has a local maximum or minimum at $c$, then $c$ is a critical number of $f$.
>
> *Stewart: 4.1, (7)*

^cor-25-3

> [!proof]+ Proof
> A local extremum at $c$ involves the value $f(c)$, so $c$ is in the domain of $f$. If $f'(c)$ does not exist, $c$ is a critical number by Definition §25.3. If $f'(c)$ exists, then $f'(c) = 0$ by Fermat's Theorem, and again $c$ is a critical number.

^pf-25-3

*Uses:* [[§25 Maximum and Minimum Values#^thm-25-2|§25.2]], [[§25 Maximum and Minimum Values#^def-25-3|Def. §25.3]]

> [!remark] Remark: Method — The Closed Interval Method
> To find the *absolute* maximum and minimum values of a continuous function $f$ on a closed interval $[a, b]$:
> 1. Find the values of $f$ at the critical numbers of $f$ in $(a, b)$.
> 2. Find the values of $f$ at the endpoints $a$ and $b$.
> 3. The largest of the values from Steps 1 and 2 is the absolute maximum value; the smallest is the absolute minimum value.
>
> **Why it works.** By the Extreme Value Theorem ([[§25 Maximum and Minimum Values#^thm-25-1|Theorem §25.1]]) the absolute maximum exists; say it is $f(c)$. Either $c$ is an endpoint, or $c \in (a, b)$. In the second case $(a, b)$ is an open interval containing $c$ on which $f(c) \ge f(x)$, so $f(c)$ is a local maximum and $c$ is a critical number by [[§25 Maximum and Minimum Values#^cor-25-3|Corollary §25.3]]. Either way $f(c)$ is on the list, and it is the largest value on the list because it is the largest value of $f$. The same holds for the minimum.

^rem-25-2

> [!example] Example §25.4: The Closed Interval Method
> Find the absolute maximum and minimum values of $f(x) = x^3 - 3x^2 + 1$, $-\frac12 \le x \le 4$.
>
> $f$ is a polynomial, hence continuous on $[-\frac12, 4]$ ([[§10 Continuity#^thm-10-2|Theorem §10.2]]), so the Closed Interval Method applies. By Example §25.3(a) the critical numbers are $0$ and $2$, both in $(-\frac12, 4)$.
> 1. Values at the critical numbers: $f(0) = 1$, $f(2) = 8 - 12 + 1 = -3$.
> 2. Values at the endpoints: $f(-\frac12) = -\frac18 - \frac34 + 1 = \frac18$, $f(4) = 64 - 48 + 1 = 17$.
> 3. Comparing the four numbers: the absolute maximum value is $f(4) = 17$ and the absolute minimum value is $f(2) = -3$.
>
> Here the absolute maximum occurs at an endpoint and the absolute minimum at a critical number. $f(0) = 1$ is a local maximum but not an absolute one.
>
> *Stewart: Example 4.1.8*

^ex-25-4

![[m233-25-1.svg]]
*Example §25.4: $y = x^3 - 3x^2 + 1$ on $[-\frac12, 4]$. The candidates are the critical numbers $0$ and $2$, where the tangent is horizontal (gray), and the two endpoints. The largest value $17$ is at the endpoint $4$ (red), the smallest $-3$ at the critical number $2$ (blue). The local maximum $f(0) = 1$ is beaten by the endpoint.*

> [!example] Example §25.5: Exact Extreme Values of a Trigonometric Function
> Find the exact absolute minimum and maximum values of $f(x) = x - 2\sin x$, $0 \le x \le 2\pi$.
>
> $f$ is continuous on $[0, 2\pi]$. Since $f'(x) = 1 - 2\cos x$ exists everywhere, the critical numbers are the solutions of $\cos x = \frac12$ in $(0, 2\pi)$: $x = \pi/3$ and $x = 5\pi/3$. The values there are
>
> $$
> f\Big(\frac{\pi}{3}\Big) = \frac{\pi}{3} - 2\sin\frac{\pi}{3} = \frac{\pi}{3} - \sqrt3 \approx -0.684853, \qquad
> f\Big(\frac{5\pi}{3}\Big) = \frac{5\pi}{3} - 2\sin\frac{5\pi}{3} = \frac{5\pi}{3} + \sqrt3 \approx 6.968039 ,
> $$
>
> and at the endpoints $f(0) = 0$ and $f(2\pi) = 2\pi \approx 6.28$. So the absolute minimum value is $f(\pi/3) = \pi/3 - \sqrt3$ and the absolute maximum value is $f(5\pi/3) = 5\pi/3 + \sqrt3$. A graph only estimates these (about $-0.68$ at $x \approx 1.05$ and $6.97$ at $x \approx 5.24$); calculus gives the exact values.
>
> *Stewart: Example 4.1.9*

^ex-25-5

Stewart's Example 4.1.10 applies the same method to the acceleration $a(t) = v'(t)$ of the space shuttle, a quadratic in $t$ on $0 \le t \le 126$: its maximum is at the endpoint $t = 126$ and its minimum at the critical number $t \approx 23.12$.
