---
type: section
subject: "[[Calculus]]"
chapter: 2
section: 11
stewart: "2.4"
aliases: ["Stewart 2.4"]
tags: [calculus]
---
← [[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem]] · ↑ [[· 2 Limits and Derivatives]] · [[§12 Continuity]] →

*Stewart, Section 2.4.*

The intuitive definition of [[§8 The Limit of a Function#^def-8-1|Definition §8.1]] uses vague phrases such as "close to $a$" and "arbitrarily close to $L$". To *prove* that $\lim_{x \to 0} \big(x^3 + \frac{\cos 5x}{10{,}000}\big) = 0.0001$ or that $\lim_{x \to 0} \frac{\sin x}{x} = 1$, the definition must be made precise. This section does so with the $\varepsilon$–$\delta$ definition: for every error tolerance $\varepsilon > 0$ for $f(x)$ there is a tolerance $\delta > 0$ for $x$. It shows how to find $\delta$ in examples, gives the precise versions of one-sided and infinite limits, and uses the definition to prove the Sum Law. The other Limit Laws and the Squeeze Theorem are proved from this definition in [[§9 Calculating Limits Using the Limit Laws|§9]] ([[§9 Calculating Limits Using the Limit Laws#^thm-9-1|Theorem §9.1]], [[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^thm-10-5|Theorem §10.5]]).

## The Precise Definition of a Limit

Consider $f(x) = 2x - 1$ for $x \ne 3$, $f(3) = 6$. Intuitively $\lim_{x \to 3} f(x) = 5$. How close to $3$ must $x$ be for $f(x)$ to differ from $5$ by less than $0.1$? The distance from $x$ to $3$ is $|x - 3|$ and the distance from $f(x)$ to $5$ is $|f(x) - 5|$, so we want a number $\delta$ such that

$$
|f(x) - 5| < 0.1 \quad\text{if}\quad 0 < |x - 3| < \delta .
$$

(The condition $0 < |x - 3|$ says $x \ne 3$.) For $x \ne 3$, $|f(x) - 5| = |(2x - 1) - 5| = |2x - 6| = 2|x - 3|$. So if $0 < |x - 3| < 0.1/2 = 0.05$, then $|f(x) - 5| < 2(0.05) = 0.1$: $\delta = 0.05$ answers the question. For the tolerance $0.01$ the same computation gives $\delta = 0.005$, and for $0.001$ it gives $\delta = 0.0005$. For $5$ to be the limit, $f(x)$ must come within *every* positive tolerance $\varepsilon$ of $5$, and it does:

$$
|f(x) - 5| < \varepsilon \quad\text{if}\quad 0 < |x - 3| < \delta = \frac{\varepsilon}{2} .
$$

In terms of intervals: if $3 - \delta < x < 3 + \delta$ and $x \ne 3$, then $5 - \varepsilon < f(x) < 5 + \varepsilon$. Note that the value $f(3) = 6$ plays no role.

> [!definition] Definition §13.1: Precise Definition of a Limit
> Let $f$ be a function defined on some open interval that contains the number $a$, except possibly at $a$ itself. We say that the **limit of $f(x)$ as $x$ approaches $a$ is $L$**, and write
>
> $$
> \lim_{x \to a} f(x) = L ,
> $$
>
> if for every number $\varepsilon > 0$ there is a number $\delta > 0$ such that
>
> $$
> \text{if} \quad 0 < |x - a| < \delta \quad \text{then} \quad |f(x) - L| < \varepsilon .
> $$
>
> In terms of intervals: for every $\varepsilon > 0$ (no matter how small) there is $\delta > 0$ such that if $x$ lies in the open interval $(a - \delta, a + \delta)$ and $x \ne a$, then $f(x)$ lies in the open interval $(L - \varepsilon, L + \varepsilon)$.
>
> *Stewart: 2.4, Definition 2*

^def-11-1

> [!remark] Remark: Reading the Definition
> - **In words.** $|x - a|$ is the distance from $x$ to $a$ and $|f(x) - L|$ is the distance from $f(x)$ to $L$. So the definition says: the distance from $f(x)$ to $L$ can be made arbitrarily small by requiring the distance from $x$ to $a$ to be sufficiently small (but not $0$).
> - **On the graph.** Draw the horizontal lines $y = L - \varepsilon$ and $y = L + \varepsilon$. The definition asks for a $\delta > 0$ such that over the interval $(a - \delta, a + \delta)$, with $x = a$ left out, the graph of $f$ stays between the two lines. Once such a $\delta$ is found, every smaller $\delta$ works too. A smaller $\varepsilon$ usually requires a smaller $\delta$.
> - **As a game.** Person A names a tolerance $\varepsilon$ (say $0.01$); person B must answer with a $\delta$ such that $0 < |x - a| < \delta$ forces $|f(x) - L| < \varepsilon$. A then names a smaller $\varepsilon$ (say $0.0001$), and B must answer again. $\lim_{x \to a} f(x) = L$ means that B can always win, however small A makes $\varepsilon$. A single $\varepsilon$, such as the one in [[§11 The Precise Definition of a Limit#^ex-11-1|Example §11.1]] below, illustrates the definition but proves nothing.

^rem-11-1

> [!remark]- Connections
> - Rigorous treatment: this is the $\varepsilon$–$\delta$ form [[§20 Limits of Functions#^rem-20-1|451 Remark: The epsilon-delta version]] of [[§20 Limits of Functions#^def-20-1|451 Def. §20.1]], which 451 states with sequences. The same pattern ("for every $\varepsilon$ there is $N$") defines convergence of sequences, [[§7 Limits of Sequences#^def-7-2|451 Def. §7.2]].

> [!example] Example §13.1: Finding a Delta from a Graph
> Since $f(x) = x^3 - 5x + 6$ is a polynomial, $\lim_{x \to 1} f(x) = f(1) = 1 - 5 + 6 = 2$ by direct substitution ([[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^thm-10-1|Theorem §10.1]]). Use a graph to find a number $\delta$ such that
>
> $$
> \text{if} \quad |x - 1| < \delta \quad \text{then} \quad |(x^3 - 5x + 6) - 2| < 0.2 ,
> $$
>
> that is, a $\delta$ that corresponds to $\varepsilon = 0.2$ in [[§11 The Precise Definition of a Limit#^def-11-1|Definition §11.1]] with $a = 1$, $L = 2$.
>
> The inequality $|(x^3 - 5x + 6) - 2| < 0.2$ means $1.8 < x^3 - 5x + 6 < 2.2$: the curve must lie between the lines $y = 1.8$ and $y = 2.2$. Near $(1, 2)$ the curve is falling. It meets $y = 2.2$ at $x \approx 0.911$ and $y = 1.8$ at $x \approx 1.124$. Rounding toward $1$ to be safe,
>
> $$
> \text{if} \quad 0.92 < x < 1.12 \quad \text{then} \quad 1.8 < x^3 - 5x + 6 < 2.2 .
> $$
>
> This interval is not symmetric about $1$: the distance from $1$ to $0.92$ is $0.08$, and to $1.12$ it is $0.12$. Take the smaller, $\delta = 0.08$. Then
>
> $$
> \text{if} \quad |x - 1| < 0.08 \quad \text{then} \quad |(x^3 - 5x + 6) - 2| < 0.2 .
> $$
>
> Any smaller positive $\delta$ works as well.
>
> **Check without the graph.** $f(x) - 2 = x^3 - 5x + 4 = (x - 1)(x^2 + x - 4)$. For $0.92 < x < 1.08$, $x^2 + x - 4$ is increasing (as $x > -\frac12$), so it lies between $0.92^2 + 0.92 - 4 = -2.2336$ and $1.08^2 + 1.08 - 4 = -1.7536$. Hence $|f(x) - 2| < 0.08 \times 2.2336 \approx 0.179 < 0.2$.
>
> *Stewart: Example 2.4.1*

^ex-11-1

> [!remark] Remark: Method — Proving a Limit from the Definition
> To prove $\lim_{x \to a} f(x) = L$ from [[§11 The Precise Definition of a Limit#^def-11-1|Definition §11.1]]:
> 1. **Guess $\delta$ (scratch work).** Let $\varepsilon > 0$ be given. Simplify $|f(x) - L|$ until it shows a factor $|x - a|$, say $|f(x) - L| = |x - a| \cdot |q(x)|$.
> 2. If $q$ is a constant $C$, take $\delta = \varepsilon / C$ ([[§11 The Precise Definition of a Limit#^ex-11-2|Example §11.2]]).
> 3. If $q(x)$ varies, bound it near $a$ first: restrict to $|x - a| < 1$ (or some other fixed distance), find a constant $C$ with $|q(x)| < C$ there, and take $\delta = \min\{1, \varepsilon / C\}$ ([[§11 The Precise Definition of a Limit#^ex-11-3|Example §11.3]]).
> 4. **Prove that $\delta$ works.** Start again from "Given $\varepsilon > 0$, let $\delta = \ldots$. If $0 < |x - a| < \delta$, then …" and derive $|f(x) - L| < \varepsilon$ step by step.
>
> The scratch work of steps 1–3 runs backward from the conclusion; only step 4 is the proof. This two-stage pattern, an intelligent guess followed by a proof that the guess is right, is typical of much of mathematics.

^rem-11-2

> [!example] Example §13.2: A Linear Function
> Prove that $\displaystyle\lim_{x \to 3} (4x - 5) = 7$.
>
> **1. Guessing $\delta$.** Let $\varepsilon > 0$. We want $\delta$ such that $0 < |x - 3| < \delta$ implies $|(4x - 5) - 7| < \varepsilon$. Now $|(4x - 5) - 7| = |4x - 12| = 4|x - 3|$, so we want
>
> $$
> 0 < |x - 3| < \delta \quad\Longrightarrow\quad 4|x - 3| < \varepsilon, \quad\text{that is,}\quad |x - 3| < \frac{\varepsilon}{4} .
> $$
>
> This suggests $\delta = \varepsilon / 4$.
>
> **2. Showing that this $\delta$ works.** Given $\varepsilon > 0$, choose $\delta = \varepsilon / 4$. If $0 < |x - 3| < \delta$, then
>
> $$
> |(4x - 5) - 7| = |4x - 12| = 4|x - 3| < 4\delta = 4 \cdot \frac{\varepsilon}{4} = \varepsilon .
> $$
>
> So $0 < |x - 3| < \delta$ implies $|(4x - 5) - 7| < \varepsilon$, and by [[§11 The Precise Definition of a Limit#^def-11-1|Definition §11.1]], $\lim_{x \to 3} (4x - 5) = 7$. On the graph: the steep line $y = 4x - 5$ stays between $y = 7 - \varepsilon$ and $y = 7 + \varepsilon$ over the interval $(3 - \frac{\varepsilon}{4}, 3 + \frac{\varepsilon}{4})$, a window four times narrower than the band.
>
> *Stewart: Example 2.4.2*

^ex-11-2

> [!example] Example §13.3: A Quadratic Function
> Prove that $\displaystyle\lim_{x \to 3} x^2 = 9$.
>
> **1. Guessing $\delta$.** Let $\varepsilon > 0$. We want $\delta$ such that $0 < |x - 3| < \delta$ implies $|x^2 - 9| < \varepsilon$. Factor: $|x^2 - 9| = |x + 3|\,|x - 3|$. If there were a constant $C$ with $|x + 3| < C$, then $|x + 3|\,|x - 3| < C|x - 3|$, and $C|x - 3| < \varepsilon$ when $|x - 3| < \varepsilon / C$. Such a $C$ exists if $x$ stays in an interval around $3$. We only care about $x$ close to $3$, so we may assume $|x - 3| < 1$. Then $2 < x < 4$, so $5 < x + 3 < 7$ and $|x + 3| < 7$: take $C = 7$. Now there are two requirements, $|x - 3| < 1$ and $|x - 3| < \varepsilon / 7$, and both hold if $\delta = \min\{1, \varepsilon/7\}$, the smaller of the two numbers.
>
> **2. Showing that this $\delta$ works.** Given $\varepsilon > 0$, let $\delta = \min\{1, \varepsilon/7\}$. If $0 < |x - 3| < \delta$, then $|x - 3| < 1$, so $2 < x < 4$ and $|x + 3| < 7$. Also $|x - 3| < \varepsilon / 7$. Therefore
>
> $$
> |x^2 - 9| = |x + 3|\,|x - 3| < 7 \cdot \frac{\varepsilon}{7} = \varepsilon .
> $$
>
> This shows $\lim_{x \to 3} x^2 = 9$.
>
> *Stewart: Example 2.4.3*

^ex-11-3

![[m233-9-1.svg]]
*[[§11 The Precise Definition of a Limit#^ex-11-3|Example §11.3]] with $\varepsilon = 2$. The graph of $y = x^2$ (blue) must stay in the band $7 < y < 11$ (shaded). It does so exactly for $\sqrt7 < x < \sqrt{11}$ (dashed), and the window $|x - 3| < \delta = \min\{1, \frac27\} = \frac27$ (red box) lies inside that interval, so over the window the graph leaves the box only through its sides. The best possible $\delta$ here is $\sqrt{11} - 3 \approx 0.317$, slightly more than $\frac27 \approx 0.286$: the estimate $|x + 3| < 7$ costs little.*

## One-Sided Limits

> [!definition] Definition §13.2: Precise Definition of One-Sided Limits
> **Left-hand limit.** $\displaystyle\lim_{x \to a^-} f(x) = L$ if for every number $\varepsilon > 0$ there is a number $\delta > 0$ such that
>
> $$
> \text{if} \quad a - \delta < x < a \quad \text{then} \quad |f(x) - L| < \varepsilon .
> $$
>
> **Right-hand limit.** $\displaystyle\lim_{x \to a^+} f(x) = L$ if for every number $\varepsilon > 0$ there is a number $\delta > 0$ such that
>
> $$
> \text{if} \quad a < x < a + \delta \quad \text{then} \quad |f(x) - L| < \varepsilon .
> $$
>
> These are [[§11 The Precise Definition of a Limit#^def-11-1|Definition §11.1]] with $x$ restricted to the left half $(a - \delta, a)$ or the right half $(a, a + \delta)$ of the interval $(a - \delta, a + \delta)$. They make [[§8 The Limit of a Function#^def-8-2|Definition §8.2]] precise.
>
> *Stewart: 2.4, Definitions 3 and 4*

^def-11-2

With Definitions [[§11 The Precise Definition of a Limit#^def-11-1|§11.1]] and [[§11 The Precise Definition of a Limit#^def-11-2|§11.2]], the statement that a limit exists exactly when both one-sided limits exist and are equal becomes a theorem with a proof: [[§10 Direct Substitution, One-Sided Limits and the Squeeze Theorem#^thm-10-3|Theorem §10.3]].

> [!example] Example §13.4: The Square Root at 0
> Use [[§11 The Precise Definition of a Limit#^def-11-2|Definition §11.2]] to prove that $\displaystyle\lim_{x \to 0^+} \sqrt{x} = 0$.
>
> **1. Guessing $\delta$.** Let $\varepsilon > 0$. Here $a = 0$ and $L = 0$, so we want $\delta$ such that $0 < x < \delta$ implies $|\sqrt{x} - 0| < \varepsilon$, that is, $\sqrt{x} < \varepsilon$. Squaring (both sides are non-negative), this says $x < \varepsilon^2$. This suggests $\delta = \varepsilon^2$.
>
> **2. Showing that this $\delta$ works.** Given $\varepsilon > 0$, let $\delta = \varepsilon^2$. If $0 < x < \delta$, then, since the square root is increasing,
>
> $$
> \sqrt{x} < \sqrt{\delta} = \sqrt{\varepsilon^2} = \varepsilon , \qquad\text{so}\qquad |\sqrt{x} - 0| < \varepsilon .
> $$
>
> By [[§11 The Precise Definition of a Limit#^def-11-2|Definition §11.2]], $\lim_{x \to 0^+} \sqrt{x} = 0$. (Only a right-hand limit makes sense here: $\sqrt{x}$ is not defined for $x < 0$.)
>
> *Stewart: Example 2.4.4*

^ex-11-4

## The Limit Laws

As the examples show, proving limits directly from the definition takes some ingenuity, and for a function such as $f(x) = (6x^2 - 8x + 9)/(2x^2 - 1)$ it would take a great deal. This is unnecessary: the Limit Laws ([[§9 Calculating Limits Using the Limit Laws#^thm-9-1|Theorems §9.1]] and [[§9 Calculating Limits Using the Limit Laws#^thm-9-2|§9.2]]) are proved once from [[§11 The Precise Definition of a Limit#^def-11-1|Definition §11.1]], and then limits of complicated functions follow rigorously from the laws, without going back to the definition. Stewart proves the Sum Law here: if $\lim_{x \to a} f(x) = L$ and $\lim_{x \to a} g(x) = M$, then $\lim_{x \to a} [f(x) + g(x)] = L + M$, by making $|f(x) - L|$ and $|g(x) - M|$ each less than $\varepsilon/2$ and adding them with the Triangle Inequality. This is the proof of Law 1 given in [[§9 Calculating Limits Using the Limit Laws#^pf-9-1|the proof of Theorem §8.1]], together with the proofs of Laws 2–5 from Stewart's Appendix F.

## Infinite Limits

> [!definition] Definition §13.3: Precise Definition of an Infinite Limit
> Let $f$ be a function defined on some open interval that contains the number $a$, except possibly at $a$ itself. Then
>
> $$
> \lim_{x \to a} f(x) = \infty
> $$
>
> means that for every positive number $M$ there is a positive number $\delta$ such that
>
> $$
> \text{if} \quad 0 < |x - a| < \delta \quad \text{then} \quad f(x) > M .
> $$
>
> So the values of $f(x)$ can be made larger than any given number $M$ by requiring $x$ to be close enough to $a$ (within a distance $\delta$, which depends on $M$), with $x \ne a$. On the graph: for any horizontal line $y = M$ there is $\delta > 0$ such that over $(a - \delta, a + \delta)$, with $x = a$ left out, the curve lies above the line. A larger $M$ may require a smaller $\delta$. This makes [[§8 The Limit of a Function#^def-8-3|Definition §8.3]] precise.
>
> *Stewart: 2.4, Definition 6*

^def-11-3

> [!remark]- Connections
> - Rigorous treatment: the case $L = \pm\infty$ of [[§20 Limits of Functions#^rem-20-1|451 Remark: The epsilon-delta version]]; the sequence analogue is [[§9a Divergence to ±∞ and the Ratio Test#^def-9a-1|451 Def. §9a.1]] (for every $M$ there is $N$ with $s_n > M$ for $n > N$).

> [!example] Example §11.5: An Infinite Limit
> Use [[§11 The Precise Definition of a Limit#^def-11-3|Definition §11.3]] to prove that $\displaystyle\lim_{x \to 0} \frac{1}{x^2} = \infty$.
>
> Let $M > 0$ be given. We want $\delta$ such that $0 < |x| < \delta$ implies $1/x^2 > M$. For $x \ne 0$,
>
> $$
> \frac{1}{x^2} > M \iff x^2 < \frac{1}{M} \iff \sqrt{x^2} < \sqrt{\frac{1}{M}} \iff |x| < \frac{1}{\sqrt{M}} .
> $$
>
> So choose $\delta = 1/\sqrt{M}$. If $0 < |x| < \delta = 1/\sqrt{M}$, then by these equivalences $1/x^2 > M$. This shows that $1/x^2 \to \infty$ as $x \to 0$ (compare the table of [[§8 The Limit of a Function#^ex-8-4|Example §8.4]]: for $M = 10^6$ we get $\delta = 0.001$).
>
> *Stewart: Example 2.4.5*

^ex-11-5

> [!definition] Definition §13.4: Precise Definition of a Negative Infinite Limit
> Let $f$ be a function defined on some open interval that contains the number $a$, except possibly at $a$ itself. Then
>
> $$
> \lim_{x \to a} f(x) = -\infty
> $$
>
> means that for every negative number $N$ there is a positive number $\delta$ such that
>
> $$
> \text{if} \quad 0 < |x - a| < \delta \quad \text{then} \quad f(x) < N .
> $$
>
> This makes the first part of [[§8 The Limit of a Function#^def-8-4|Definition §8.4]] precise. The one-sided infinite limits are defined in the same way as in Definitions [[§11 The Precise Definition of a Limit#^def-11-3|§11.3]] and [[§11 The Precise Definition of a Limit#^def-11-4|§11.4]], with $0 < |x - a| < \delta$ replaced by $a - \delta < x < a$ (for $x \to a^-$) or $a < x < a + \delta$ (for $x \to a^+$), as in [[§11 The Precise Definition of a Limit#^def-11-2|Definition §11.2]].
>
> *Stewart: 2.4, Definition 7*

^def-11-4
