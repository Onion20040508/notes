---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 1
section: 8
powers: "1.3"
aliases: ["Powers 1.3"]
tags: [fourier-series-and-pdes, math341]
---
← [[§7 Arbitrary Period and Half-Range Expansions]] · ↑ [[· 1 Fourier Series and Integrals]] · [[§9 Uniform Convergence]] →

*Powers, Section 1.3 · MAT 341 lectures 9.3, 9.5 · HW 2 · Review Sheet 1.*

This section answers the second question of [[§6 Periodic Functions and Fourier Series|§6]]: does the Fourier series of $f$ actually represent $f$? For practical purposes this means: if a value of $x$ is chosen and the sum of the series is computed, is it $f(x)$? The answer is the convergence theorem. If $f$ is periodic and sectionally smooth (made of finitely many smooth pieces per period, with jumps and corners allowed but no blow-ups or vertical tangents), its Fourier series converges at every point, to $f(x)$ where $f$ is continuous and to the midpoint of the jump where it is not. To state this, the section first names the one-sided limits and the kinds of discontinuity. The theorem is stated here and proved in [[§12★ Proof of Convergence|§12★]] (Powers 1.7). It is what makes the series solutions of Chapters 2–4 meaningful at each point of a rod, string or plate, including at the points where an initial temperature or displacement jumps.

## One-Sided Limits and Discontinuities

The ordinary limit $\lim_{x \to x_0} f(x)$ can be rewritten as $\lim_{h \to 0} f(x_0 + h)$, where $h$ may approach zero in any manner.

> [!definition] Definition §8.1: One-Sided Limits
> If $h$ is required to be positive, we get the **right-hand limit** of $f$ at $x_0$,
>
> $$
> f(x_0+) = \lim_{h \to 0+} f(x_0 + h) = \lim_{\substack{h \to 0 \\ h > 0}} f(x_0 + h) ,
> $$
>
> and, with $h$ negative, the **left-hand limit**
>
> $$
> f(x_0-) = \lim_{h \to 0-} f(x_0 + h) = \lim_{\substack{h \to 0 \\ h < 0}} f(x_0 + h) = \lim_{h \to 0+} f(x_0 - h) .
> $$
>
> $f(x_0+)$ and $f(x_0-)$ need not be values of $f$. If both one-sided limits exist and are equal, the ordinary limit exists and equals them; conversely $\lim_{x \to x_0} f(x) = L$ if and only if $f(x_0-) = f(x_0+) = L$.
>
> *Powers: 1.3 (text); Source: 341 lecture 9.5*

^def-8-1

