---
subject: "[[Single Variable Analysis]]"
section: 8
chapter: 2
tags: [real-analysis, math451]
---
← [[Single Variable Analysis §7 Limits of Sequences]] · ↑ [[Single Variable Analysis — 2 Sequences]] · [[Single Variable Analysis §9 Limit Theorems for Sequences]] →

This section is a workshop on the two-step method: guess the limit, then prove it. The recurring technique: simplify $|s_n - s|$ by replacing it with a *simpler upper bound*, then solve $N$ in terms of $\varepsilon$ — the point being to get a simple, clean formula for $N$.

## Guessing and Proving

> [!example] Example §8.1: An indeterminate form of type $\infty - \infty$
> Let $s_n = \sqrt{n^2 + n + 1} - n$. Determine whether it converges; if yes, guess the limit and prove it.
>
> **Guessing.** The expression is of the type $\infty - \infty$; we need to get rid of the $\infty$'s. Multiply and divide by the conjugate:
>
> $$
> \begin{align*}
> \sqrt{n^2+n+1} - n
> &= \frac{(\sqrt{n^2+n+1} + n)(\sqrt{n^2+n+1} - n)}{\sqrt{n^2+n+1} + n}\\
> &= \frac{n^2 + n + 1 - n^2}{\sqrt{n^2+n+1} + n}
> = \frac{n+1}{\sqrt{n^2+n+1} + n}.
> \end{align*}
> $$
>
> Then what? *Look at the main term and ignore lower-order ones:*
>
> $$
> \approx \frac{n}{\sqrt{n^2} + n} = \frac{n}{n + n} = \frac12.
> $$
>
> So we guess $s_n \to \tfrac12$.
>
> **Proving.** We compute $|s_n - \tfrac12|$ and simplify, again via the conjugate (now of $\sqrt{n^2+n+1} - (n + \tfrac12)$):
>
> $$
> \left| s_n - \tfrac12 \right|
> = \left| \frac{n^2+n+1 - (n+\tfrac12)^2}{\sqrt{n^2+n+1} + n + \tfrac12} \right|
> = \frac{\tfrac34}{\sqrt{n^2+n+1} + n + \tfrac12}
> < \frac{\tfrac34}{n + n}
> < \frac1n.
> $$
>
> (In the second-to-last step we threw away a lot — using only $\sqrt{n^2+n+1} > n$ — but an upper bound is all we need.) Now $\tfrac1n < \varepsilon$ suffices: take $N > \tfrac1\varepsilon$.

^ex-8-1

> [!example] Example §8.2: Same method
> Let $s_n = \sqrt{9n^2 + n} - 3n$. By the conjugate trick,
>
> $$
> s_n = \frac{(\sqrt{9n^2+n} - 3n)(\sqrt{9n^2+n} + 3n)}{\sqrt{9n^2+n} + 3n}
> = \frac{9n^2 + n - 9n^2}{\sqrt{9n^2+n} + 3n}
> = \frac{n}{\sqrt{9n^2+n} + 3n}
> \approx \frac{n}{3n + 3n} = \frac16,
> $$
>
> so the limit should be $\tfrac16$. *Writing up the proof* (left as an exercise in lecture): from the display,
>
> $$
> \begin{align*}
> \left| s_n - \tfrac16 \right|
> = \left| \frac{n}{\sqrt{9n^2+n} + 3n} - \frac16 \right|
> &= \frac{\left| 6n - \sqrt{9n^2+n} - 3n \right|}{6\left(\sqrt{9n^2+n} + 3n\right)}\\
> &= \frac{\left| 3n - \sqrt{9n^2+n} \right|}{6\left(\sqrt{9n^2+n} + 3n\right)}
> = \frac{n}{6\left(\sqrt{9n^2+n} + 3n\right)^2},
> \end{align*}
> $$
>
> using the conjugate once more for $|3n - \sqrt{9n^2+n}| = \frac{n}{\sqrt{9n^2+n}+3n}$. Since $\sqrt{9n^2+n} + 3n > 6n$, the last quantity is $< \dfrac{n}{6 \cdot 36 n^2} < \dfrac1n$. So $N > \tfrac1\varepsilon$ works.

^ex-8-2

## Sequences Between $\mathbb{Q}$ and $\mathbb{R}$

