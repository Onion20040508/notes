---
subject: "[[Single Variable Analysis]]"
section: 20
chapter: 3
tags: [real-analysis, math451]
---
← [[Single Variable Analysis §19 Uniform Continuity]] · ↑ [[Single Variable Analysis — 3 Continuity]] · [[Single Variable Analysis §21 More on Metric Spaces꞉ Continuity]] →

Recall: $f$ is continuous at $x_0$ if $x_n \to x_0$ implies $f(x_n) \to f(x_0)$. What we *really* want to say is: as $x \to x_0$, $f(x) \to f(x_0)$ — with the continuous variable $x$, not just discrete sequences. This jump from discrete to continuous is an important interplay in mathematics and science; we now formalize it.

> [!definition] Definition §20.1: Limit of a Function Along a Set
> Let $S \subseteq \mathbb{R}$, let $a \in [-\infty, +\infty]$ be the limit of some sequence in $S$ (in the terminology of §13: $a$ lies in the closure of $S$, allowing $\pm\infty$), and let $L \in [-\infty, +\infty]$. Given $f: S \to \mathbb{R}$, we say **$f(x) \to L$ as $x \to a$ through $S$**, written
>
> $$
> \lim_{x \to a^S} f(x) = L,
> $$
>
> if for every sequence $x_n \in S$ with $x_n \to a$, we have $f(x_n) \to L$. The set $S$ controls where the sequence can take its values. Note that $f$ need not be defined at $a$ — we are *not* comparing $f(x)$ with any value $f(a)$.

^def-20-1