> [!remark]- Connections
> - [[§7 The Limit of a Function#^def-7-2|Calc Def. §7.2]] (one-sided limits); rigorously, [[§20 Limits of Functions#^def-20-2|451 Def. §20.2]], and the two-sided limit exists exactly when both one-sided limits exist and agree, [[§20 Limits of Functions#^thm-20-2|451 Thm. §20.2]].

It is quite possible that the one-sided limits exist but are different. This happens at $x = 0$ for $f(x) = 1$ on $0 < x < \pi$, $f(x) = -1$ on $-\pi < x < 0$: the left-hand limit is $-1$, the right-hand limit $+1$.

> [!definition] Definition §8.2: Kinds of Discontinuity
> At a point $x_0$, a function $f$ has
>
> | name | criterion |
> |---|---|
> | continuity | $f(x_0+) = f(x_0-) = f(x_0)$ |
> | removable discontinuity | $f(x_0+) = f(x_0-) \ne f(x_0)$ |
> | jump discontinuity | $f(x_0+) \ne f(x_0-)$ |
> | "bad" discontinuity | $f(x_0+)$ or $f(x_0-)$ or both fail to exist |
>
> A removable discontinuity also covers the case where $f$ is not defined at $x_0$ although both limits exist and agree; redefining $f(x_0)$ to be the limit makes $f$ continuous there. Removable discontinuities are so simple that we may assume they have been removed from any function under discussion. A one-sided limit fails to exist when $f$ tends to $\pm\infty$ or oscillates infinitely often.
>
> *Powers: 1.3, Table 2; Source: 341 lecture 9.5*

^def-8-2

> [!remark]- Connections
> - Stewart's removable, infinite and jump discontinuities: [[§10 Continuity#^def-10-3|Calc Def. §10.3]]. Powers' "bad" discontinuities include Stewart's infinite ones and also oscillation such as $\sin(1/x)$ at $0$, which fits none of Stewart's names ([[§20 Limits of Functions#^rem-20-3|451 Remark: Worse than a jump]]); removable and jump discontinuities in 451: [[§20 Limits of Functions#^ex-20-4|451 Ex. §20.4]], [[§20 Limits of Functions#^ex-20-5|451 Ex. §20.5]].

> [!example] Example §8.1: Classifying Discontinuities
> **(a)** $f(x) = (x - x^2)/(1 - x)$ equals $x$ for $x \ne 1$ and is undefined at $1$: $f(1-) = f(1+) = 1$, a removable discontinuity. Likewise $\sin(x)/x$ has a removable discontinuity at $x = 0$, removed by setting $f(0) = 1$.
>
> **(b)** $f(x) = x$ for $0 < x < 1$ and $f(x) = x - 1$ for $1 < x$ (or $1 < x < 2$): $f(1-) = 1$, $f(1+) = 0$, a jump discontinuity; $\lim_{x \to 1} f(x)$ does not exist.
>
> **(c)** $f(x) = -\ln(|1 - x|)$: $f(x) \to +\infty$ as $x \to 1$ from either side, a bad discontinuity. So are $\tan x$ at $\pi/2$ (with $f(x) = 1$ for $x > \pi/2$, $f(\pi/2+) = 1$ but $f(\pi/2-) = \infty$ does not exist), and $\sin(1/x)$, $e^{1/x}$, $1/x$ at $x = 0$: $\sin(1/x)$ oscillates between $\pm1$ infinitely often, $e^{1/x} \to \infty$ as $x \to 0+$, and $1/x \to \pm\infty$.
>
> *Powers: 1.3 (text), Figure 7; Source: 341 lecture 9.5, Examples 1–3*

^ex-8-1

## Sectionally Continuous and Sectionally Smooth Functions

> [!definition] Definition §8.3: Sectionally Continuous Function
> A function $f$ is **sectionally continuous** (also called **piecewise continuous**) on an interval $a < x < b$ if it is bounded and continuous there, except possibly for a finite number of jumps and removable discontinuities. A function is sectionally continuous (without qualification) if it is sectionally continuous on every interval of finite length. For instance, a periodic function that is sectionally continuous on an interval of length one period or more is sectionally continuous.
>
> A sectionally continuous function must not "blow up" at any point, even an endpoint of an interval: "no bad discontinuity" forces it to be bounded on finite intervals. It need not be defined at every point.
>
> *Powers: 1.3 (text), Figure 8; Source: 341 lecture 9.5*

^def-8-3

> [!definition] Definition §8.4: Sectionally Smooth Function
> A function $f$ is **sectionally smooth** (also **piecewise smooth**; the lecture says *piecewise continuously differentiable*) on an interval $a < x < b$ if
> 1. $f$ is sectionally continuous;
> 2. $f'(x)$ exists, except perhaps at a finite number of points; and
> 3. $f'(x)$ is sectionally continuous.
>
> The graph of a sectionally smooth function has a finite number of removable discontinuities, jumps and corners, where the derivative does not exist. Between these points the graph is continuous with a continuous derivative. No vertical tangents are allowed, since they indicate that the derivative is infinite.
>
> *Powers: 1.3 (text); Source: 341 lecture 9.5*

^def-8-4

> [!example] Example §8.2: Sectionally Continuous or Smooth, or Not
> **(a)** The **square wave** $f(x) = 1$ for $0 < x < a$, $f(x) = -1$ for $-a < x < 0$, $f(x + 2a) = f(x)$, is sectionally continuous, with jumps at $x = 0, \pm a, \pm2a, \ldots$. No value was given at these points, and the function remains sectionally continuous whatever values are assigned. It is also sectionally smooth ($f' = 0$ except at the jumps), but not continuous.
>
> **(b)** $f(x) = 1/x$ cannot be sectionally continuous on any interval that contains $0$, or even has $0$ as an endpoint, because it is not bounded near $x = 0$.
>
> **(c)** $f(x) = x$, $-1 < x < 1$, is continuous on that interval. Its periodic extension ([[§7 Arbitrary Period and Half-Range Expansions#^ex-7-3|Example §7.3]]) is sectionally continuous, and sectionally smooth, but not continuous: it jumps at $x = \pm1, \pm3, \ldots$
>
> **(d)** $f(x) = |x|^{1/2}$ is continuous but not sectionally smooth on any interval containing $0$: $|f'(x)| = \frac12|x|^{-1/2} \to \infty$ as $x \to 0$, a vertical tangent.
>
> *Powers: 1.3, Examples 1–3 (sectionally continuous) and Examples 1–2 (sectionally smooth)*

^ex-8-2

## The Convergence Theorem

Most functions useful in mathematical modeling are sectionally smooth. Fortunately, there is a positive statement about the Fourier series of such functions.

> [!theorem] Theorem §8.1: Convergence of Fourier Series
> If $f$ is sectionally smooth and periodic with period $2a$, then at each point $x$ the Fourier series corresponding to $f$ converges, and its sum is
>
> $$
> a_0 + \sum_{n=1}^{\infty} a_n\cos\Big(\frac{n\pi x}{a}\Big) + b_n\sin\Big(\frac{n\pi x}{a}\Big) = \frac{f(x+) + f(x-)}{2} .
> $$
>
> In particular the sum is $f(x)$ at every point where $f$ is continuous.
>
> *Powers: 1.3, Theorem*

^thm-8-1

*Powers states the theorem here without proof and proves it in Section 1.7: [[§12★ Proof of Convergence#^thm-12-4|Theorem §12.4]] (period $2\pi$), extended to period $2a$ in [[§12★ Proof of Convergence#^cor-12-5|Corollary §12.5]]. The rigorous subjects of the vault treat Fourier series only in the mean (see Connections), so §12★ is the home of this proof.*

> [!remark]- Connections
> - In Functional Analysis the trigonometric functions form an orthonormal basis of $L^2$, [[§20 Orthonormal Sets and Bases#^thm-20-11|556 Thm. §20.11]], so every square-integrable $f$ is the sum of its Fourier series in the $L^2$ norm, "not necessarily pointwise" ([[§20 Orthonormal Sets and Bases#^rem-20-9|556 Remark: Fourier Series]]); Lay's version for continuous $f$ is [[§47 Applications of Inner Product Spaces#^thm-47-4|235 Thm. §47.4]]. Theorem §8.1 is the pointwise statement, at the price of the smoothness hypothesis; convergence in the mean is [[§11★ Mean Error and Convergence in Mean#^thm-11-6|Theorem §11.6]].

This theorem answers the question at the beginning of the section. A sectionally smooth function has only finitely many jumps and no bad discontinuities in every finite interval. Hence

$$
f(x-) = f(x+) = \tfrac12\big(f(x+) + f(x-)\big) = f(x) ,
$$

except perhaps at a finite number of points in any finite interval (once removable discontinuities are removed). For this reason, if $f$ satisfies the hypotheses of the theorem, we write $f$ *equal* to its Fourier series, even though the equality may fail at the jumps.

> [!remark] Remark: Values at Jumps and at the Endpoints
> In constructing the periodic extension of a function given on $-a < x < a$, the values at the endpoints were never defined. Since the Fourier coefficients are integrals, the value of $f$ at one point cannot influence them: in that sense the value at $x = \pm a$ is unimportant. But because of the averaging feature of the Fourier series it is reasonable to define
>
> $$
> f(a) = f(-a) = \tfrac12\big(f(a-) + f(-a+)\big) ,
> $$
>
> the average of the one-sided limits at the two endpoints, each taken from the interior. For instance, if $f(x) = 1 + x$ for $0 < x < 1$ and $f(x) = 0$ for $-1 < x < 0$, then $f(\pm1)$ should be taken to be $\frac12(2 + 0) = 1$, and $f(0)$ should be $\frac12(0 + 1) = \frac12$. With these values $f$ equals its Fourier series everywhere.

^rem-8-1

> [!remark] Remark: Method — The Sum of a Fourier Series at a Point
> To find the value of the Fourier series of $f$ at a point $x_0$:
> 1. Check that $f$ (or its periodic extension) is sectionally smooth: finitely many pieces per period, no blow-up, no vertical tangent.
> 2. Sketch the periodic extension $\bar f$ (odd or even periodic extension for a sine or cosine series) and locate $x_0$; reduce $x_0$ by multiples of the period if convenient.
> 3. If $\bar f$ is continuous at $x_0$, the sum is $\bar f(x_0)$. If it jumps, the sum is $\frac12(\bar f(x_0+) + \bar f(x_0-))$. At an endpoint $\pm a$ of the original interval, the two one-sided limits come from the two *ends* of the interval: $\bar f(a-) = f(a-)$ and $\bar f(a+) = f(-a+)$.
> 4. The value assigned to $f$ at $x_0$ itself plays no role.

^rem-8-2

> [!remark] Remark: The Hypotheses Are Sufficient, Not Necessary
> For $f(x) = |x|^{1/2}$, $-\pi < x < \pi$, $f(x + 2\pi) = f(x)$, the theorem does not guarantee convergence of the Fourier series at any point, even though the function is continuous (it is not sectionally smooth, [[§8 Convergence of Fourier Series#^ex-8-2|Example §8.2]](d)). Nevertheless the series does converge at every point $x$. This shows that the conditions in the theorem are perhaps too strong; but they are useful, because they are easy to check.

^rem-8-3

## Examples

> [!example] Example §8.3: The Sawtooth and the Square Wave
> **(a) Sawtooth.** Let $f(x) = x$ on $-\pi < x < \pi$, periodic with period $2\pi$, with Fourier series $\sum_{n=1}^{\infty}\frac{2(-1)^{n + 1}}{n}\sin nx$ ([[§6 Periodic Functions and Fourier Series#^ex-6-1|Example §6.1]]). Evaluate the series at $x = 1$ and $x = \pi$. $f$ is sectionally smooth on $\mathbb{R}$. At $x = 1$ it is continuous, so the series converges to $\frac12(f(1-) + f(1+)) = 1$. At $x = \pi$ it jumps: $f(\pi-) = \pi$ and $f(\pi+) = f(-\pi+) = -\pi$, so the series converges to $\frac12(\pi - \pi) = 0$, as it must, since every term $\sin n\pi$ is $0$.
>
> **(b) Square wave of period 2.** The function $f(x) = 1$ for $0 < x < 1$, $-1$ for $-1 < x < 0$ is sectionally smooth; therefore its Fourier series converges to $1$ for $0 < x < 1$, to $-1$ for $-1 < x < 0$, and to $0$ for $x = 0, 1, -1$, and the sum is periodic with period $2$.
>
> **(c) Square wave of period 4.** Let $f$ be periodic with period $4$, $f(x) = 1$ for $0 < x < 2$ and $-1$ for $-2 < x < 0$. Sketch $f$ on $(-6, 6)$, find its Fourier series, and give the values of the series at $x = -0.2$, $0$, $2$.
>
> The graph alternates between the levels $1$ (on $(0, 2)$, $(4, 6)$, $(-4, -2)$) and $-1$ (on $(-2, 0)$, $(2, 4)$, $(-6, -4)$), with jumps at the even integers. $f$ is odd, so $a_0 = a_n = 0$, and with $a = 2$,
>
> $$
> b_n = \frac22\int_0^2\sin\frac{n\pi x}{2}\,dx = \Big[-\frac{2}{n\pi}\cos\frac{n\pi x}{2}\Big]_0^2 = \frac{2}{n\pi}\big[1 - (-1)^n\big], \qquad f(x) \sim \sum_{n=1}^{\infty}\frac{2}{n\pi}\big[1 - (-1)^n\big]\sin\frac{n\pi x}{2} ,
> $$
>
> that is, $\frac4\pi\big(\sin\frac{\pi x}{2} + \frac13\sin\frac{3\pi x}{2} + \cdots\big)$. Since $f$ is sectionally smooth, the series converges to $1$ on $(0, 2)$, to $-1$ on $(-2, 0)$, and to $0$ at the jumps $x = 0, \pm2$ (periodically). So the values are $-1$ at $x = -0.2$, $\frac12(1 + (-1)) = 0$ at $x = 0$, and $\frac12(f(2-) + f(2+)) = \frac12(1 - 1) = 0$ at $x = 2$.
>
> *Powers: 1.3, Example 1 (convergence); Source: 341 lecture 9.5, Example 1; 341 HW 2, Problem 2*

^ex-8-3

> [!example] Example §8.4: A Function with a Jump at the Ends of the Period
> A function is given on $-\pi < x < \pi$ by
>
> $$
> f(x) = \begin{cases} 2x, & 0 \le x < \pi, \\ -x, & -\pi < x < 0 . \end{cases}
> $$
>
> **(a)** Sketch the periodic extension $\bar f$ on $-3\pi < x < 3\pi$. **(b)** Give the types of the discontinuities of $\bar f$ on one period. **(c)** Find the Fourier series. **(d)** Find the value of the series at $x = -\pi$, $0$, $\pi$.
>
> **(a)** On each period the graph falls along $y = -x$ from $(-\pi, \pi)$ to $(0, 0)$ and then rises along $y = 2x$ to $(\pi, 2\pi)$; at $x = \pi$ it drops back to $\pi$ and repeats.
>
> **(b)** At $x = 0$: $\bar f(0-) = 0 = \bar f(0+) = f(0)$, so $\bar f$ is continuous. At $x = \pm\pi$ (and every odd multiple of $\pi$): $\bar f(\pi-) = 2\pi$ and $\bar f(\pi+) = f(-\pi+) = \pi$, a jump discontinuity, since the one-sided limits exist and differ. There are no other discontinuities.
>
> **(c)** Write $f(x) = \frac{x}{2} + \frac{3|x|}{2}$ on $(-\pi, \pi)$ (check: $\frac x2 + \frac{3x}{2} = 2x$ for $x > 0$, $\frac x2 - \frac{3x}{2} = -x$ for $x < 0$), the odd plus the even part ([[§7 Arbitrary Period and Half-Range Expansions#^prop-7-2|Proposition §7.2]]). By [[§7 Arbitrary Period and Half-Range Expansions#^thm-7-4|Theorem §7.4]], the odd part contributes only sines and the even part only cosines:
>
> $$
> a_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi}\frac{3|x|}{2}\,dx = \frac{3}{2\pi}\int_0^{\pi} x\,dx = \frac{3\pi}{4}, \qquad
> a_n = \frac{2}{\pi}\int_0^{\pi}\frac{3x}{2}\cos nx\,dx = \frac3\pi\cdot\frac{(-1)^n - 1}{n^2} = \frac{3}{n^2\pi}\big[(-1)^n - 1\big],
> $$
>
> $$
> b_n = \frac2\pi\int_0^{\pi}\frac x2\sin nx\,dx = \frac1\pi\cdot\frac{\pi(-1)^{n + 1}}{n} = \frac{(-1)^{n + 1}}{n} ,
> $$
>
> using $\int_0^\pi x\cos nx\,dx = \frac{(-1)^n - 1}{n^2}$ and $\int_0^\pi x\sin nx\,dx = \frac{\pi(-1)^{n + 1}}{n}$. (Integrating $2x$ and $-x$ separately over $(0, \pi)$ and $(-\pi, 0)$ gives the same numbers.) So
>
> $$
> \bar f(x) \sim \frac{3\pi}{4} + \sum_{n=1}^{\infty}\Big(\frac{3[(-1)^n - 1]}{n^2\pi}\cos nx + \frac{(-1)^{n + 1}}{n}\sin nx\Big) .
> $$
>
> **(d)** $\bar f$ is sectionally smooth. At $x = 0$ it is continuous and the series converges to $0$. At $x = \pm\pi$ it converges to $\frac12(2\pi + \pi) = \frac{3\pi}{2}$.
>
> *Source: 341 Review Sheet 1, Problem 4*

^ex-8-4

![[m341-8-1.svg]]
*Example §8.4: the periodic extension $\bar f$ (black) and the partial sum $S_{20}$ of its Fourier series (blue). At the continuity point $x = 0$ the partial sums approach $0$; at the jumps $x = \pm\pi, \pm3\pi$ every partial sum passes through the midpoint $3\pi/2$ (red dots), the value given by Theorem §8.1.*

> [!example] Example §8.5: The Function sin(x)/x
> Consider $f(x) = \frac{\sin x}{x}$ for $x \in (-\pi, 0) \cup (0, \pi)$, extended with period $2\pi$. **(a)** Is $f$ continuous on $(-\pi, \pi)$? **(b)** To what value does the Fourier series converge at $x = 0$, $\pi/2$, $\pi$? **(c)** Compute $f'(0)$ and decide whether $f'$ is continuous on $(-\pi, \pi)$.
>
> **(a)** $\sin x$ and $x$ are continuous and $x \ne 0$ away from $0$, so $f$ is continuous on $(-\pi, 0) \cup (0, \pi)$. At $0$, $f(0-) = f(0+) = \lim_{x \to 0}\frac{\sin x}{x} = 1$. With the value $f(0) = 1$, $f$ is continuous on $(-\pi, \pi)$.
>
> **(b)** $f$ is sectionally smooth (by (c), $f'$ is continuous on $(-\pi, \pi)$ with one-sided limits $\mp\frac1\pi$ at $\pm\pi$), so Theorem §8.1 applies. At $x = 0$ the series converges to $\frac12(1 + 1) = 1$; at $x = \frac\pi2$ to $f(\frac\pi2) = \frac{\sin(\pi/2)}{\pi/2} = \frac2\pi$; at $x = \pi$ to $\frac12(f(\pi-) + f(-\pi+)) = \frac12(0 + 0) = 0$, since $\sin(\pm\pi) = 0$.
>
> **(c)** With $f(0) = 1$, by the definition of the derivative and $\sin h = h - \frac{h^3}{6} + \cdots$,
>
> $$
> f'(0) = \lim_{h \to 0}\frac{f(h) - f(0)}{h} = \lim_{h \to 0}\frac{\frac{\sin h}{h} - 1}{h} = \lim_{h \to 0}\frac{\sin h - h}{h^2} = \lim_{h \to 0}\Big(-\frac h6 + \cdots\Big) = 0 .
> $$
>
> For $x \ne 0$, $f'(x) = \frac{\cos x}{x} - \frac{\sin x}{x^2} = \frac{x\cos x - \sin x}{x^2}$, and $x\cos x - \sin x = x - \frac{x^3}{2} - x + \frac{x^3}{6} + \cdots = -\frac{x^3}{3} + \cdots$, so $f'(x) \to 0 = f'(0)$ as $x \to 0$: $f'$ is continuous on $(-\pi, \pi)$. Uniform convergence of the series is decided in [[§9 Uniform Convergence#^ex-9-3|Example §9.3]].
>
> *The problem sheet defines $f(0) = 0$; the key reads it as $f(0) = 1$, the value that removes the discontinuity. With $f(0) = 0$ as printed, $f$ has a removable discontinuity at $0$ and $f'(0)$ does not exist; the Fourier series, which does not see the value at one point, and its values in (b) are the same in both readings.*
>
> *Powers: Exercise 1.4.2; Source: 341 HW 2, Problem 3(a)–(c)*

^ex-8-5
