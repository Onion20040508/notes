---
type: section
subject: "[[Calculus]]"
chapter: 2
section: 8
stewart: "2.3"
aliases: ["Stewart 2.3"]
tags: [calculus]
---
← [[§7 The Limit of a Function]] · ↑ [[· 2 Limits and Derivatives]] · [[§9 The Precise Definition of a Limit]] →

*Stewart, Section 2.3 · proofs from Section 2.4 and Appendix F.*

Tables and graphs can suggest a limit but cannot settle it ([[§7 The Limit of a Function#^ex-7-2|Example §7.2]]). This section replaces guessing by calculation. The Limit Laws say that limits respect sums, differences, constant multiples, products, quotients, powers and roots; together with the two basic limits $\lim_{x \to a} c = c$ and $\lim_{x \to a} x = a$ they give the limit of every polynomial and rational function by direct substitution. When substitution fails (typically with $0/0$), algebra first replaces the function by one that agrees with it near $a$. One-sided limits handle piecewise formulas, and the Squeeze Theorem handles functions trapped between two others with the same limit. The proofs use the precise definition of a limit from [[§9 The Precise Definition of a Limit#^def-9-1|Definition §9.1]] and are collected right after each result.

## Properties of Limits

> [!theorem] Theorem §8.1: The Limit Laws
> Suppose that $c$ is a constant and the limits
>
> $$
> \lim_{x \to a} f(x) = L \qquad\text{and}\qquad \lim_{x \to a} g(x) = M
> $$
>
> exist. Then
>
> | | Law | Statement |
> |---|---|---|
> | 1 | Sum Law | $\displaystyle\lim_{x \to a} [f(x) + g(x)] = L + M$ |
> | 2 | Difference Law | $\displaystyle\lim_{x \to a} [f(x) - g(x)] = L - M$ |
> | 3 | Constant Multiple Law | $\displaystyle\lim_{x \to a} [c f(x)] = c L$ |
> | 4 | Product Law | $\displaystyle\lim_{x \to a} [f(x) g(x)] = L M$ |
> | 5 | Quotient Law | $\displaystyle\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{L}{M}$ if $M \ne 0$ |
>
> In words: the limit of a sum is the sum of the limits, the limit of a difference is the difference of the limits, the limit of a constant times a function is the constant times the limit, the limit of a product is the product of the limits, and the limit of a quotient is the quotient of the limits, provided that the limit of the denominator is not $0$.
>
> *Stewart: 2.3, Limit Laws 1–5; proof of Law 1 in 2.4, of Laws 2–5 in Appendix F*

^thm-8-1

> [!remark] Remark: Why It Works
> If $f(x)$ is close to $L$ and $g(x)$ is close to $M$, then $f(x) + g(x)$ should be close to $L + M$, and similarly for the other operations. The proof makes "close" quantitative: to get $f(x) + g(x)$ within $\varepsilon$ of $L + M$, it is enough to get $f(x)$ and $g(x)$ each within $\varepsilon/2$ of their limits. Each law needs only the precise definition of a limit ([[§9 The Precise Definition of a Limit#^def-9-1|Definition §9.1]]) and the Triangle Inequality $|p + q| \le |p| + |q|$ ([[§116 Numbers, Inequalities, and Absolute Values|§116]]).

^rem-8-1

> [!proof]- Proof
> Throughout, $f$ and $g$ are defined on an open interval around $a$, except possibly at $a$, and "$\lim_{x \to a} f(x) = L$" means: for every $\varepsilon > 0$ there is $\delta > 0$ such that $0 < |x - a| < \delta$ implies $|f(x) - L| < \varepsilon$ ([[§9 The Precise Definition of a Limit#^def-9-1|Definition §9.1]]). Each law is proved by producing such a $\delta$.
>
> **Law 1 (Sum Law).** Let $\varepsilon > 0$. We must find $\delta > 0$ such that
>
> $$
> 0 < |x - a| < \delta \quad\Longrightarrow\quad |f(x) + g(x) - (L + M)| < \varepsilon .
> $$
>
> By the Triangle Inequality,
>
> $$
> |f(x) + g(x) - (L + M)| = |(f(x) - L) + (g(x) - M)| \le |f(x) - L| + |g(x) - M| . \qquad (1)
> $$
>
> So it suffices to make each of the two terms on the right less than $\varepsilon/2$. Since $\varepsilon/2 > 0$ and $\lim_{x \to a} f(x) = L$, there is $\delta_1 > 0$ such that $0 < |x - a| < \delta_1$ implies $|f(x) - L| < \varepsilon/2$. Since $\lim_{x \to a} g(x) = M$, there is $\delta_2 > 0$ such that $0 < |x - a| < \delta_2$ implies $|g(x) - M| < \varepsilon/2$. Let $\delta = \min\{\delta_1, \delta_2\}$. If $0 < |x - a| < \delta$, then $0 < |x - a| < \delta_1$ and $0 < |x - a| < \delta_2$, so both estimates hold and by (1)
>
> $$
> |f(x) + g(x) - (L + M)| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon .
> $$
>
> Hence $\lim_{x \to a} [f(x) + g(x)] = L + M$. (This is the proof Stewart gives in Section 2.4, [[§9 The Precise Definition of a Limit|§9]].)
>
> **Law 4 (Product Law).** Let $\varepsilon > 0$. To bring in $|f(x) - L|$ and $|g(x) - M|$, add and subtract $L g(x)$:
>
> $$
> \begin{aligned}
> |f(x) g(x) - LM| &= |f(x) g(x) - L g(x) + L g(x) - LM| \\
> &= |[f(x) - L]\, g(x) + L\, [g(x) - M]| \\
> &\le |f(x) - L|\, |g(x)| + |L|\, |g(x) - M| . \qquad (2)
> \end{aligned}
> $$
>
> We make each term in (2) less than $\varepsilon/2$, using three choices of $\delta$.
> - Since $g(x) \to M$, there is $\delta_1 > 0$ such that $0 < |x - a| < \delta_1$ implies $|g(x) - M| < \dfrac{\varepsilon}{2(1 + |L|)}$.
> - There is also $\delta_2 > 0$ such that $0 < |x - a| < \delta_2$ implies $|g(x) - M| < 1$, and then $|g(x)| = |g(x) - M + M| \le |g(x) - M| + |M| < 1 + |M|$. So $g$ is bounded near $a$.
> - Since $f(x) \to L$, there is $\delta_3 > 0$ such that $0 < |x - a| < \delta_3$ implies $|f(x) - L| < \dfrac{\varepsilon}{2(1 + |M|)}$.
>
> Let $\delta = \min\{\delta_1, \delta_2, \delta_3\}$. If $0 < |x - a| < \delta$, all three estimates hold, and (2) gives
>
> $$
> |f(x) g(x) - LM| < \frac{\varepsilon}{2(1 + |M|)}\,(1 + |M|) + |L|\, \frac{\varepsilon}{2(1 + |L|)} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon ,
> $$
>
> because $|L| / (1 + |L|) < 1$. Hence $\lim_{x \to a} [f(x) g(x)] = LM$. (The $1 +$ in the denominators only guards against dividing by $0$ when $L = 0$ or $M = 0$.)
>
> **Law 3 (Constant Multiple Law).** A constant function has limit equal to that constant: for $g(x) = c$ we have $|g(x) - c| = 0 < \varepsilon$ for every $x$, so any $\delta$ works. (This is Law 8 of [[§8 Calculating Limits Using the Limit Laws#^thm-8-2|Theorem §8.2]].) Law 4 with $g(x) = c$ now gives
>
> $$
> \lim_{x \to a} [c f(x)] = \lim_{x \to a} c \cdot \lim_{x \to a} f(x) = c L .
> $$
>
> **Law 2 (Difference Law).** Write $f(x) - g(x) = f(x) + (-1) g(x)$. By Law 1 and then Law 3 with $c = -1$,
>
> $$
> \lim_{x \to a} [f(x) - g(x)] = \lim_{x \to a} f(x) + \lim_{x \to a} [(-1) g(x)] = L + (-1) M = L - M .
> $$
>
> **Law 5 (Quotient Law).** Let $M \ne 0$. First we show $\lim_{x \to a} 1/g(x) = 1/M$, that is: for every $\varepsilon > 0$ there is $\delta > 0$ such that $0 < |x - a| < \delta$ implies $\big|\frac{1}{g(x)} - \frac{1}{M}\big| < \varepsilon$. We have
>
> $$
> \left| \frac{1}{g(x)} - \frac{1}{M} \right| = \frac{|M - g(x)|}{|M g(x)|} .
> $$
>
> The numerator can be made small. We also need the denominator not to be small near $a$. Since $|M|/2 > 0$, there is $\delta_1 > 0$ such that $0 < |x - a| < \delta_1$ implies $|g(x) - M| < |M|/2$, and then
>
> $$
> |M| = |M - g(x) + g(x)| \le |M - g(x)| + |g(x)| < \frac{|M|}{2} + |g(x)| , \qquad\text{so}\qquad |g(x)| > \frac{|M|}{2} .
> $$
>
> In particular $g(x) \ne 0$ there, so $1/g(x)$ and $f(x)/g(x)$ are defined near $a$, and
>
> $$
> \frac{1}{|M g(x)|} = \frac{1}{|M|\, |g(x)|} < \frac{1}{|M|} \cdot \frac{2}{|M|} = \frac{2}{M^2} .
> $$
>
> Next there is $\delta_2 > 0$ such that $0 < |x - a| < \delta_2$ implies $|g(x) - M| < \dfrac{M^2}{2}\, \varepsilon$. Let $\delta = \min\{\delta_1, \delta_2\}$. For $0 < |x - a| < \delta$,
>
> $$
> \left| \frac{1}{g(x)} - \frac{1}{M} \right| = \frac{|M - g(x)|}{|M g(x)|} < \frac{2}{M^2} \cdot \frac{M^2}{2}\, \varepsilon = \varepsilon .
> $$
>
> So $\lim_{x \to a} 1/g(x) = 1/M$. Finally, by Law 4,
>
> $$
> \lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \left( f(x) \cdot \frac{1}{g(x)} \right) = \lim_{x \to a} f(x) \cdot \lim_{x \to a} \frac{1}{g(x)} = L \cdot \frac{1}{M} = \frac{L}{M} .
> $$

^pf-8-1

*Uses:* [[§9 The Precise Definition of a Limit#^def-9-1|Def. §9.1]], [[§116 Numbers, Inequalities, and Absolute Values|§116]] (Triangle Inequality)

> [!remark]- Connections
> - Rigorous treatment: 451 obtains these laws for limits of functions ([[§20 Limits of Functions#^rem-20-2|451 Remark after Thm. §20.2]]) from the same laws for sequences, [[§9 Limit Theorems for Sequences#^thm-9-3|451 Thm. §9.3]] (sums and products, with the same add-and-subtract step as Law 4) and [[§9 Limit Theorems for Sequences#^thm-9-4|451 Thm. §9.4]] (quotients, with the same lower bound for the denominator as Law 5).

Repeated use of the Product Law, and two basic limits, give six more laws. Stewart numbers them on from 6.

> [!theorem] Theorem §8.2: Limit Laws 6–11
> Let $n$ be a positive integer, $a$ and $c$ constants, and suppose $\lim_{x \to a} f(x)$ exists.
>
> | | Law | Statement |
> |---|---|---|
> | 6 | Power Law | $\displaystyle\lim_{x \to a} [f(x)]^n = \Big[\lim_{x \to a} f(x)\Big]^n$ |
> | 7 | Root Law | $\displaystyle\lim_{x \to a} \sqrt[n]{f(x)} = \sqrt[n]{\lim_{x \to a} f(x)}$ (if $n$ is even, assume $\lim_{x \to a} f(x) > 0$) |
> | 8 | | $\displaystyle\lim_{x \to a} c = c$ |
> | 9 | | $\displaystyle\lim_{x \to a} x = a$ |
> | 10 | | $\displaystyle\lim_{x \to a} x^n = a^n$ |
> | 11 | | $\displaystyle\lim_{x \to a} \sqrt[n]{x} = \sqrt[n]{a}$ (if $n$ is even, assume $a > 0$) |
>
> **Law 7 is proved in [[§10 Continuity|§10]]**, as [[§10 Continuity#^cor-10-8|Corollary §10.8]]; the other five are proved below.
>
> *Stewart: 2.3, Limit Laws 6–11 (Law 7 proved in 2.5)*

^thm-8-2

> [!proof]+ Proof
> **Law 8.** For every $x$, $|c - c| = 0 < \varepsilon$, so any $\delta > 0$ works in [[§9 The Precise Definition of a Limit#^def-9-1|Definition §9.1]].
>
> **Law 9.** Given $\varepsilon > 0$, take $\delta = \varepsilon$: if $0 < |x - a| < \delta$, then $|x - a| < \varepsilon$.
>
> (Stewart calls Laws 8 and 9 obvious from the graphs of $y = c$ and $y = x$ and leaves the $\varepsilon$–$\delta$ proofs as Exercises 2.4.23–24; these are those proofs.)
>
> **Law 6.** By induction on $n$. For $n = 1$ there is nothing to prove. If Law 6 holds for $n$, then $[f(x)]^{n+1} = [f(x)]^n \cdot f(x)$, and the Product Law (Law 4 of [[§8 Calculating Limits Using the Limit Laws#^thm-8-1|Theorem §8.1]]) gives
>
> $$
> \lim_{x \to a} [f(x)]^{n+1} = \lim_{x \to a} [f(x)]^n \cdot \lim_{x \to a} f(x) = \Big[\lim_{x \to a} f(x)\Big]^n \cdot \lim_{x \to a} f(x) = \Big[\lim_{x \to a} f(x)\Big]^{n+1} .
> $$
>
> **Law 10.** Put $f(x) = x$ in Law 6 and use Law 9: $\lim_{x \to a} x^n = \big[\lim_{x \to a} x\big]^n = a^n$.
>
> **Law 7** is [[§10 Continuity#^cor-10-8|Corollary §10.8]] (Stewart leaves it as Exercise 2.5.69).
>
> **Law 11.** Stewart puts $f(x) = x$ in Law 7 and uses Law 9: $\lim_{x \to a} \sqrt[n]{x} = \sqrt[n]{\lim_{x \to a} x} = \sqrt[n]{a}$ (for even $n$ the hypothesis of Law 7 is $a > 0$). This rests on Law 7 and hence on [[§10 Continuity|§10]]. There is no circle: Law 11 says that the root functions are continuous, and [[§10 Continuity#^thm-10-6|Theorem §10.6]] proves that directly (roots are inverses of powers), without Law 7 or Law 11. Corollary §10.8 then derives Law 7 from it. (For square roots Stewart also outlines an $\varepsilon$–$\delta$ proof in Exercise 2.4.37.)

^pf-8-2

*Uses:* [[§8 Calculating Limits Using the Limit Laws#^thm-8-1|§8.1]], [[§9 The Precise Definition of a Limit#^def-9-1|Def. §9.1]], [[§10 Continuity#^cor-10-8|§10.8]], [[§10 Continuity#^thm-10-6|§10.6]]

> [!example] Example §8.1: Justifying Each Step
> Evaluate the following limits and justify each step.
>
> **(a)** $\displaystyle\lim_{x \to 5} (2x^2 - 3x + 4)$.
>
> $$
> \begin{aligned}
> \lim_{x \to 5} (2x^2 - 3x + 4) &= \lim_{x \to 5} (2x^2) - \lim_{x \to 5} (3x) + \lim_{x \to 5} 4 && \text{(Laws 2 and 1)} \\
> &= 2 \lim_{x \to 5} x^2 - 3 \lim_{x \to 5} x + \lim_{x \to 5} 4 && \text{(Law 3)} \\
> &= 2(5^2) - 3(5) + 4 && \text{(Laws 10, 9 and 8)} \\
> &= 50 - 15 + 4 = 39 .
> \end{aligned}
> $$
>
> **(b)** $\displaystyle\lim_{x \to -2} \frac{x^3 + 2x^2 - 1}{5 - 3x}$.
>
> $$
> \begin{aligned}
> \lim_{x \to -2} \frac{x^3 + 2x^2 - 1}{5 - 3x}
> &= \frac{\lim_{x \to -2} (x^3 + 2x^2 - 1)}{\lim_{x \to -2} (5 - 3x)} && \text{(Law 5)} \\
> &= \frac{\lim_{x \to -2} x^3 + 2 \lim_{x \to -2} x^2 - \lim_{x \to -2} 1}{\lim_{x \to -2} 5 - 3 \lim_{x \to -2} x} && \text{(Laws 1, 2 and 3)} \\
> &= \frac{(-2)^3 + 2(-2)^2 - 1}{5 - 3(-2)} && \text{(Laws 10, 9 and 8)} \\
> &= \frac{-8 + 8 - 1}{11} = -\frac{1}{11} .
> \end{aligned}
> $$
>
> The first step of (b) is justified only by the last ones: Law 5 needs the limits of numerator and denominator to exist and the limit of the denominator to be non-zero, and that is what the computation shows ($-1$ and $11 \ne 0$). In both parts the answer is the value of the function at the point: $2(5^2) - 3(5) + 4 = 39$, and the rational function at $x = -2$ equals $-\frac{1}{11}$.
>
> *Stewart: Example 2.3.2*

^ex-8-1

## Evaluating Limits by Direct Substitution

> [!theorem] Theorem §8.3: Direct Substitution Property
> If $f$ is a polynomial or a rational function and $a$ is in the domain of $f$, then
>
> $$
> \lim_{x \to a} f(x) = f(a) .
> $$
>
> *Stewart: 2.3, Direct Substitution Property*

^thm-8-3

> [!proof]+ Proof
> Stewart: "similar use of the Limit Laws" as in Example §8.1 proves this (his Exercises 59 and 60). Here is that argument.
>
> **Polynomials.** Let $P(x) = c_n x^n + c_{n-1} x^{n-1} + \cdots + c_1 x + c_0$. By Law 3 and Law 10, $\lim_{x \to a} c_k x^k = c_k a^k$ for $k = 1, \ldots, n$, and by Law 8, $\lim_{x \to a} c_0 = c_0$. Applying Law 1 to these $n + 1$ terms ($n$ times, one term at a time),
>
> $$
> \lim_{x \to a} P(x) = c_n a^n + \cdots + c_1 a + c_0 = P(a) .
> $$
>
> **Rational functions.** Let $f = P/Q$ with polynomials $P$, $Q$, and let $a$ be in the domain of $f$, that is, $Q(a) \ne 0$. By the polynomial case, $\lim_{x \to a} P(x) = P(a)$ and $\lim_{x \to a} Q(x) = Q(a) \ne 0$, so Law 5 gives $\lim_{x \to a} f(x) = P(a)/Q(a) = f(a)$.

^pf-8-3

*Uses:* [[§8 Calculating Limits Using the Limit Laws#^thm-8-1|§8.1]] (Laws 1, 3, 5), [[§8 Calculating Limits Using the Limit Laws#^thm-8-2|§8.2]] (Laws 8, 10)

Functions with the Direct Substitution Property at $a$ are called **continuous at $a$** ([[§10 Continuity#^def-10-1|Definition §10.1]]); in that language this theorem is [[§10 Continuity#^thm-10-2|Theorem §10.2]]. Not every limit can be found by substitution: the interesting ones in calculus are of the form $0/0$ at $a$. The next fact lets us change the function at $a$ itself without changing the limit.

> [!theorem] Theorem §8.4: Functions That Agree Except at a
> If $f(x) = g(x)$ when $x \ne a$, then $\lim_{x \to a} f(x) = \lim_{x \to a} g(x)$, provided the limits exist.
>
> *Stewart: 2.3 (boxed statement after Example 3)*

^thm-8-4

> [!proof]+ Proof
> Stewart's reason: in computing a limit as $x \to a$ we never consider $x = a$. Precisely: suppose $\lim_{x \to a} g(x) = L$ and let $\varepsilon > 0$. Take $\delta > 0$ such that $0 < |x - a| < \delta$ implies $|g(x) - L| < \varepsilon$. For such $x$ we have $x \ne a$, so $f(x) = g(x)$ and $|f(x) - L| = |g(x) - L| < \varepsilon$. So $\lim_{x \to a} f(x) = L$ as well.
>
> The argument shows a little more than the statement: if one of the two limits exists, so does the other, and they are equal.

^pf-8-4

*Uses:* [[§9 The Precise Definition of a Limit#^def-9-1|Def. §9.1]]

> [!example] Example §8.2: Cancelling a Common Factor
> **(a)** Find $\displaystyle\lim_{x \to 1} \frac{x^2 - 1}{x - 1}$.
>
> Substituting $x = 1$ is impossible ($f(1)$ is $0/0$, undefined), and the Quotient Law does not apply because the limit of the denominator is $0$. Factor the numerator as a difference of squares:
>
> $$
> \frac{x^2 - 1}{x - 1} = \frac{(x - 1)(x + 1)}{x - 1} = x + 1 \qquad (x \ne 1) .
> $$
>
> Cancelling is legitimate because $x \ne 1$, so $x - 1 \ne 0$. The two functions agree except at $1$, so by Theorem §8.4 and direct substitution (Theorem §8.3),
>
> $$
> \lim_{x \to 1} \frac{x^2 - 1}{x - 1} = \lim_{x \to 1} (x + 1) = 1 + 1 = 2 .
> $$
>
> This is the slope of the tangent to $y = x^2$ at $(1, 1)$ from [[§6 The Tangent and Velocity Problems|§6]] (Example 2.1.1).
>
> **(b)** Find $\lim_{x \to 1} g(x)$ for $g(x) = x + 1$ if $x \ne 1$ and $g(1) = \pi$.
>
> The value $g(1) = \pi$ is irrelevant. Since $g(x) = x + 1$ for $x \ne 1$, Theorem §8.4 gives $\lim_{x \to 1} g(x) = \lim_{x \to 1} (x + 1) = 2$. The functions of (a) and (b) differ only at $x = 1$ (one is undefined there, the other equals $\pi$), so they have the same limit.
>
> **(c)** Evaluate $\displaystyle\lim_{h \to 0} \frac{(3 + h)^2 - 9}{h}$.
>
> Again $h = 0$ gives $0/0$. Expand and cancel, remembering that $h \ne 0$:
>
> $$
> \frac{(3 + h)^2 - 9}{h} = \frac{9 + 6h + h^2 - 9}{h} = \frac{h(6 + h)}{h} = 6 + h ,
> $$
>
> so the limit is $\lim_{h \to 0} (6 + h) = 6$. (This is the slope of the tangent to $y = x^2$ at $(3, 9)$; limits of this shape are derivatives, [[§12 Derivatives and Rates of Change|§12]].)
>
> *Stewart: Examples 2.3.3, 2.3.4 and 2.3.5*

^ex-8-2

> [!example] Example §8.3: Rationalizing the Numerator
> Find $\displaystyle\lim_{t \to 0} \frac{\sqrt{t^2 + 9} - 3}{t^2}$.
>
> The denominator tends to $0$, so the Quotient Law cannot be applied directly. Multiply numerator and denominator by the conjugate $\sqrt{t^2 + 9} + 3$:
>
> $$
> \begin{aligned}
> \lim_{t \to 0} \frac{\sqrt{t^2 + 9} - 3}{t^2}
> &= \lim_{t \to 0} \frac{\sqrt{t^2 + 9} - 3}{t^2} \cdot \frac{\sqrt{t^2 + 9} + 3}{\sqrt{t^2 + 9} + 3}
> = \lim_{t \to 0} \frac{(t^2 + 9) - 9}{t^2 \big(\sqrt{t^2 + 9} + 3\big)} \\
> &= \lim_{t \to 0} \frac{t^2}{t^2 \big(\sqrt{t^2 + 9} + 3\big)}
> = \lim_{t \to 0} \frac{1}{\sqrt{t^2 + 9} + 3} \\
> &= \frac{1}{\sqrt{\lim_{t \to 0} (t^2 + 9)} + 3} = \frac{1}{3 + 3} = \frac{1}{6} .
> \end{aligned}
> $$
>
> The last line uses Laws 5, 1, 7, 8 and 10. Law 7 applies because $\lim_{t \to 0} (t^2 + 9) = 9 > 0$. This confirms the value guessed from a table in [[§7 The Limit of a Function#^ex-7-1|Example §7.1]], where the calculator went wrong for very small $t$. The algebra removed the subtraction of nearly equal numbers $\sqrt{t^2 + 9} - 3$ that caused the trouble.
>
> *Stewart: Example 2.3.6*

^ex-8-3

## Using One-Sided Limits

> [!theorem] Theorem §8.5: Two-Sided and One-Sided Limits
> $$
> \lim_{x \to a} f(x) = L \qquad\text{if and only if}\qquad \lim_{x \to a^-} f(x) = L = \lim_{x \to a^+} f(x) .
> $$
>
> So the two-sided limit exists exactly when both one-sided limits exist and are equal.
>
> *Stewart: 2.3, Theorem 1 (stated first as 2.2, box 3)*

^thm-8-5

> [!proof]+ Proof
> Stewart observes this in Section 2.2 by comparing the intuitive definitions, and asks for a proof from the precise ones in Exercise 2.4.40. Here it is, with [[§9 The Precise Definition of a Limit#^def-9-1|Definition §9.1]] (two-sided) and [[§9 The Precise Definition of a Limit#^def-9-2|Definition §9.2]] (one-sided).
>
> ($\Rightarrow$) Let $\varepsilon > 0$ and take $\delta > 0$ with $|f(x) - L| < \varepsilon$ whenever $0 < |x - a| < \delta$. If $a - \delta < x < a$, then $0 < |x - a| < \delta$, so $|f(x) - L| < \varepsilon$: this $\delta$ works for the left-hand limit. In the same way it works for $a < x < a + \delta$, the right-hand limit.
>
> ($\Leftarrow$) Let $\varepsilon > 0$. The left-hand limit gives $\delta_1 > 0$ with $|f(x) - L| < \varepsilon$ for $a - \delta_1 < x < a$, and the right-hand limit gives $\delta_2 > 0$ with $|f(x) - L| < \varepsilon$ for $a < x < a + \delta_2$. Let $\delta = \min\{\delta_1, \delta_2\}$. If $0 < |x - a| < \delta$, then either $a - \delta_1 \le a - \delta < x < a$ or $a < x < a + \delta \le a + \delta_2$, and in both cases $|f(x) - L| < \varepsilon$. So $\lim_{x \to a} f(x) = L$.

^pf-8-5

*Uses:* [[§9 The Precise Definition of a Limit#^def-9-1|Def. §9.1]], [[§9 The Precise Definition of a Limit#^def-9-2|Def. §9.2]]

> [!remark]- Connections
> - Rigorous treatment: [[§20 Limits of Functions#^thm-20-2|451 Thm. §20.2]], with the same choice $\delta = \min\{\delta_1, \delta_2\}$.

> [!remark] Remark: The Limit Laws for One-Sided Limits
> Stewart uses the fact that the Limit Laws ([[§8 Calculating Limits Using the Limit Laws#^thm-8-1|Theorems §8.1]] and [[§8 Calculating Limits Using the Limit Laws#^thm-8-2|§8.2]]) also hold for one-sided limits. The proofs are the same word for word, with the condition $0 < |x - a| < \delta$ replaced by $a < x < a + \delta$ (right-hand limits) or $a - \delta < x < a$ (left-hand limits). For example, $\lim_{x \to a^+} [f(x) g(x)] = \lim_{x \to a^+} f(x) \cdot \lim_{x \to a^+} g(x)$ whenever both right-hand limits exist, even if the two-sided limit of $g$ does not.

^rem-8-2

> [!example] Example §8.4: Comparing One-Sided Limits
> **(a)** Prove that $\displaystyle\lim_{x \to 0} \frac{|x|}{x}$ does not exist.
>
> Since $|x| = x$ for $x > 0$ and $|x| = -x$ for $x < 0$,
>
> $$
> \lim_{x \to 0^+} \frac{|x|}{x} = \lim_{x \to 0^+} \frac{x}{x} = \lim_{x \to 0^+} 1 = 1, \qquad
> \lim_{x \to 0^-} \frac{|x|}{x} = \lim_{x \to 0^-} \frac{-x}{x} = \lim_{x \to 0^-} (-1) = -1 .
> $$
>
> The one-sided limits are different, so by Theorem §8.5 the two-sided limit does not exist. (The graph of $|x|/x$ is the line $y = 1$ for $x > 0$ and $y = -1$ for $x < 0$, with a jump at $0$.)
>
> **(b)** Let
>
> $$
> f(x) = \begin{cases} \sqrt{x - 4} & \text{if } x > 4 \\ 8 - 2x & \text{if } x < 4 . \end{cases}
> $$
>
> Determine whether $\lim_{x \to 4} f(x)$ exists.
>
> For $x > 4$, $f(x) = \sqrt{x - 4}$, and $\lim_{x \to 4^+} \sqrt{x - 4} = 0$. (Law 7 cannot be used here, because the inner limit is $0$, not positive; but $\lim_{u \to 0^+} \sqrt{u} = 0$ by [[§9 The Precise Definition of a Limit#^ex-9-4|Example §9.4]], and the same $\delta = \varepsilon^2$ works for $u = x - 4$.) For $x < 4$, $f(x) = 8 - 2x$, so by direct substitution in the one-sided form,
>
> $$
> \lim_{x \to 4^-} f(x) = \lim_{x \to 4^-} (8 - 2x) = 8 - 2 \cdot 4 = 0 .
> $$
>
> Both one-sided limits equal $0$, so by Theorem §8.5 the limit exists and $\lim_{x \to 4} f(x) = 0$, although $f(4)$ is not defined.
>
> *Stewart: Examples 2.3.8 and 2.3.9*

^ex-8-4

## The Squeeze Theorem

The next two theorems compare the limits of two functions when one is below the other near $a$. Stewart states them with "when $x$ is near $a$ (except possibly at $a$)"; in Appendix F this means: for all $x \ne a$ in some open interval that contains $a$.

> [!theorem] Theorem §8.6: Limits Preserve Inequalities
> If $f(x) \le g(x)$ when $x$ is near $a$ (except possibly at $a$) and the limits of $f$ and $g$ both exist as $x$ approaches $a$, then
>
> $$
> \lim_{x \to a} f(x) \le \lim_{x \to a} g(x) .
> $$
>
> *Stewart: 2.3, Theorem 2; proof in Appendix F*

^thm-8-6

> [!proof]+ Proof
> Let $L = \lim_{x \to a} f(x)$ and $M = \lim_{x \to a} g(x)$, and let $r > 0$ be such that $f(x) \le g(x)$ for all $x$ with $0 < |x - a| < r$. We argue by contradiction: suppose $L > M$. By the Difference Law (Law 2),
>
> $$
> \lim_{x \to a} [g(x) - f(x)] = M - L .
> $$
>
> Take $\varepsilon = L - M$, which is positive by assumption. There is $\delta > 0$ such that
>
> $$
> 0 < |x - a| < \delta \quad\Longrightarrow\quad \big| [g(x) - f(x)] - (M - L) \big| < L - M .
> $$
>
> Since $b \le |b|$ for every number $b$, this gives $[g(x) - f(x)] - (M - L) < L - M$, which simplifies to $g(x) - f(x) < 0$, that is, $g(x) < f(x)$, for all $0 < |x - a| < \delta$. Now take any $x$ with $0 < |x - a| < \min\{\delta, r\}$. Then $g(x) < f(x)$ and $f(x) \le g(x)$, a contradiction. Hence $L \le M$. (Stewart's proof says only "this contradicts $f(x) \le g(x)$"; the $\min\{\delta, r\}$ makes sure we look at an $x$ where the hypothesis holds.)

^pf-8-6

*Uses:* [[§8 Calculating Limits Using the Limit Laws#^thm-8-1|§8.1]] (Law 2), [[§9 The Precise Definition of a Limit#^def-9-1|Def. §9.1]]

Strict inequalities are not preserved: $0 < x^2$ for $x \ne 0$, yet both sides have limit $0$ as $x \to 0$. The theorem only gives $\le$.

> [!theorem] Theorem §8.7: The Squeeze Theorem
> If $f(x) \le g(x) \le h(x)$ when $x$ is near $a$ (except possibly at $a$) and
>
> $$
> \lim_{x \to a} f(x) = \lim_{x \to a} h(x) = L ,
> $$
>
> then
>
> $$
> \lim_{x \to a} g(x) = L .
> $$
>
> Also called the Sandwich Theorem or the Pinching Theorem: if $g(x)$ is squeezed between $f(x)$ and $h(x)$ near $a$, and $f$ and $h$ have the same limit $L$ at $a$, then $g$ is forced to have the limit $L$ too.
>
> *Stewart: 2.3, Theorem 3; proof in Appendix F*

^thm-8-7

> [!proof]+ Proof
> Let $r > 0$ be such that $f(x) \le g(x) \le h(x)$ for $0 < |x - a| < r$, and let $\varepsilon > 0$. Since $\lim_{x \to a} f(x) = L$, there is $\delta_1 > 0$ such that
>
> $$
> 0 < |x - a| < \delta_1 \quad\Longrightarrow\quad |f(x) - L| < \varepsilon, \quad\text{that is,}\quad L - \varepsilon < f(x) < L + \varepsilon .
> $$
>
> Since $\lim_{x \to a} h(x) = L$, there is $\delta_2 > 0$ such that
>
> $$
> 0 < |x - a| < \delta_2 \quad\Longrightarrow\quad L - \varepsilon < h(x) < L + \varepsilon .
> $$
>
> Let $\delta = \min\{\delta_1, \delta_2, r\}$ (Stewart takes $\min\{\delta_1, \delta_2\}$; including $r$ guarantees that the squeeze inequality holds). If $0 < |x - a| < \delta$, then
>
> $$
> L - \varepsilon < f(x) \le g(x) \le h(x) < L + \varepsilon ,
> $$
>
> in particular $L - \varepsilon < g(x) < L + \varepsilon$, that is, $|g(x) - L| < \varepsilon$. Therefore $\lim_{x \to a} g(x) = L$.

^pf-8-7

*Uses:* [[§9 The Precise Definition of a Limit#^def-9-1|Def. §9.1]]

> [!remark]- Connections
> - Hub: [[Squeeze Theorem]]. The same proof for sequences: [[§8 A Discussion About Proofs#^thm-8-1|451 Thm. §8.1]]. Theorem §8.6 for sequences: [[§9 Limit Theorems for Sequences#^prop-9-5|451 Prop. §9.5]], proved by the same contradiction.

> [!example] Example §8.5: Squeezing an Oscillation
> Show that $\displaystyle\lim_{x \to 0} x^2 \sin\frac{1}{x} = 0$.
>
> The Product Law does **not** apply: $\lim_{x \to 0} \sin(1/x)$ does not exist: it oscillates between $-1$ and $1$ infinitely often near $0$, exactly like $\sin(\pi/x)$ in [[§7 The Limit of a Function#^ex-7-2|Example §7.2]](b). Instead, find a smaller and a larger function with limit $0$. The sine of any number lies between $-1$ and $1$, so
>
> $$
> -1 \le \sin\frac{1}{x} \le 1 \qquad (x \ne 0) .
> $$
>
> Multiplying by $x^2 \ge 0$ preserves the inequalities:
>
> $$
> -x^2 \le x^2 \sin\frac{1}{x} \le x^2 .
> $$
>
> Since $\lim_{x \to 0} x^2 = 0$ (Law 10) and $\lim_{x \to 0} (-x^2) = 0$ (Law 3), the Squeeze Theorem with $f(x) = -x^2$, $g(x) = x^2 \sin(1/x)$, $h(x) = x^2$ gives
>
> $$
> \lim_{x \to 0} x^2 \sin\frac{1}{x} = 0 .
> $$
>
> *Stewart: Example 2.3.11*

^ex-8-5

![[m233-8-1.svg]]
*The graph of $x^2 \sin(1/x)$ (blue) oscillates infinitely often near $0$, but always between the parabolas $y = x^2$ and $y = -x^2$ (gray), which pinch together at the origin. The function is forced to the limit $0$ even though $\sin(1/x)$ alone has no limit.*

> [!remark] Remark: Method — Evaluating a Limit
> To find $\lim_{x \to a} f(x)$:
> 1. **Substitute** if you may: for polynomials and rational functions with $a$ in the domain (Theorem §8.3), and later for every function continuous at $a$ ([[§10 Continuity|§10]]). The answer is $f(a)$.
> 2. **$0/0$:** simplify first, then substitute. Factor and cancel the common factor $x - a$ (Example §8.2), expand (Example §8.2(c)), rationalize with a conjugate (Example §8.3), or combine fractions. Theorem §8.4 justifies replacing $f$ by the simplified function.
> 3. **(non-zero)$/0$:** there is no finite limit. Find the signs of numerator and denominator on each side of $a$ to decide between $\infty$, $-\infty$ and "does not exist" ([[§7 The Limit of a Function#^ex-7-5|Example §7.5]]).
> 4. **Piecewise formulas, $|x|$, $\lfloor x \rfloor$:** compute the two one-sided limits with the formula valid on each side and compare them (Theorem §8.5, Example §8.4).
> 5. **A bounded factor without a limit** (such as $\sin(1/x)$) times a factor tending to $0$: squeeze (Theorem §8.7, Example §8.5).
>
> The Product and Quotient Laws may only be used when the individual limits exist (and, for the Quotient Law, the limit of the denominator is not $0$). When they do not, the laws say nothing, and steps 2–5 are needed.

^rem-8-3