> [!example] Example §8.3: Irrational terms with rational limit
> Give an example of a sequence of irrational numbers converging to a rational limit. Many choices — for instance
>
> $$
> s_n = 1 + \frac{\pi}{n} \longrightarrow 1.
> $$
>
> Each $s_n$ is irrational (if $1 + \pi/n$ were rational, so would be $\pi$), and $|s_n - 1| = \pi/n < \varepsilon$ once $n > \pi/\varepsilon$.

^ex-8-3

> [!example] Example §8.4: Rational terms with irrational limit
> Give an example of a sequence of rational numbers converging to an irrational limit — say $s = \tfrac{\pi}{4}$.
>
> Here we need an *algorithm*, not a formula for $s_n$. Note $\tfrac\pi4 \in [0,1]$. Divide $[0,1]$ into two equal intervals $[0, \tfrac12]$, $[\tfrac12, 1]$, and keep the one containing $\tfrac\pi4$. Dividing again and again into halves, we get a nested sequence of intervals containing $\tfrac\pi4$, the $n$-th of length $\tfrac{1}{2^n}$, with rational endpoints. Take $s_n$ to be the left endpoint of the $n$-th interval. Then $s_n \in \mathbb{Q}$ and
>
> $$
> \left| s_n - \frac\pi4 \right| \leq \frac{1}{2^n} \longrightarrow 0,
> $$
>
> so $s_n \to \tfrac\pi4$. (Are there other solutions? Certainly — e.g. truncated decimal expansions, once those are available.)

^ex-8-4

## Limits and Absolute Values; a Divergent Sequence

> [!example] Example §8.5: $s_n \to 0 \iff |s_n| \to 0$
> Prove: $\lim_{n\to\infty} s_n = 0$ if and only if $\lim_{n\to\infty} |s_n| = 0$.
>
> *Proof.* Compare the $(\varepsilon, N)$ conditions for the two statements. For the first: $|s_n - 0| = |s_n| < \varepsilon$. For the second: $\big| |s_n| - 0 \big| = \big| |s_n| \big| = |s_n| < \varepsilon$. The two conditions are *identical*, so for any $\varepsilon$, the same $N$ witnesses both.

^ex-8-5

> [!example] Example §8.6: $|s_n|$ converges but $s_n$ diverges
> Take $s_n = (-1)^n$. Then $|s_n| = 1$ clearly converges. But $(s_n)$ does not converge.
>
> *Proof.* Suppose it did, with $s = \lim_{n\to\infty} s_n$. Let $\varepsilon > 0$ be arbitrary; there exists $N$ such that $|s_n - s| < \varepsilon$ for all $n \geq N$. Choosing an *even* $n \geq N$ (e.g. $n = 2N$), where $s_n = 1$, gives $|1 - s| < \varepsilon$. Since $\varepsilon > 0$ was arbitrary, $|1 - s| = 0$, i.e. $s = 1$. Choosing an *odd* $n \geq N$ (e.g. $n = 2N+1$), where $s_n = -1$, gives $|-1 - s| = |1 + s| < \varepsilon$, and by the same argument $s = -1$. So $s = 1$ and $s = -1$ — impossible. Hence $(s_n)$ diverges. (The book has a different proof.)

^ex-8-6

## The Squeeze Theorem

> [!theorem] Theorem §8.1: Squeeze Theorem
> Given three sequences $(a_n), (b_n), (c_n)$ satisfying
>
> $$
> a_n \leq b_n \leq c_n \quad \text{for all } n,
> $$
>
> assume $\lim_{n\to\infty} a_n = \lim_{n\to\infty} c_n = s$. Then $(b_n)$ also converges to $s$.

^thm-8-1

> [!proof]+ Proof
> The idea: $|a_n - s| < \varepsilon$ if and only if $-\varepsilon < a_n - s < \varepsilon$, equivalently
>
> $$
> s - \varepsilon < a_n < s + \varepsilon,
> $$
>
> and the same unpacking applies to $c_n$ and $b_n$.
>
> Given $\varepsilon > 0$: since $a_n \to s$, there is $N_1$ with $s - \varepsilon < a_n < s + \varepsilon$ for $n \geq N_1$; since $c_n \to s$, there is $N_2$ with $s - \varepsilon < c_n < s + \varepsilon$ for $n \geq N_2$. Take $N = \max\{N_1, N_2\}$. For $n \geq N$, using the sandwich hypothesis,
>
> $$
> s - \varepsilon < a_n \leq b_n \leq c_n < s + \varepsilon,
> $$
>
> so $|b_n - s| < \varepsilon$. Hence $b_n \to s$.

