---
type: section
subject: "[[Calculus]]"
chapter: 2
section: 10
stewart: "2.3"
aliases: ["Stewart 2.3 (cont.)"]
tags: [calculus]
---
← [[§9 Calculating Limits Using the Limit Laws]] · ↑ [[· 2 Limits and Derivatives]] · [[§11 The Precise Definition of a Limit]] →

*Stewart, Section 2.3 · proofs from Section 2.4 and Appendix F.*

The Limit Laws of [[§9 Calculating Limits Using the Limit Laws|§9]], together with the two basic limits $\lim_{x \to a} c = c$ and $\lim_{x \to a} x = a$, give the limit of every polynomial and rational function by direct substitution. When substitution fails (typically with $0/0$), algebra first replaces the function by one that agrees with it near $a$. One-sided limits handle piecewise formulas, and the Squeeze Theorem handles functions trapped between two others with the same limit.

## Evaluating Limits by Direct Substitution

> [!theorem] Theorem §12.1: Direct Substitution Property
> If $f$ is a polynomial or a rational function and $a$ is in the domain of $f$, then
>
> $$
> \lim_{x \to a} f(x) = f(a) .
> $$
>
> *Stewart: 2.3, Direct Substitution Property*

^thm-10-1

> [!proof]+ Proof
> Stewart: "similar use of the Limit Laws" as in [[§9 Calculating Limits Using the Limit Laws#^ex-9-1|Example §9.1]] proves this (his Exercises 59 and 60). Here is that argument.
>
> **Polynomials.** Let $P(x) = c_n x^n + c_{n-1} x^{n-1} + \cdots + c_1 x + c_0$. By Law 3 and Law 10, $\lim_{x \to a} c_k x^k = c_k a^k$ for $k = 1, \ldots, n$, and by Law 8, $\lim_{x \to a} c_0 = c_0$. Applying Law 1 to these $n + 1$ terms ($n$ times, one term at a time),
>
> $$
> \lim_{x \to a} P(x) = c_n a^n + \cdots + c_1 a + c_0 = P(a) .
> $$
>
> **Rational functions.** Let $f = P/Q$ with polynomials $P$, $Q$, and let $a$ be in the domain of $f$, that is, $Q(a) \ne 0$. By the polynomial case, $\lim_{x \to a} P(x) = P(a)$ and $\lim_{x \to a} Q(x) = Q(a) \ne 0$, so Law 5 gives $\lim_{x \to a} f(x) = P(a)/Q(a) = f(a)$.

^pf-10-1

*Uses:* [[§9 Calculating Limits Using the Limit Laws#^thm-9-1|§9.1]] (Laws 1, 3, 5), [[§9 Calculating Limits Using the Limit Laws#^thm-9-2|§9.2]] (Laws 8, 10)

Functions with the Direct Substitution Property at $a$ are called **continuous at $a$** ([[§12 Continuity#^def-12-1|Definition §12.1]]); in that language this theorem is [[§12 Continuity#^thm-12-2|Theorem §12.2]]. Not every limit can be found by substitution: the interesting ones in calculus are of the form $0/0$ at $a$. The next fact lets us change the function at $a$ itself without changing the limit.

> [!theorem] Theorem §12.2: Functions That Agree Except at a
> If $f(x) = g(x)$ when $x \ne a$, then $\lim_{x \to a} f(x) = \lim_{x \to a} g(x)$, provided the limits exist.
>
> *Stewart: 2.3 (boxed statement after Example 3)*

^thm-10-2

> [!proof]+ Proof
> Stewart's reason: in computing a limit as $x \to a$ we never consider $x = a$. Precisely: suppose $\lim_{x \to a} g(x) = L$ and let $\varepsilon > 0$. Take $\delta > 0$ such that $0 < |x - a| < \delta$ implies $|g(x) - L| < \varepsilon$. For such $x$ we have $x \ne a$, so $f(x) = g(x)$ and $|f(x) - L| = |g(x) - L| < \varepsilon$. So $\lim_{x \to a} f(x) = L$ as well.
>
> The argument shows a little more than the statement: if one of the two limits exists, so does the other, and they are equal.

^pf-10-2

*Uses:* [[§11 The Precise Definition of a Limit#^def-11-1|Def. §11.1]]

> [!example] Example §12.1: Cancelling a Common Factor
> **(a)** Find $\displaystyle\lim_{x \to 1} \frac{x^2 - 1}{x - 1}$.
>
> Substituting $x = 1$ is impossible ($f(1)$ is $0/0$, undefined), and the Quotient Law does not apply because the limit of the denominator is $0$. Factor the numerator as a difference of squares:
>
> $$
> \frac{x^2 - 1}{x - 1} = \frac{(x - 1)(x + 1)}{x - 1} = x + 1 \qquad (x \ne 1) .
> $$
>
> Cancelling is legitimate because $x \ne 1$, so $x - 1 \ne 0$. The two functions agree except at $1$, so by [[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^thm-10-2|Theorem §10.2]] and direct substitution ([[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^thm-10-1|Theorem §10.1]]),
>
> $$
> \lim_{x \to 1} \frac{x^2 - 1}{x - 1} = \lim_{x \to 1} (x + 1) = 1 + 1 = 2 .
> $$
>
> This is the slope of the tangent to $y = x^2$ at $(1, 1)$ from [[§7 The Tangent and Velocity Problems#^ex-7-1|Example §7.1]].
>
> **(b)** Find $\lim_{x \to 1} g(x)$ for $g(x) = x + 1$ if $x \ne 1$ and $g(1) = \pi$.
>
> The value $g(1) = \pi$ is irrelevant. Since $g(x) = x + 1$ for $x \ne 1$, [[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^thm-10-2|Theorem §10.2]] gives $\lim_{x \to 1} g(x) = \lim_{x \to 1} (x + 1) = 2$. The functions of (a) and (b) differ only at $x = 1$ (one is undefined there, the other equals $\pi$), so they have the same limit.
>
> **(c)** Evaluate $\displaystyle\lim_{h \to 0} \frac{(3 + h)^2 - 9}{h}$.
>
> Again $h = 0$ gives $0/0$. Expand and cancel, remembering that $h \ne 0$:
>
> $$
> \frac{(3 + h)^2 - 9}{h} = \frac{9 + 6h + h^2 - 9}{h} = \frac{h(6 + h)}{h} = 6 + h ,
> $$
>
> so the limit is $\lim_{h \to 0} (6 + h) = 6$. (This is the slope of the tangent to $y = x^2$ at $(3, 9)$; limits of this shape are derivatives, [[§14 Derivatives and Rates of Change#^def-14-3|Definition §14.3]].)
>
> *Stewart: Examples 2.3.3, 2.3.4 and 2.3.5*

^ex-10-1

> [!example] Example §12.2: Rationalizing the Numerator
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
> The last line uses Laws 5, 1, 7, 8 and 10. Law 7 applies because $\lim_{t \to 0} (t^2 + 9) = 9 > 0$. This confirms the value guessed from a table in [[§8 The Limit of a Function#^ex-8-1|Example §8.1]], where the calculator went wrong for very small $t$. The algebra removed the subtraction of nearly equal numbers $\sqrt{t^2 + 9} - 3$ that caused the trouble.
>
> *Stewart: Example 2.3.6*

^ex-10-2

## Using One-Sided Limits

> [!theorem] Theorem §12.3: Two-Sided and One-Sided Limits
> $$
> \lim_{x \to a} f(x) = L \qquad\text{if and only if}\qquad \lim_{x \to a^-} f(x) = L = \lim_{x \to a^+} f(x) .
> $$
>
> So the two-sided limit exists exactly when both one-sided limits exist and are equal.
>
> *Stewart: 2.3, Theorem 1 (stated first as 2.2, box 3)*

^thm-10-3

> [!proof]+ Proof
> Stewart observes this in Section 2.2 by comparing the intuitive definitions, and asks for a proof from the precise ones in Exercise 2.4.40. Here it is, with [[§11 The Precise Definition of a Limit#^def-11-1|Definition §11.1]] (two-sided) and [[§11 The Precise Definition of a Limit#^def-11-2|Definition §11.2]] (one-sided).
>
> ($\Rightarrow$) Let $\varepsilon > 0$ and take $\delta > 0$ with $|f(x) - L| < \varepsilon$ whenever $0 < |x - a| < \delta$. If $a - \delta < x < a$, then $0 < |x - a| < \delta$, so $|f(x) - L| < \varepsilon$: this $\delta$ works for the left-hand limit. In the same way it works for $a < x < a + \delta$, the right-hand limit.
>
> ($\Leftarrow$) Let $\varepsilon > 0$. The left-hand limit gives $\delta_1 > 0$ with $|f(x) - L| < \varepsilon$ for $a - \delta_1 < x < a$, and the right-hand limit gives $\delta_2 > 0$ with $|f(x) - L| < \varepsilon$ for $a < x < a + \delta_2$. Let $\delta = \min\{\delta_1, \delta_2\}$. If $0 < |x - a| < \delta$, then either $a - \delta_1 \le a - \delta < x < a$ or $a < x < a + \delta \le a + \delta_2$, and in both cases $|f(x) - L| < \varepsilon$. So $\lim_{x \to a} f(x) = L$.

^pf-10-3

*Uses:* [[§11 The Precise Definition of a Limit#^def-11-1|Def. §11.1]], [[§11 The Precise Definition of a Limit#^def-11-2|Def. §11.2]]

> [!remark]- Connections
> - Rigorous treatment: [[§20 Limits of Functions#^thm-20-2|451 Thm. §20.2]], with the same choice $\delta = \min\{\delta_1, \delta_2\}$.

> [!remark] Remark: The Limit Laws for One-Sided Limits
> Stewart uses the fact that the Limit Laws ([[§9 Calculating Limits Using the Limit Laws#^thm-9-1|Theorems §9.1]] and [[§9 Calculating Limits Using the Limit Laws#^thm-9-2|§9.2]]) also hold for one-sided limits. The proofs are the same word for word, with the condition $0 < |x - a| < \delta$ replaced by $a < x < a + \delta$ (right-hand limits) or $a - \delta < x < a$ (left-hand limits). For example, $\lim_{x \to a^+} [f(x) g(x)] = \lim_{x \to a^+} f(x) \cdot \lim_{x \to a^+} g(x)$ whenever both right-hand limits exist, even if the two-sided limit of $g$ does not.

^rem-10-2

> [!definition] Definition §12.1: Greatest Integer Function
> The **greatest integer function** (or **floor function**) is defined by
>
> $$
> \lfloor x \rfloor = \text{the largest integer that is less than or equal to } x .
> $$
>
> For instance, $\lfloor 4 \rfloor = 4$, $\lfloor 4.8 \rfloor = 4$, $\lfloor \pi \rfloor = 3$, $\lfloor \sqrt2 \rfloor = 1$ and $\lfloor -\frac12 \rfloor = -1$. For each integer $n$, $\lfloor x \rfloor = n$ exactly when $n \le x < n + 1$, so the graph is a staircase of horizontal segments, each closed at its left end and open at its right end. (Stewart writes $[\![x]\!]$; other notations are $[x]$ and $\lfloor x \rfloor$.)
>
> *Stewart: Example 2.3.10*

^def-10-1

> [!example] Example §12.3: Comparing One-Sided Limits
> **(a)** Prove that $\displaystyle\lim_{x \to 0} \frac{|x|}{x}$ does not exist.
>
> Since $|x| = x$ for $x > 0$ and $|x| = -x$ for $x < 0$,
>
> $$
> \lim_{x \to 0^+} \frac{|x|}{x} = \lim_{x \to 0^+} \frac{x}{x} = \lim_{x \to 0^+} 1 = 1, \qquad
> \lim_{x \to 0^-} \frac{|x|}{x} = \lim_{x \to 0^-} \frac{-x}{x} = \lim_{x \to 0^-} (-1) = -1 .
> $$
>
> The one-sided limits are different, so by [[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^thm-10-3|Theorem §10.3]] the two-sided limit does not exist. (The graph of $|x|/x$ is the line $y = 1$ for $x > 0$ and $y = -1$ for $x < 0$, with a jump at $0$.)
>
> **(b)** Let
>
> $$
> f(x) = \begin{cases} \sqrt{x - 4} & \text{if } x > 4 \\ 8 - 2x & \text{if } x < 4 . \end{cases}
> $$
>
> Determine whether $\lim_{x \to 4} f(x)$ exists.
>
> For $x > 4$, $f(x) = \sqrt{x - 4}$, and $\lim_{x \to 4^+} \sqrt{x - 4} = 0$. (Law 7 cannot be used here, because the inner limit is $0$, not positive; but $\lim_{u \to 0^+} \sqrt{u} = 0$ by [[§11 The Precise Definition of a Limit#^ex-11-4|Example §11.4]], and the same $\delta = \varepsilon^2$ works for $u = x - 4$.) For $x < 4$, $f(x) = 8 - 2x$, so by direct substitution in the one-sided form,
>
> $$
> \lim_{x \to 4^-} f(x) = \lim_{x \to 4^-} (8 - 2x) = 8 - 2 \cdot 4 = 0 .
> $$
>
> Both one-sided limits equal $0$, so by [[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^thm-10-3|Theorem §10.3]] the limit exists and $\lim_{x \to 4} f(x) = 0$, although $f(4)$ is not defined.
>
> **(c)** Show that $\lim_{x \to 3} \lfloor x \rfloor$ does not exist.
>
> Since $\lfloor x \rfloor = 3$ for $3 \le x < 4$ and $\lfloor x \rfloor = 2$ for $2 \le x < 3$ ([[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^def-10-1|Definition §10.1]]),
>
> $$
> \lim_{x \to 3^+} \lfloor x \rfloor = \lim_{x \to 3^+} 3 = 3, \qquad \lim_{x \to 3^-} \lfloor x \rfloor = \lim_{x \to 3^-} 2 = 2 .
> $$
>
> The one-sided limits differ, so $\lim_{x \to 3} \lfloor x \rfloor$ does not exist ([[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^thm-10-3|Theorem §10.3]]). The same happens at every integer ([[§12 Continuity#^ex-12-1|Example §12.1]](d)).
>
> *Stewart: Examples 2.3.8, 2.3.9 and 2.3.10*

^ex-10-3

## The Squeeze Theorem

The next two theorems compare the limits of two functions when one is below the other near $a$. Stewart states them with "when $x$ is near $a$ (except possibly at $a$)"; in Appendix F this means: for all $x \ne a$ in some open interval that contains $a$.

> [!theorem] Theorem §12.4: Limits Preserve Inequalities
> If $f(x) \le g(x)$ when $x$ is near $a$ (except possibly at $a$) and the limits of $f$ and $g$ both exist as $x$ approaches $a$, then
>
> $$
> \lim_{x \to a} f(x) \le \lim_{x \to a} g(x) .
> $$
>
> *Stewart: 2.3, Theorem 2; proof in Appendix F*

^thm-10-4

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

^pf-10-4

*Uses:* [[§9 Calculating Limits Using the Limit Laws#^thm-9-1|§9.1]] (Law 2), [[§11 The Precise Definition of a Limit#^def-11-1|Def. §11.1]]

Strict inequalities are not preserved: $0 < x^2$ for $x \ne 0$, yet both sides have limit $0$ as $x \to 0$. The theorem only gives $\le$.

> [!theorem] Theorem §12.5: The Squeeze Theorem
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

^thm-10-5

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

^pf-10-5

*Uses:* [[§11 The Precise Definition of a Limit#^def-11-1|Def. §11.1]]

> [!remark]- Connections
> - Hub: [[Squeeze Theorem]]. The same proof for sequences: [[§8 A Discussion About Proofs#^thm-8-1|451 Thm. §8.1]]. [[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^thm-10-4|Theorem §10.4]] for sequences: [[§9 Limit Theorems for Sequences#^prop-9-5|451 Prop. §9.5]], proved by the same contradiction.

> [!example] Example §12.4: Squeezing an Oscillation
> Show that $\displaystyle\lim_{x \to 0} x^2 \sin\frac{1}{x} = 0$.
>
> The Product Law does **not** apply: $\lim_{x \to 0} \sin(1/x)$ does not exist: it oscillates between $-1$ and $1$ infinitely often near $0$, exactly like $\sin(\pi/x)$ in [[§8 The Limit of a Function#^ex-8-2|Example §8.2]](b). Instead, find a smaller and a larger function with limit $0$. The sine of any number lies between $-1$ and $1$, so
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

^ex-10-4

![[m233-8-1.svg]]
*The graph of $x^2 \sin(1/x)$ (blue) oscillates infinitely often near $0$, but always between the parabolas $y = x^2$ and $y = -x^2$ (gray), which pinch together at the origin. The function is forced to the limit $0$ even though $\sin(1/x)$ alone has no limit.*

> [!remark] Remark: Method — Evaluating a Limit
> To find $\lim_{x \to a} f(x)$:
> 1. **Substitute** if you may: for polynomials and rational functions with $a$ in the domain ([[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^thm-10-1|Theorem §10.1]]), and later for every function continuous at $a$ ([[§12 Continuity#^def-12-1|Definition §12.1]], [[§12 Continuity#^thm-12-6|Theorem §12.6]]). The answer is $f(a)$.
> 2. **$0/0$:** simplify first, then substitute. Factor and cancel the common factor $x - a$ ([[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^ex-10-1|Example §10.1]]), expand ([[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^ex-10-1|Example §10.1]](c)), rationalize with a conjugate ([[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^ex-10-2|Example §10.2]]), or combine fractions. [[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^thm-10-2|Theorem §10.2]] justifies replacing $f$ by the simplified function.
> 3. **(non-zero)$/0$:** there is no finite limit. Find the signs of numerator and denominator on each side of $a$ to decide between $\infty$, $-\infty$ and "does not exist" ([[§8 The Limit of a Function#^ex-8-5|Example §8.5]]).
> 4. **Piecewise formulas, $|x|$, $\lfloor x \rfloor$:** compute the two one-sided limits with the formula valid on each side and compare them ([[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^thm-10-3|Theorem §10.3]], [[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^ex-10-3|Example §10.3]]).
> 5. **A bounded factor without a limit** (such as $\sin(1/x)$) times a factor tending to $0$: squeeze ([[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^thm-10-5|Theorem §10.5]], [[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^ex-10-4|Example §10.4]]).
>
> The Product and Quotient Laws may only be used when the individual limits exist (and, for the Quotient Law, the limit of the denominator is not $0$). When they do not, the laws say nothing, and steps 2–5 are needed.

^rem-10-3