> [!remark] Remark: The epsilon-delta version
> For finite $a$ and $L$, equivalently: for every $\varepsilon > 0$ there exists $\delta > 0$ such that for every $x \in S$ with $|x - a| < \delta$ (and, when $a \notin S$ is intended, $x \neq a$ automatically since $f$ is only defined on $S$),
>
> $$
> |f(x) - L| < \varepsilon.
> $$
>
> (The equivalence is proved exactly as in §17.) If $a = +\infty$, modify: for every $\varepsilon > 0$ there exists $M > 0$ such that $x > M$ implies $|f(x) - L| < \varepsilon$; similarly for $a = -\infty$, and for $L = \pm\infty$ (replace the conclusion by $f(x) > M'$, etc.).

^rem-20-1

> [!example] Example §20.1: First computations
> $S = (0,1)$, $f(x) = \tfrac1x$: then $\lim_{x\to 0^S} f(x) = +\infty$ and $\lim_{x \to 1^S} f(x) = 1$.

^ex-20-1

> [!theorem] Theorem §20.1: Continuity in Terms of Limits
> If $a \in S$, then $f$ is continuous at $a$ if and only if $\lim_{x\to a^S} f(x)$ exists and
>
> $$
> \lim_{x \to a^S} f(x) = f(a).
> $$

^thm-20-1

> [!proof]+ Proof
> Immediate from the sequential definitions of both sides. This is consistent with the intuition: continuity at $a$ means the values of $f(x)$ approach $f(a)$ as $x \to a$.

^pf-20-1

## Notation: Two-Sided and One-Sided Limits

The notation $\lim_{x\to a^S}$ is a bit inconvenient; in common situations we simplify it:

> [!definition] Definition §20.2: Standard Limit Notations
> - If $S = (c,d) \setminus \{a\}$ with $a \in (c,d)$ (a punctured interval), write $\displaystyle\lim_{x\to a} f(x) = L$ — the **two-sided limit**; $S$ is dropped.
>
> - If $S = (a, b)$ (points to the right of $a$), write $\displaystyle\lim_{x\to a^+} f(x) = L$: the **right-hand limit** — $x > a$ approaching $a$.
>
> - If $S = (c, a)$, write $\displaystyle\lim_{x\to a^-} f(x) = L$: the **left-hand limit**.
>
> - If $S = (c, +\infty)$, write $\displaystyle\lim_{x\to+\infty} f(x) = L$; similarly $\displaystyle\lim_{x\to-\infty} f(x) = L$ for $S = (-\infty, c)$.

^def-20-2

Why do we need one-sided limits?

> [!example] Example §20.2: A step function
> Let $f(x) = 1$ for $x > 0$ and $f(x) = 0$ for $x \leq 0$. Is $f$ continuous? No — not at $0$: the sequence $\tfrac1n \to 0$ has $f(\tfrac1n) = 1 \not\to 0 = f(0)$. Here
>
> $$
> \lim_{x\to 0^-} f(x) = 0, \qquad \lim_{x\to 0^+} f(x) = 1, \qquad \lim_{x\to 0} f(x) \ \text{does not exist}
> $$
>
> — we only have the partial limits, from the left and from the right.

^ex-20-2

> [!example] Example §20.3: The reciprocal at its four ends
> For $f(x) = \tfrac1x$ on $S = \mathbb{R}\setminus\{0\}$:
>
> $$
> \lim_{x\to+\infty} \frac1x = 0, \qquad \lim_{x\to-\infty} \frac1x = 0, \qquad \lim_{x\to 0^+} \frac1x = +\infty, \qquad \lim_{x\to 0^-} \frac1x = -\infty.
> $$
>
> In particular $\lim_{x\to 0} \tfrac1x$ does not exist (not even in $[-\infty,+\infty]$: the one-sided limits differ).

^ex-20-3

> [!theorem] Theorem §20.2: Two-Sided Equals Both One-Sided
> $\displaystyle\lim_{x\to a} f(x) = L$ if and only if
>
> $$
> \lim_{x\to a^+} f(x) = L \quad \text{and} \quad \lim_{x\to a^-} f(x) = L.
> $$

^thm-20-2

> [!proof]+ Proof
> ($\Rightarrow$) Clear: a sequence approaching $a$ from within $(a,d)$ (or $(c,a)$) is in particular a sequence in the punctured interval, so the one-sided limits exist and equal $L$.
>
> ($\Leftarrow$) Use the $(\varepsilon,\delta)$ formulations. Given $\varepsilon > 0$: from the right-hand limit, there is $\delta_+ > 0$ such that $x > a$, $|x - a| < \delta_+$ imply $|f(x) - L| < \varepsilon$; from the left-hand limit, there is $\delta_- > 0$ such that $x < a$, $|x-a| < \delta_-$ imply $|f(x) - L| < \varepsilon$. Take
>
> $$
> \delta = \min\{\delta_+, \delta_-\}:
> $$
>
> for every $x$ in the punctured interval with $|x - a| < \delta$, whichever side $x$ is on, $|f(x) - L| < \varepsilon$.

^pf-20-2

> [!remark] Remark
> The usual limit theorems (sums, products, quotients) hold for these limits — including the one-sided versions — by the corresponding theorems for sequences; likewise a composition theorem, where one should be careful about matching sides and domains.

^rem-20-2

## Filling Removable Holes

These notions can be used to *produce* continuous functions: extend a function to a missing point by its limit there — when the limit exists.

> [!example] Example §20.4: A removable singularity
> Let $S = \mathbb{R}\setminus\{0\}$ and $f(x) = \dfrac{\sqrt{1+2x^2} - 1}{x^2}$. Can we define $f(0)$ so that $f$ becomes continuous on $\mathbb{R}$? Compute the limit at $0$ by the conjugate:
>
> $$
> \frac{\sqrt{1+2x^2}-1}{x^2}
> = \frac{(1 + 2x^2) - 1}{x^2\left(\sqrt{1+2x^2}+1\right)}
> = \frac{2x^2}{x^2\left(\sqrt{1+2x^2}+1\right)}
> = \frac{2}{\sqrt{1+2x^2}+1} \longrightarrow \frac{2}{1+1} = 1.
> $$
>
> So $\lim_{x\to0} f(x) = 1$; defining $f(0) = 1$ yields a continuous function on $\mathbb{R}$.

^ex-20-4

> [!example] Example §20.5: A jump that cannot be removed
> Now $g(x) = \dfrac{\sqrt{1 + 2|x|} - 1}{x}$ on $\mathbb{R}\setminus\{0\}$ — a bit different. The same conjugate computation gives
>
> $$
> g(x) = \frac{2|x|}{x\left(\sqrt{1+2|x|}+1\right)},
> $$
>
> and $\tfrac{|x|}{x} = \pm1$ depending on the side:
>
> $$
> \lim_{x\to 0^+} g(x) = \frac{2}{1+1} = 1, \qquad \lim_{x\to0^-} g(x) = -1.
> $$
>
> The one-sided limits differ, so $\lim_{x\to0} g(x)$ does not exist, and *no* value $g(0)$ makes $g$ continuous.

^ex-20-5

![[m451-20-1.svg]]
*Removable versus non-removable. Left: $f$ is undefined at $0$, but both sides approach the same height, so the hole (hollow) is filled by $f(0) = \lim_{x\to0} f(x) = 1$. Right: $g$ approaches $1$ from the right and $-1$ from the left (both hollow); a single value $g(0)$ cannot sit at both ends of the jump.*

> [!remark] Remark: Worse than a jump
> For $f(x) = \sin\tfrac1x$, $x \neq 0$: not only does $\lim_{x\to0} f(x)$ not exist — the left and right limits do not exist either (the oscillation argument of §17 works from each side). This is much worse than the previous example: the existence of one-sided limits is already a good property of a function.

^rem-20-3