^pf-8-1

> [!example] Example §8.7: Null sequence times bounded sequence
> First: if $s_n \to 0$, then for any number $M$, also $M s_n \to 0$. (By definition: given $\varepsilon > 0$, if $M = 0$ there is nothing to prove; otherwise choose $N$ with $|s_n| < \varepsilon / |M|$ for $n \geq N$; then $|M s_n| < \varepsilon$.)
>
> Now, by the [[Squeeze Theorem|Squeeze Theorem]] and this observation: *if $s_n \to 0$ and $(t_n)$ is a bounded sequence — i.e. there exists $M > 0$ such that $|t_n| \leq M$ for all $n$ — then $s_n t_n \to 0$.*
>
> *Proof.* Just note
>
> $$
> -|s_n| M \leq s_n t_n \leq |s_n| M,
> $$
>
> and the fact that $|s_n| \to 0$ too (previous subsection). Hence both outer sequences $-|s_n|M$ and $|s_n|M$ converge to $0$, and the middle sequence $s_n t_n$ converges to $0$ by squeezing.

^ex-8-7

## Two More Worked Examples

> [!example] Example §8.8: Square roots preserve limits
> Let $(s_n)$ be a sequence of nonnegative numbers with $s = \lim_{n\to\infty} s_n \geq 0$. Prove $\sqrt{s_n} \to \sqrt{s}$.
>
> What is known? That $|s_n - s|$ is small. So we must bound $|\sqrt{s_n} - \sqrt{s}|$ from above *in terms of* $|s_n - s|$, getting rid of the square roots — by the conjugate again:
>
> $$
> \left| \sqrt{s_n} - \sqrt{s} \right|
> = \left| \frac{(\sqrt{s_n} + \sqrt{s})(\sqrt{s_n} - \sqrt{s})}{\sqrt{s_n} + \sqrt{s}} \right|
> = \frac{|s_n - s|}{\sqrt{s_n} + \sqrt{s}}.
> $$
>
> It is good that $s_n - s$ appears in the numerator. How about the denominator?
>
> **Case $s > 0$.** Then $\sqrt{s_n} + \sqrt{s} \geq \sqrt{s}$, so
>
> $$
> \left| \sqrt{s_n} - \sqrt{s} \right| \leq \frac{|s_n - s|}{\sqrt{s}}.
> $$
>
> Write-up: given $\varepsilon > 0$, take $N$ such that $|s_n - s| < \sqrt{s}\, \varepsilon$ for $n \geq N$ (possible since $s_n \to s$). Then for $n \geq N$, $|\sqrt{s_n} - \sqrt{s}| < \varepsilon$.
>
> **Is this the end of the proof? No** — the bound divided by $\sqrt{s}$, so the case $s = 0$ needs separate treatment.
>
> **Case $s = 0$.** We want $|\sqrt{s_n}| < \varepsilon$, which is equivalent to $|s_n| < \varepsilon^2$. The latter is achievable since $s_n \to 0$: given $\varepsilon > 0$, apply the definition of $s_n \to 0$ with the tolerance $\varepsilon^2 > 0$ to get $N$ such that $|s_n| < \varepsilon^2$ for $n \geq N$; then $|\sqrt{s_n} - 0| < \varepsilon$ for $n \geq N$. So $\sqrt{s_n} \to 0$.

^ex-8-8

> [!example] Example §8.9: Eventually above $a$
> Assume $(s_n)$ is convergent with $\lim_{n\to\infty} s_n = s > a$. Prove there exists $N$ such that $s_n > a$ for all $n \geq N$.
>
> *Finding the proof.* For any $\varepsilon$, when $n$ is large, $|s_n - s| < \varepsilon$, i.e.
>
> $$
> s - \varepsilon < s_n < s + \varepsilon.
> $$
>
> We want $s - \varepsilon > a$, i.e. $\varepsilon < s - a$ — which is a legitimate choice since $s - a > 0$.
>
> *Write-up.* Set $\varepsilon = s - a > 0$. There exists $N$ such that $|s_n - s| < \varepsilon$ for $n \geq N$. Then for such $n$,
>
> $$
> s_n > s - \varepsilon = s - (s - a) = a. \tag*{$\blacksquare$}
> $$

^ex-8-9
