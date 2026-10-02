---
subject: "[[Single Variable Analysis]]"
section: 30
chapter: 5
tags: [real-analysis, math451]
---
← [[§29 The Mean Value Theorem]] · ↑ [[· 5 Differentiation]] · [[§31 Taylor's Theorem]] →

Now the most interesting section — with a good story about learning: paying for knowledge and fame (L'Hospital famously bought the result from Johann Bernoulli). We often meet limits of the type

$$
\lim_{x\to s} \frac{f(x)}{g(x)}, \qquad \text{where } f(x) \to 0,\ g(x) \to 0, \quad \text{or} \quad f(x) \to \infty,\ g(x) \to \infty
$$

— problematic, since no value can be given to $\tfrac00$ or $\tfrac\infty\infty$ (§5). Examples: $\lim_{x\to0}\tfrac{\sin x}{x}$ (type $\tfrac00$), $\lim_{x\to+\infty} \tfrac{x}{e^x}$ (type $\tfrac\infty\infty$).

> [!theorem] Theorem §30.1: L'Hospital's Rule
> Suppose $\lim_{x\to s} f(x) = 0 = \lim_{x\to s} g(x)$, *or* $\lim_{x\to s} |g(x)| = \infty$; suppose $f, g$ are differentiable (with $g'(x) \neq 0$) near $s$. If
>
> $$
> \lim_{x\to s} \frac{f'(x)}{g'(x)} = L,
> $$
>
> then
>
> $$
> \lim_{x\to s} \frac{f(x)}{g(x)} = L.
> $$
>
> Here $s$ can be a finite number or $\pm\infty$, the limits can be one-sided ($x \to s^+$ or $x \to s^-$), and $L$ may be finite or $\pm\infty$.

^thm-30-1

> [!remark]- Connections
> - Computational version: [[§28 Indeterminate Forms and L'Hospital's Rule#^thm-28-2|Calc Thm. §28.2]] (with worked examples).
> - Used in PDEs: the one-sided rule handles the difference quotients at $y=0$ in the proof of the Fourier convergence theorem, [[§12★ Proof of Convergence#^thm-12-4|341 Thm. §12.4]].

The idea: differentiating can *simplify* $f$ and $g$, letting us escape the indeterminate forms. We use the rule first, then prove it.

## Using the Rule

> [!example] Example §30.1: Four computations
> **(1)** $\displaystyle\lim_{x\to0} \frac{\sin x}{x} = \lim_{x\to0} \frac{\cos x}{1} = \frac11 = 1$ — after differentiating, the denominator is $1 \neq 0$ and $\cos$ is continuous: the difficulty has been avoided.
>
> **(2)** $\displaystyle\lim_{x\to+\infty} \frac{x}{e^x} = \lim_{x\to+\infty} \frac{1}{e^x} = 0$ (type $\tfrac\infty\infty$; this finally makes rigorous the growth comparison borrowed in §9).
>
> **(3)** $\displaystyle\lim_{x\to0} \frac{1 - \cos x}{x^2} = \lim_{x\to0} \frac{\sin x}{2x} = \lim_{x\to0} \frac{\cos x}{2} = \frac12$ — two applications in a row, each hypothesis re-checked (the intermediate quotient is again $\tfrac00$).
>
> **(4)** $\displaystyle\lim_{x\to0^+} x \log x$ — type $0 \cdot \infty$; convert to a standard form:
>
> $$
> \lim_{x\to0^+} x\log x = \lim_{x\to0^+} \frac{\log x}{\tfrac1x} = \lim_{x\to0^+} \frac{\tfrac1x}{-\tfrac1{x^2}} = \lim_{x\to0^+} (-x) = 0.
> $$
>
> *But beware*: rewriting instead as $\tfrac{x}{1/\log x}$ and differentiating makes the expression *more* complicated — the rule does not tell you *which* rewriting to choose. This is one thing to remember.

^ex-30-1

> [!example] Example §30.2: The form zero to the zero
> Compute $\lim_{x\to0^+} x^x$ — type $0^0$: since $a^0 = 1$ for $a > 0$ but $0^a = 0$, we don't know right away. The trick: exponentials convert products into the standard forms,
>
> $$
> x^x = e^{\log x^x} = e^{x \log x},
> $$
>
> reducing to example (4): $x\log x \to 0$, so by continuity of the exponential,
>
> $$
> \lim_{x\to0^+} x^x = e^0 = 1. \tag*{$\blacksquare$}
> $$

^ex-30-2

## Proving the Rule: the Generalized Mean Value Theorem

We prove a special case: $f(x) \to 0$, $g(x) \to 0$ as $x \to a^-$, with finite $a$ and finite $L$. (The $\tfrac\infty\infty$ case and $s = \pm\infty$ are similar in spirit; see the book.) The idea: for $x < x_1 < a$ with both close to $a$,

$$
\frac{f(x)}{g(x)} \approx \frac{f(x) - f(x_1)}{g(x) - g(x_1)},
$$

since $f(x_1), g(x_1)$ are very small — and the right side, by the following theorem, is an honest derivative quotient.

> [!theorem] Theorem §30.2: Generalized Mean Value Theorem
> Let $f, g: [a,b] \to \mathbb{R}$ be continuous and differentiable on $(a,b)$. Then there exists $x_0 \in (a,b)$ such that
>
> $$
> \bigl(f(b) - f(a)\bigr)\, g'(x_0) = \bigl(g(b) - g(a)\bigr)\, f'(x_0).
> $$
>
> In particular, when $g(b) - g(a) \neq 0$ (and $g'(x_0) \neq 0$),
>
> $$
> \frac{f(b) - f(a)}{g(b) - g(a)} = \frac{f'(x_0)}{g'(x_0)}.
> $$
>
> The symmetric formulation avoids any difficulty with $g(b) - g(a) = 0$; taking $g(x) = x$ recovers the ordinary [[Mean Value Theorem|MVT]].

^thm-30-2

![[m451-30-1.svg]]
*The Generalized MVT as the MVT for a curve: as $t$ runs over $[a,b]$, the point $(g(t), f(t))$ traces a curve (blue) whose chord (dashed) has slope $\tfrac{f(b)-f(a)}{g(b)-g(a)}$. At some $t = x_0$ the tangent, with direction $(g'(x_0), f'(x_0))$ and slope $\tfrac{f'(x_0)}{g'(x_0)}$, is parallel to the chord (red). With $g(t) = t$ this is the picture of the ordinary MVT in §29.*

> [!proof]+ Proof
> Following the pattern, define a new function whose critical point we seek:
>
> $$
> F(x) = \bigl(f(b) - f(a)\bigr) g(x) - \bigl(g(b) - g(a)\bigr) f(x).
> $$
>
> Compute the endpoint values — the cross terms survive:
>
> $$
> F(a) = f(b)g(a) - g(b)f(a), \qquad F(b) = f(b)g(a) - g(b)f(a) = F(a).
> $$
>
> By Rolle's theorem, there is $x_0 \in (a,b)$ with $F'(x_0) = 0$, which is exactly the claimed identity.

^pf-30-2

> [!remark]- Connections
> - Computational version: [[§28 Indeterminate Forms and L'Hospital's Rule#^thm-28-1|Calc Thm. §28.1]].

> [!proof]+ Proof
> Assume $f, g \to 0$ as $x \to a^-$, $g' \neq 0$ on some $(a - \delta_0, a)$, and $\tfrac{f'}{g'} \to L$ finite. First, two housekeeping points on $(a-\delta_0, a)$: for $x < x_1$ there, $g(x_1) \neq g(x)$ (otherwise Rolle would give a zero of $g'$ in between); and $g(x) \neq 0$ for $x$ close to $a$ (if $g$ vanished at points arbitrarily close to $a$, Rolle between two such zeros would again contradict $g' \neq 0$).
>
> Let $\varepsilon > 0$. Choose $\delta \leq \delta_0$ such that
>
> $$
> \left| \frac{f'(t)}{g'(t)} - L \right| < \varepsilon \qquad \text{for all } t \in (a - \delta,\, a).
> $$
>
> Fix any $x \in (a-\delta, a)$, and let $x_1 \in (x, a)$. By the Generalized MVT on $[x, x_1]$, there is $x_2 \in (x, x_1) \subset (a-\delta, a)$ with
>
> $$
> \frac{f(x) - f(x_1)}{g(x) - g(x_1)} = \frac{f'(x_2)}{g'(x_2)}, \qquad \text{hence} \qquad \left| \frac{f(x) - f(x_1)}{g(x) - g(x_1)} - L \right| < \varepsilon.
> $$
>
> Now let $x_1 \to a^-$ with $x$ held fixed: $f(x_1) \to 0$ and $g(x_1) \to 0$, so the quotient tends to $\tfrac{f(x)}{g(x)}$, and limits preserve the closed bound:
>
> $$
> \left| \frac{f(x)}{g(x)} - L \right| \leq \varepsilon \qquad \text{for every } x \in (a - \delta, a).
> $$
>
> Since $\varepsilon$ was arbitrary, $\lim_{x\to a^-} \tfrac{f(x)}{g(x)} = L$. (This $\varepsilon$-argument is the rigorous form of the approximation idea sketched above.)

^pf-30-1

## More Indeterminate Forms

> [!example] Example §30.3: One to the infinity
> Compute $\displaystyle\lim_{x\to\infty} \left( 1 - \frac2x \right)^x$ — type $1^\infty$, undetermined. Transform through the exponential:
>
> $$
> \left(1 - \frac2x\right)^x = e^{x \log\left(1 - \frac2x\right)},
> $$
>
> and the exponent, of type $\infty \cdot 0$, transforms again:
>
> $$
> x \log\left(1 - \frac2x\right) = \frac{\log\left(1 - \frac2x\right)}{\frac1x}
> \ \xrightarrow{\text{L'H}}\
> \frac{\left(1 - \frac2x\right)^{-1} \cdot \frac{2}{x^2}}{-\frac{1}{x^2}} = -\frac{2}{1 - \frac2x} \longrightarrow -2.
> $$
>
> By continuity of the exponential, the answer is $e^{-2}$.

^ex-30-3

> [!example] Example §30.4: Infinity minus infinity
> Compute $\displaystyle\lim_{x\to0} \left( \frac{1}{e^x - 1} - \frac{1}{x} \right)$ — type $\infty - \infty$. Combine over a common denominator to reach $\tfrac00$:
>
> $$
> \frac{1}{e^x-1} - \frac1x = \frac{x - e^x + 1}{x(e^x - 1)}
> \ \xrightarrow{\text{L'H}}\
> \frac{1 - e^x}{e^x - 1 + x e^x}
> \ \xrightarrow{\text{L'H}}\
> \frac{-e^x}{2e^x + x e^x} \longrightarrow \frac{-1}{2}.
> $$
>
> (Each application re-checked: both intermediate quotients are $\tfrac00$ at $x = 0$.) So the limit is $-\tfrac12$.

^ex-30-4

## Abstract Applications

Sometimes we deal with abstract functions rather than explicit formulas.

> [!example] Example §30.5: Recovering the limit of f from a combination
> Let $f: (c, \infty) \to \mathbb{R}$ be differentiable and suppose $\lim_{x\to\infty} \bigl(f(x) + f'(x)\bigr) = L$. Prove $\lim_{x\to\infty} f(x) = L$.
>
> *Proof.* Rewrite with an exponential weight:
>
> $$
> f(x) = \frac{f(x)e^x}{e^x}.
> $$
>
> The denominator $e^x \to \infty$, so L'Hospital's rule applies (note: the $|g| \to \infty$ case requires *nothing* of the numerator!). The quotient of derivatives is
>
> $$
> \frac{\bigl(f(x)e^x\bigr)'}{(e^x)'} = \frac{\bigl(f'(x) + f(x)\bigr)e^x}{e^x} = f'(x) + f(x) \longrightarrow L,
> $$
>
> hence $f(x) \to L$. Similarly, if $\lim_{x\to\infty}\bigl(2f(x) + f'(x)\bigr) = L$, write $f = \tfrac{f e^{2x}}{e^{2x}}$; the derivative quotient is $\tfrac{(f' + 2f)e^{2x}}{2e^{2x}} = \tfrac{f' + 2f}{2} \to \tfrac L2$, so $\lim f(x) = \tfrac L2$.

^ex-30-5

> [!example] Example §30.6: Another one-to-the-infinity
> $\displaystyle\lim_{x\to\infty}\left(1 - \frac1x\right)^x = e^{-1}$, by the same method as $\left(1-\tfrac2x\right)^x$ in the previous subsection (the exponent $x\log(1-\tfrac1x) \to -1$).

^ex-30-6
