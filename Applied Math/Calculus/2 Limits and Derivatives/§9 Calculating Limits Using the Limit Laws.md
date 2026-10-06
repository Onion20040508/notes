---
type: section
subject: "[[Calculus]]"
chapter: 2
section: 9
stewart: "2.3"
aliases: ["Stewart 2.3"]
tags: [calculus]
---
← [[§8 The Limit of a Function]] · ↑ [[· 2 Limits and Derivatives]] · [[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem]] →

*Stewart, Section 2.3 · proofs from Section 2.4 and Appendix F.*

Tables and graphs can suggest a limit but cannot settle it ([[§8 The Limit of a Function#^ex-8-2|Example §8.2]]). This section replaces guessing by calculation. The Limit Laws say that limits respect sums, differences, constant multiples, products, quotients, powers and roots; together with the two basic limits $\lim_{x \to a} c = c$ and $\lim_{x \to a} x = a$ they give the limit of every polynomial and rational function by direct substitution. When substitution fails (typically with $0/0$), algebra first replaces the function by one that agrees with it near $a$. One-sided limits handle piecewise formulas, and the Squeeze Theorem handles functions trapped between two others with the same limit. The proofs use the precise definition of a limit from [[§11 The Precise Definition of a Limit#^def-11-1|Definition §11.1]] and are collected right after each result.

## Properties of Limits

> [!remark] Remark: Why It Works
> If $f(x)$ is close to $L$ and $g(x)$ is close to $M$, then $f(x) + g(x)$ should be close to $L + M$, and similarly for the other operations. The proof makes "close" quantitative: to get $f(x) + g(x)$ within $\varepsilon$ of $L + M$, it is enough to get $f(x)$ and $g(x)$ each within $\varepsilon/2$ of their limits. Each law needs only the precise definition of a limit ([[§11 The Precise Definition of a Limit#^def-11-1|Definition §11.1]]) and the Triangle Inequality $|p + q| \le |p| + |q|$ ([[§139 Numbers, Inequalities, and Absolute Values#^thm-139-6|Theorem §139.6]]).

^rem-9-1

> [!theorem] Theorem §9.1: The Limit Laws
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

^thm-9-1

> [!proof]- Proof
> Throughout, $f$ and $g$ are defined on an open interval around $a$, except possibly at $a$, and "$\lim_{x \to a} f(x) = L$" means: for every $\varepsilon > 0$ there is $\delta > 0$ such that $0 < |x - a| < \delta$ implies $|f(x) - L| < \varepsilon$ ([[§11 The Precise Definition of a Limit#^def-11-1|Definition §11.1]]). Each law is proved by producing such a $\delta$.
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
> Hence $\lim_{x \to a} [f(x) + g(x)] = L + M$. (This is the proof Stewart gives in Section 2.4, [[§11 The Precise Definition of a Limit#^def-11-1|right after Definition §11.1]].)
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
> **Law 3 (Constant Multiple Law).** A constant function has limit equal to that constant: for $g(x) = c$ we have $|g(x) - c| = 0 < \varepsilon$ for every $x$, so any $\delta$ works. (This is Law 8 of [[§9 Calculating Limits Using the Limit Laws#^thm-9-2|Theorem §9.2]].) Law 4 with $g(x) = c$ now gives
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

^pf-9-1

*Uses:* [[§11 The Precise Definition of a Limit#^def-11-1|Def. §11.1]], [[§139 Numbers, Inequalities, and Absolute Values#^thm-139-6|§139.6]] (Triangle Inequality), [[§9 Calculating Limits Using the Limit Laws#^thm-9-2|§9.2]] (Law 8)

> [!remark]- Connections
> - Rigorous treatment: 451 obtains these laws for limits of functions ([[§20 Limits of Functions#^rem-20-2|451 Remark after Thm. §20.2]]) from the same laws for sequences, [[§9 Limit Theorems for Sequences#^thm-9-3|451 Thm. §9.3]] (sums and products, with the same add-and-subtract step as Law 4) and [[§9 Limit Theorems for Sequences#^thm-9-4|451 Thm. §9.4]] (quotients, with the same lower bound for the denominator as Law 5).

Repeated use of the Product Law, and two basic limits, give six more laws. Stewart numbers them on from 6.

> [!theorem] Theorem §9.2: Limit Laws 6–11
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
> **Law 7 is proved in Section 2.5**, as [[§12 Continuity#^cor-12-8|Corollary §12.8]]; the other five are proved below.
>
> *Stewart: 2.3, Limit Laws 6–11 (Law 7 proved in 2.5)*

^thm-9-2

> [!proof]+ Proof
> **Law 8.** For every $x$, $|c - c| = 0 < \varepsilon$, so any $\delta > 0$ works in [[§11 The Precise Definition of a Limit#^def-11-1|Definition §11.1]].
>
> **Law 9.** Given $\varepsilon > 0$, take $\delta = \varepsilon$: if $0 < |x - a| < \delta$, then $|x - a| < \varepsilon$.
>
> (Stewart calls Laws 8 and 9 obvious from the graphs of $y = c$ and $y = x$ and leaves the $\varepsilon$–$\delta$ proofs as Exercises 2.4.23–24; these are those proofs.)
>
> **Law 6.** By induction on $n$. For $n = 1$ there is nothing to prove. If Law 6 holds for $n$, then $[f(x)]^{n+1} = [f(x)]^n \cdot f(x)$, and the Product Law (Law 4 of [[§9 Calculating Limits Using the Limit Laws#^thm-9-1|Theorem §9.1]]) gives
>
> $$
> \lim_{x \to a} [f(x)]^{n+1} = \lim_{x \to a} [f(x)]^n \cdot \lim_{x \to a} f(x) = \Big[\lim_{x \to a} f(x)\Big]^n \cdot \lim_{x \to a} f(x) = \Big[\lim_{x \to a} f(x)\Big]^{n+1} .
> $$
>
> **Law 10.** Put $f(x) = x$ in Law 6 and use Law 9: $\lim_{x \to a} x^n = \big[\lim_{x \to a} x\big]^n = a^n$.
>
> **Law 7** is [[§12 Continuity#^cor-12-8|Corollary §12.8]] (Stewart leaves it as Exercise 2.5.69).
>
> **Law 11.** Stewart puts $f(x) = x$ in Law 7 and uses Law 9: $\lim_{x \to a} \sqrt[n]{x} = \sqrt[n]{\lim_{x \to a} x} = \sqrt[n]{a}$ (for even $n$ the hypothesis of Law 7 is $a > 0$). This rests on Law 7 and hence on [[§12 Continuity#^cor-12-8|Corollary §12.8]]. There is no circle: Law 11 says that the root functions are continuous, and [[§12 Continuity#^thm-12-6|Theorem §12.6]] proves that directly (roots are inverses of powers), without Law 7 or Law 11. [[§12 Continuity#^cor-12-8|Corollary §12.8]] then derives Law 7 from it. (For square roots Stewart also outlines an $\varepsilon$–$\delta$ proof in Exercise 2.4.37.)

^pf-9-2

*Uses:* [[§9 Calculating Limits Using the Limit Laws#^thm-9-1|§9.1]], [[§11 The Precise Definition of a Limit#^def-11-1|Def. §11.1]], [[§12 Continuity#^cor-12-8|§12.8]], [[§12 Continuity#^thm-12-6|§12.6]]

> [!example] Example §9.1: Justifying Each Step
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

^ex-9-1

*Continued in [[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem]]: direct substitution, one-sided limits and the Squeeze Theorem.*
