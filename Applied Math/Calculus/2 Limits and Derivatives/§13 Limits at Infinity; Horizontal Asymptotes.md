---
type: section
subject: "[[Calculus]]"
chapter: 2
section: 13
stewart: "2.6"
aliases: ["Stewart 2.6"]
tags: [calculus]
---
← [[§12 Continuity]] · ↑ [[· 2 Limits and Derivatives]] · [[§14 Derivatives and Rates of Change]] →

*Stewart, Section 2.6.*

In [[§8 The Limit of a Function|§8]] and [[§11 The Precise Definition of a Limit|§11]] the variable $x$ approached a number and $f(x)$ could become arbitrarily large. Here the roles are reversed: $x$ grows without bound (positively or negatively) and we ask what happens to $f(x)$. A finite answer $L$ gives a horizontal asymptote $y = L$, which describes the end behavior of the graph. The working rules are the Limit Laws together with $1/x^r \to 0$. The main computational trick is to divide numerator and denominator by the highest power of $x$ in the denominator. The section ends with the ε–$N$ definitions, which make "sufficiently large" precise.

## Limits at Infinity and Horizontal Asymptotes

> [!definition] Definition §13.1: Limit at Infinity
> Let $f$ be defined on some interval $(a, \infty)$. Then
>
> $$
> \lim_{x \to \infty} f(x) = L \qquad\text{(also written } f(x) \to L \text{ as } x \to \infty\text{)}
> $$
>
> means that the values of $f(x)$ can be made arbitrarily close to $L$ by requiring $x$ to be sufficiently large.
>
> Likewise, if $f$ is defined on some interval $(-\infty, a)$, then $\lim_{x \to -\infty} f(x) = L$ means that the values of $f(x)$ can be made arbitrarily close to $L$ by requiring $x$ to be sufficiently large negative.
>
> The symbols $\infty$ and $-\infty$ are not numbers. $\lim_{x \to \infty} f(x) = L$ is read "the limit of $f(x)$, as $x$ approaches infinity (or becomes infinite, or increases without bound), is $L$". The precise version is [[§13 Limits at Infinity; Horizontal Asymptotes#^def-13-4|Definition §13.4]].
>
> *Stewart: 2.6, Definitions 1 and 2*

^def-13-1

> [!remark]- Connections
> - Rigorous treatment: in 451 a limit as $x \to \pm\infty$ is a limit along the set $S = (c, \infty)$ or $(-\infty, c)$, [[§20 Limits of Functions#^def-20-2|451 Def. §20.2]], with the ε–$M$ form in [[§20 Limits of Functions#^rem-20-1|451 Remark: The epsilon-delta version]]. The reciprocal at its four ends, $1/x \to 0$ as $x \to \pm\infty$ and $1/x \to \pm\infty$ as $x \to 0^\pm$: [[§20 Limits of Functions#^ex-20-3|451 Ex. §20.3]].

> [!definition] Definition §13.2: Horizontal Asymptote
> The line $y = L$ is a **horizontal asymptote** of the curve $y = f(x)$ if either
>
> $$
> \lim_{x \to \infty} f(x) = L \qquad\text{or}\qquad \lim_{x \to -\infty} f(x) = L .
> $$
>
> *Stewart: 2.6, Definition 3*

^def-13-2

For example, $y = 1$ is a horizontal asymptote of $y = (x^2 - 1)/(x^2 + 1)$: the values approach $1$ as $x \to \infty$ and as $x \to -\infty$. A graph may approach its asymptote from above, from below, or oscillating around it and crossing it infinitely often; it may also have two different horizontal asymptotes, one at each end, as the next result shows.

> [!remark] Remark: Why It Works
> The graph of $\tan^{-1}$ is the reflection in the line $y = x$ of the graph of $\tan$ restricted to $(-\pi/2, \pi/2)$ ([[§5 Inverse Functions and Logarithms#^thm-5-3|Theorem §5.3]]). The tangent has the vertical asymptotes $x = \pm\pi/2$, and reflecting turns them into the horizontal asymptotes $y = \pm\pi/2$. This is Stewart's argument.

^rem-13-1

> [!theorem] Theorem §13.1: Limits of the Inverse Tangent at Infinity
> $$
> \lim_{x \to -\infty} \tan^{-1} x = -\frac{\pi}{2}, \qquad \lim_{x \to \infty} \tan^{-1} x = \frac{\pi}{2} .
> $$
>
> So both lines $y = -\pi/2$ and $y = \pi/2$ are horizontal asymptotes of $y = \tan^{-1} x$.
>
> *Stewart: 2.6, Equation 4*

^thm-13-1

> [!proof]+ Proof
> Recall that $\tan^{-1}$ is increasing, since $\tan$ is increasing on $(-\pi/2, \pi/2)$, and that its values lie in $(-\pi/2, \pi/2)$. We check [[§13 Limits at Infinity; Horizontal Asymptotes#^def-13-4|Definition §13.4]]. Let $\varepsilon > 0$; making $\varepsilon$ smaller only makes the goal harder, so we may assume $\varepsilon < \pi/2$. Put $N = \tan(\pi/2 - \varepsilon)$. If $x > N$, then
>
> $$
> \frac{\pi}{2} - \varepsilon = \tan^{-1} N < \tan^{-1} x < \frac{\pi}{2}, \qquad\text{so}\qquad \Big| \tan^{-1} x - \frac{\pi}{2} \Big| < \varepsilon .
> $$
>
> Hence $\tan^{-1} x \to \pi/2$ as $x \to \infty$. Since $\tan^{-1}$ is odd ($\tan^{-1}(-x) = -\tan^{-1} x$, because $\tan$ is odd), $x < -N$ gives $|\tan^{-1} x - (-\pi/2)| = |\tan^{-1}(-x) - \pi/2| < \varepsilon$, so $\tan^{-1} x \to -\pi/2$ as $x \to -\infty$.

^pf-13-1

*Uses:* [[§13 Limits at Infinity; Horizontal Asymptotes#^def-13-4|Def. §13.4]], [[§6 Logarithmic and Inverse Trigonometric Functions#^def-6-5|Def. §6.5]] (inverse tangent)

## Evaluating Limits at Infinity

> [!theorem] Theorem §13.2: Limit Laws at Infinity
> The Limit Laws of [[§9 Calculating Limits Using the Limit Laws#^thm-9-1|Theorems §9.1]] and [[§9 Calculating Limits Using the Limit Laws#^thm-9-2|§9.2]], with the exception of Laws 10 and 11, remain valid if "$x \to a$" is replaced by "$x \to \infty$" or "$x \to -\infty$". (Laws 10 and 11, $\lim_{x \to a} x^n = a^n$ and $\lim_{x \to a} \sqrt[n]{x} = \sqrt[n]{a}$, have no meaning with $a = \pm\infty$.)
>
> *Stewart: 2.6 (text)*

^thm-13-2

*Stewart omits the proof ("it can be proved that…"). The ε–δ proofs of the Limit Laws ([[§9 Calculating Limits Using the Limit Laws#^pf-9-1|proof of Theorem §8.1]]) carry over word for word with "$x > N$" in place of "$0 < |x - a| < \delta$". In 451 the laws for every kind of limit follow from the limit theorems for sequences: [[§20 Limits of Functions#^rem-20-2|451 §20, Remark after Thm. §20.2]].*

> [!theorem] Theorem §13.3: Reciprocal Powers Tend to Zero
> If $r > 0$ is a rational number, then
>
> $$
> \lim_{x \to \infty} \frac{1}{x^r} = 0 .
> $$
>
> If $r > 0$ is a rational number such that $x^r$ is defined for all $x$, then
>
> $$
> \lim_{x \to -\infty} \frac{1}{x^r} = 0 .
> $$
>
> *Stewart: 2.6, Theorem 5*

^thm-13-3

> [!proof]+ Proof
> **The case $r = 1$.** When $x$ is large, $1/x$ is small: $1/100 = 0.01$, $1/10{,}000 = 0.0001$, $1/1{,}000{,}000 = 0.000001$. Precisely ([[§13 Limits at Infinity; Horizontal Asymptotes#^def-13-4|Definition §13.4]]): given $\varepsilon > 0$, let $N = 1/\varepsilon$. If $x > N$, then $x > 0$ and
>
> $$
> \Big| \frac1x - 0 \Big| = \frac1x < \frac1N = \varepsilon .
> $$
>
> So $\lim_{x \to \infty} 1/x = 0$. In the same way, $x < -1/\varepsilon$ gives $|1/x| = 1/|x| < \varepsilon$, so $\lim_{x \to -\infty} 1/x = 0$. (These are Stewart's Examples 2.6.2 and 2.6.14.)
>
> **General $r$.** Stewart obtains the theorem from the case $r = 1$ with the Power Law and the Root Law (Laws 6 and 7), writing $r = p/q$ and $1/x^r = \big(\sqrt[q]{1/x}\big)^p$. The Root Law requires a positive limit under an even root, and here the limit is $0$, so we argue directly instead. Write $r = p/q$ with positive integers $p$, $q$ in lowest terms. For $x > 0$, both $x \mapsto \sqrt[q]{x}$ and $x \mapsto x^p$ are increasing, hence so is $x^r = (\sqrt[q]{x})^p$. Given $\varepsilon > 0$, let $N = (1/\varepsilon)^{1/r}$, so that $N^r = 1/\varepsilon$. If $x > N$, then $x^r > N^r = 1/\varepsilon$, so
>
> $$
> 0 < \frac{1}{x^r} < \varepsilon .
> $$
>
> This proves the first statement. If $x^r$ is defined for all $x$, then $q$ is odd, and $|x^r| = |\sqrt[q]{x}|^p = |x|^r$. For $x < -N$ we have $|x| > N$, so $|1/x^r| = 1/|x|^r < \varepsilon$. This proves the second statement.

^pf-13-3

*Uses:* [[§13 Limits at Infinity; Horizontal Asymptotes#^def-13-4|Def. §13.4]]

> [!remark] Remark: Method — Limits at Infinity of Algebraic Expressions
> 1. **Rational functions.** Divide numerator and denominator by the highest power of $x$ that occurs in the *denominator* (we may assume $x \ne 0$). Every term then becomes a constant or a constant times $1/x^r$, and [[§13 Limits at Infinity; Horizontal Asymptotes#^thm-13-3|Theorem §13.3]] with the Limit Laws ([[§13 Limits at Infinity; Horizontal Asymptotes#^thm-13-2|Theorem §13.2]]) finishes the job.
> 2. **Square roots.** Bring the divisor under the root as $x = \sqrt{x^2}$ — but only for $x > 0$. For $x < 0$, $\sqrt{x^2} = |x| = -x$, so dividing by $x$ introduces a minus sign in front of the root.
> 3. **Differences $\infty - \infty$.** The Limit Laws do not apply to infinite limits, since $\infty - \infty$ is not defined. Multiply by the conjugate radical (for roots), or factor (for polynomials), to turn the difference into a product or quotient.
> 4. **Composite expressions.** Substitute a new variable, for instance $t = 1/(x - a)$, which tends to $\pm\infty$ as $x \to a^\pm$, and use a known limit in $t$.

^rem-13-2

> [!example] Example §13.1: A Rational Function
> Evaluate $\displaystyle\lim_{x \to \infty} \frac{3x^2 - x - 2}{5x^2 + 4x + 1}$ and say which properties of limits are used.
>
> Both numerator and denominator become large, so the ratio is not obvious. The highest power of $x$ in the denominator is $x^2$; divide by it:
>
> $$
> \begin{aligned}
> \lim_{x \to \infty} \frac{3x^2 - x - 2}{5x^2 + 4x + 1}
> &= \lim_{x \to \infty} \frac{3 - \dfrac1x - \dfrac{2}{x^2}}{5 + \dfrac4x + \dfrac{1}{x^2}}
> = \frac{\lim_{x \to \infty} \Big(3 - \dfrac1x - \dfrac{2}{x^2}\Big)}{\lim_{x \to \infty} \Big(5 + \dfrac4x + \dfrac{1}{x^2}\Big)} && \text{(Law 5)} \\[4pt]
> &= \frac{\lim 3 - \lim \dfrac1x - 2 \lim \dfrac{1}{x^2}}{\lim 5 + 4 \lim \dfrac1x + \lim \dfrac{1}{x^2}} && \text{(Laws 1, 2 and 3)} \\[4pt]
> &= \frac{3 - 0 - 0}{5 + 0 + 0} = \frac35 && \text{(Law 8 and [[§13 Limits at Infinity; Horizontal Asymptotes#^thm-13-3|Theorem §13.3]])}.
> \end{aligned}
> $$
>
> (Law 5 is justified only at the end, once the denominator's limit is seen to be $5 \ne 0$.) A similar calculation gives the limit $\frac35$ as $x \to -\infty$, so $y = \frac35 = 0.6$ is a horizontal asymptote at both ends.
>
> *Stewart: Example 2.6.3*

^ex-13-1

> [!example] Example §13.2: Two Different Horizontal Asymptotes
> Find the horizontal asymptotes of $f(x) = \dfrac{\sqrt{2x^2 + 1}}{3x - 5}$.
>
> Divide numerator and denominator by $x$, the highest power of $x$ in the denominator. **For $x > 0$**, $x = \sqrt{x^2}$, so
>
> $$
> \lim_{x \to \infty} \frac{\sqrt{2x^2 + 1}}{3x - 5}
> = \lim_{x \to \infty} \frac{\sqrt{\dfrac{2x^2 + 1}{x^2}}}{\dfrac{3x - 5}{x}}
> = \lim_{x \to \infty} \frac{\sqrt{2 + \dfrac{1}{x^2}}}{3 - \dfrac5x}
> = \frac{\sqrt{\lim 2 + \lim \dfrac{1}{x^2}}}{\lim 3 - 5 \lim \dfrac1x}
> = \frac{\sqrt{2 + 0}}{3 - 5 \cdot 0} = \frac{\sqrt2}{3} .
> $$
>
> **For $x < 0$**, $\sqrt{x^2} = |x| = -x$, so $x = -\sqrt{x^2}$ and
>
> $$
> \frac{\sqrt{2x^2 + 1}}{x} = \frac{\sqrt{2x^2 + 1}}{-\sqrt{x^2}} = -\sqrt{\frac{2x^2 + 1}{x^2}} = -\sqrt{2 + \frac{1}{x^2}} .
> $$
>
> Therefore
>
> $$
> \lim_{x \to -\infty} \frac{\sqrt{2x^2 + 1}}{3x - 5} = \lim_{x \to -\infty} \frac{-\sqrt{2 + \dfrac{1}{x^2}}}{3 - \dfrac5x} = \frac{-\sqrt{2 + 0}}{3 - 0} = -\frac{\sqrt2}{3} .
> $$
>
> So $y = \sqrt2/3$ and $y = -\sqrt2/3$ are both horizontal asymptotes. (The root law is used here with the positive limit $2$.)
>
> *Stewart: Example 2.6.4*

^ex-13-2

> [!theorem] Theorem §13.4: The Natural Exponential at Infinity
> $$
> \lim_{x \to -\infty} e^x = 0, \qquad \lim_{x \to \infty} e^x = \infty .
> $$
>
> So the $x$-axis is a horizontal asymptote of $y = e^x$ (on the left). The same holds for every exponential function $b^x$ with $b > 1$. The values of $e^x$ approach $0$ very rapidly: $e^{-5} \approx 0.00674$, $e^{-10} \approx 0.00005$. And as $x \to \infty$, $e^x$ grows much faster than $x^3$ (made precise with l'Hospital's Rule in [[§31 Indeterminate Forms and L'Hospital's Rule#^ex-31-1|Example §31.1]](b)).
>
> *Stewart: 2.6, Equation 6, and text*

^thm-13-4

> [!proof]+ Proof
> Stewart reads both limits off the graph and a table of values. Here is a proof from two facts about $e$ ([[§4 Exponential Functions#^def-4-4|Definition §4.4]], [[§4 Exponential Functions#^prop-4-2|Proposition §4.2]]): $e > 2$, and $e^x$ is increasing because $e > 1$. Also $2^n > n$ for every positive integer $n$ (by induction: $2^1 > 1$, and $2^{n+1} = 2 \cdot 2^n > 2n \ge n + 1$).
>
> **As $x \to -\infty$.** Let $\varepsilon > 0$ and choose an integer $n > 1/\varepsilon$. If $x < -n$, then
>
> $$
> 0 < e^x < e^{-n} = \frac{1}{e^n} < \frac{1}{2^n} < \frac1n < \varepsilon .
> $$
>
> By [[§13 Limits at Infinity; Horizontal Asymptotes#^def-13-4|Definition §13.4]] (with $N = -n$), $\lim_{x \to -\infty} e^x = 0$.
>
> **As $x \to \infty$.** Let $M > 0$ and choose an integer $n > M$. If $x > n$, then $e^x > e^n > 2^n > n > M$. By [[§13 Limits at Infinity; Horizontal Asymptotes#^def-13-5|Definition §13.5]], $\lim_{x \to \infty} e^x = \infty$.
>
> For $b > 1$ the same argument works with $2$ replaced by any rational number $c$ with $1 < c < b$ and the inequality $c^n \ge 1 + n(c - 1)$ (Bernoulli's inequality), which tends to $\infty$.

^pf-13-4

*Uses:* [[§13 Limits at Infinity; Horizontal Asymptotes#^def-13-4|Def. §13.4]], [[§13 Limits at Infinity; Horizontal Asymptotes#^def-13-5|Def. §13.5]], [[§4 Exponential Functions#^def-4-4|Def. §4.4]], [[§4 Exponential Functions#^prop-4-2|§4.2]] (the number e; monotonicity of exponentials)

> [!example] Example §13.3: The Conjugate Radical and New Variables
> **(a)** Compute $\lim_{x \to \infty} \big(\sqrt{x^2 + 1} - x\big)$.
>
> Both terms are large, so this is of the form $\infty - \infty$. Think of the expression as a fraction with denominator $1$ and multiply numerator and denominator by the conjugate radical:
>
> $$
> \lim_{x \to \infty} \big(\sqrt{x^2 + 1} - x\big)
> = \lim_{x \to \infty} \big(\sqrt{x^2 + 1} - x\big) \cdot \frac{\sqrt{x^2 + 1} + x}{\sqrt{x^2 + 1} + x}
> = \lim_{x \to \infty} \frac{(x^2 + 1) - x^2}{\sqrt{x^2 + 1} + x}
> = \lim_{x \to \infty} \frac{1}{\sqrt{x^2 + 1} + x} = 0 ,
> $$
>
> because the denominator $\sqrt{x^2 + 1} + x$ is larger than $x$ and so becomes large as $x \to \infty$.
>
> **(b)** Evaluate $\displaystyle\lim_{x \to 2^+} \arctan\Big(\frac{1}{x - 2}\Big)$.
>
> Let $t = 1/(x - 2)$. As $x \to 2^+$, $x - 2 \to 0$ through positive values, so $t \to \infty$. By the second equation of [[§13 Limits at Infinity; Horizontal Asymptotes#^thm-13-1|Theorem §13.1]],
>
> $$
> \lim_{x \to 2^+} \arctan\Big(\frac{1}{x - 2}\Big) = \lim_{t \to \infty} \arctan t = \frac{\pi}{2} .
> $$
>
> **(c)** Evaluate $\lim_{x \to 0^-} e^{1/x}$.
>
> Let $t = 1/x$. As $x \to 0^-$, $t \to -\infty$, so by [[§13 Limits at Infinity; Horizontal Asymptotes#^thm-13-4|Theorem §13.4]],
>
> $$
> \lim_{x \to 0^-} e^{1/x} = \lim_{t \to -\infty} e^t = 0 .
> $$
>
> (The substitution step is the rule "if $t = g(x) \to \infty$ and $F(t) \to L$ as $t \to \infty$, then $F(g(x)) \to L$". It is proved like the limit of a composite function, [[§12 Continuity#^thm-12-7|Theorem §12.7]]: given $\varepsilon$, choose $N$ for $F$, then $\delta$ so that $g(x) > N$.)
>
> Not every function has a limit at infinity: as $x$ increases, $\sin x$ oscillates between $1$ and $-1$ infinitely often and approaches no number, so $\lim_{x \to \infty} \sin x$ does not exist.
>
> *Stewart: Examples 2.6.5, 2.6.6, 2.6.7 and 2.6.8*

^ex-13-3

## Infinite Limits at Infinity

> [!definition] Definition §13.3: Infinite Limit at Infinity
> The notation
>
> $$
> \lim_{x \to \infty} f(x) = \infty
> $$
>
> indicates that the values of $f(x)$ become large as $x$ becomes large. Similar meanings are attached to
>
> $$
> \lim_{x \to -\infty} f(x) = \infty, \qquad \lim_{x \to \infty} f(x) = -\infty, \qquad \lim_{x \to -\infty} f(x) = -\infty .
> $$
>
> For instance, $\lim_{x \to \infty} x^3 = \infty$ and $\lim_{x \to -\infty} x^3 = -\infty$: $10^3 = 1000$, $100^3 = 10^6$, $1000^3 = 10^9$, and $x^3$ is large negative when $x$ is. The precise version is [[§13 Limits at Infinity; Horizontal Asymptotes#^def-13-5|Definition §13.5]].
>
> *Stewart: 2.6 (text); Example 2.6.9*

^def-13-3

> [!example] Example §13.4: Infinite Limits at Infinity
> **(a)** Find $\lim_{x \to \infty} (x^2 - x)$.
>
> Law 2 would give "$\lim x^2 - \lim x = \infty - \infty$". It does not apply: the Limit Laws cannot be applied to infinite limits, because $\infty$ is not a number and $\infty - \infty$ cannot be defined. Factor instead:
>
> $$
> \lim_{x \to \infty} (x^2 - x) = \lim_{x \to \infty} x(x - 1) = \infty ,
> $$
>
> because both $x$ and $x - 1$ become arbitrarily large, and so does their product.
>
> **(b)** Find $\displaystyle\lim_{x \to \infty} \frac{x^2 + x}{3 - x}$.
>
> As in [[§13 Limits at Infinity; Horizontal Asymptotes#^ex-13-1|Example §13.1]], divide numerator and denominator by $x$, the highest power of $x$ in the denominator:
>
> $$
> \lim_{x \to \infty} \frac{x^2 + x}{3 - x} = \lim_{x \to \infty} \frac{x + 1}{\dfrac3x - 1} = -\infty ,
> $$
>
> because $x + 1 \to \infty$ while $3/x - 1 \to 0 - 1 = -1$ as $x \to \infty$: a large positive number divided by a number near $-1$ is large negative.
>
> *Stewart: Examples 2.6.10 and 2.6.11*

^ex-13-4

Infinite limits at infinity, together with the intercepts, give a quick rough sketch of a polynomial. For $y = (x - 2)^4 (x + 1)^3 (x - 1)$: the $y$-intercept is $-16$, the $x$-intercepts are $2, -1, 1$, and $y \to \infty$ both as $x \to \infty$ (all three factors large positive) and as $x \to -\infty$ (the first factor large positive, the other two large negative). Since $(x - 2)^4 \ge 0$, the graph touches the axis at $2$ without crossing it (Stewart, Example 2.6.12).

## Precise Definitions

> [!definition] Definition §13.4: Precise Definition of a Limit at Infinity
> Let $f$ be defined on some interval $(a, \infty)$. Then
>
> $$
> \lim_{x \to \infty} f(x) = L
> $$
>
> means that for every $\varepsilon > 0$ there is a corresponding number $N$ such that
>
> $$
> \text{if}\quad x > N \quad\text{then}\quad |f(x) - L| < \varepsilon .
> $$
>
> Let $f$ be defined on some interval $(-\infty, a)$. Then $\lim_{x \to -\infty} f(x) = L$ means that for every $\varepsilon > 0$ there is a corresponding number $N$ such that
>
> $$
> \text{if}\quad x < N \quad\text{then}\quad |f(x) - L| < \varepsilon .
> $$
>
> *Stewart: 2.6, Definitions 7 and 8*

^def-13-4

> [!remark] Remark: What the Definition Says
> The values of $f(x)$ can be made to lie within any distance $\varepsilon$ of $L$ by taking $x$ larger than some $N$, where $N$ depends on $\varepsilon$. On the graph: to the right of the vertical line $x = N$, the curve stays in the horizontal band between $y = L - \varepsilon$ and $y = L + \varepsilon$. This must hold however small $\varepsilon$ is, and a smaller $\varepsilon$ usually requires a larger $N$. It is the same game as the ε–δ definition of [[§11 The Precise Definition of a Limit#^def-11-1|Definition §11.1]], with "$x$ close to $a$" replaced by "$x$ beyond $N$". Stewart's Example 2.6.13 finds, from a graph, that $N = 7$ works for the limit of [[§13 Limits at Infinity; Horizontal Asymptotes#^ex-13-1|Example §13.1]] with $\varepsilon = 0.1$; the figure below does it algebraically.

^rem-13-3

![[m233-11-1.svg]]
*[[§13 Limits at Infinity; Horizontal Asymptotes#^def-13-4|Definition §13.4]] for $f(x) = \dfrac{3x^2 - x - 2}{5x^2 + 4x + 1} \to 0.6$ ([[§13 Limits at Infinity; Horizontal Asymptotes#^ex-13-1|Example §13.1]]) with $\varepsilon = 0.1$. Here $f(x) - 0.6 = -\dfrac{3.4x + 2.6}{5x^2 + 4x + 1} < 0$ for $x > 0$, and $|f(x) - 0.6| < 0.1$ reduces to $x^2 - 6x - 5 > 0$, that is, $x > 3 + \sqrt{14} \approx 6.74$. So any $N \ge 6.74$ works (Stewart takes $N = 7$): to the right of $N$ the graph stays inside the band $0.5 < y < 0.7$ (green).*

> [!definition] Definition §13.5: Precise Definition of an Infinite Limit at Infinity
> Let $f$ be defined on some interval $(a, \infty)$. Then
>
> $$
> \lim_{x \to \infty} f(x) = \infty
> $$
>
> means that for every positive number $M$ there is a corresponding positive number $N$ such that
>
> $$
> \text{if}\quad x > N \quad\text{then}\quad f(x) > M .
> $$
>
> Similar definitions apply when either $\infty$ is replaced by $-\infty$: for $x \to -\infty$ the condition $x > N$ becomes $x < -N$, and for the value $-\infty$ the conclusion $f(x) > M$ becomes $f(x) < -M$.
>
> *Stewart: 2.6, Definition 9*

^def-13-5

> [!remark]- Connections
> - The sequence version, divergence to $+\infty$ ("for every $M$ there is $N$ with $s_n > M$ for $n > N$"): [[§9a Divergence to ±∞ and the Ratio Test#^def-9a-1|451 Def. §9a.1]]; 451 treats $\pm\infty$ as possible values of every limit along a set, [[§20 Limits of Functions#^def-20-1|451 Def. §20.1]].
