---
type: section
subject: "[[Calculus]]"
chapter: 4
section: 30
stewart: "4.3"
aliases: ["Stewart 4.3"]
tags: [calculus]
---
← [[§29 Rolle's Theorem and the Mean Value Theorem]] · ↑ [[· 4 Applications of Differentiation]] · [[§31 Indeterminate Forms and L'Hospital's Rule]] →

*Stewart, Section 4.3.*

Since $f'(x)$ is the slope of the curve $y = f(x)$ at $(x, f(x))$, the sign of $f'$ tells where the curve rises and falls, and the sign of $f''$ tells which way it bends. This section turns those observations into tests, each proved from the Mean Value Theorem ([[§29 Rolle's Theorem and the Mean Value Theorem#^thm-29-2|Theorem §29.2]]). The Increasing/Decreasing Test reads monotonicity off the sign of $f'$. The First Derivative Test decides whether a critical number gives a local maximum, a local minimum or neither. The Concavity Test reads concavity off the sign of $f''$, and the Second Derivative Test is an alternative way to classify critical numbers. Together they are the tools for sketching a curve from its formula ([[§32 Summary of Curve Sketching|§32]]).

## What Does f′ Say About f?

> [!theorem] Theorem §30.1: The Increasing/Decreasing Test
> (a) If $f'(x) > 0$ on an interval, then $f$ is increasing on that interval.
>
> (b) If $f'(x) < 0$ on an interval, then $f$ is decreasing on that interval.
>
> Stewart abbreviates the name to the **I/D Test**. ("Increasing" means $x_1 < x_2 \Rightarrow f(x_1) < f(x_2)$, as defined in [[§1 Four Ways to Represent a Function#^def-1-8|Def. §1.8]].)
>
> *Stewart: 4.3, Increasing/Decreasing Test*

^thm-30-1

> [!proof]+ Proof
> (a) Let $x_1$ and $x_2$ be any two numbers in the interval with $x_1 < x_2$. We must show that $f(x_1) < f(x_2)$. Since $f'(x) > 0$ on the interval, $f$ is differentiable on $[x_1, x_2]$, hence continuous there. By the Mean Value Theorem there is a number $c$ between $x_1$ and $x_2$ such that
>
> $$
> f(x_2) - f(x_1) = f'(c)(x_2 - x_1) . \qquad (1)
> $$
>
> Now $f'(c) > 0$ by assumption and $x_2 - x_1 > 0$ because $x_1 < x_2$, so the right side of (1) is positive: $f(x_2) - f(x_1) > 0$, that is, $f(x_1) < f(x_2)$. So $f$ is increasing.
>
> (b) (Stewart: "proved similarly.") Now $f'(c) < 0$, so the right side of (1) is negative and $f(x_1) > f(x_2)$: $f$ is decreasing.

^pf-30-1

*Uses:* [[§29 Rolle's Theorem and the Mean Value Theorem#^thm-29-2|§29.2]], [[§15 The Derivative as a Function#^thm-15-1|§15.1]] (differentiable implies continuous)

> [!remark]- Connections
> - Rigorous treatment: [[§29 The Mean Value Theorem#^cor-29-7|451 Cor. §29.7]], which also gives the non-strict version ($f' \ge 0$ implies $f$ non-decreasing).

> [!example] Example §33.1: Intervals of Increase and Local Extrema
> Find where $f(x) = 3x^4 - 4x^3 - 12x^2 + 5$ is increasing and where it is decreasing, and find its local maximum and minimum values.
>
> $$
> f'(x) = 12x^3 - 12x^2 - 24x = 12x(x^2 - x - 2) = 12x(x - 2)(x + 1) .
> $$
>
> $f'(x) = 0$ at $x = -1, 0, 2$, the critical numbers of $f$. They divide the line into four intervals, on each of which $f'$ has constant sign (it is continuous and has no zeros there). The sign is the product of the signs of the three factors:
>
> | interval | $12x$ | $x - 2$ | $x + 1$ | $f'(x)$ | $f$ |
> |---|---|---|---|---|---|
> | $x < -1$ | $-$ | $-$ | $-$ | $-$ | decreasing on $(-\infty, -1)$ |
> | $-1 < x < 0$ | $-$ | $-$ | $+$ | $+$ | increasing on $(-1, 0)$ |
> | $0 < x < 2$ | $+$ | $-$ | $+$ | $-$ | decreasing on $(0, 2)$ |
> | $x > 2$ | $+$ | $+$ | $+$ | $+$ | increasing on $(2, \infty)$ |
>
> (One may also say that $f$ is decreasing on the closed interval $[0, 2]$.) By the First Derivative Test below: $f'$ changes from negative to positive at $-1$, so $f(-1) = 3 + 4 - 12 + 5 = 0$ is a local minimum value; from positive to negative at $0$, so $f(0) = 5$ is a local maximum value; and from negative to positive at $2$, so $f(2) = 48 - 32 - 48 + 5 = -27$ is a local minimum value.
>
> *Stewart: Examples 4.3.1 and 4.3.2*

^ex-30-1

## The First Derivative Test

By Fermat's Theorem ([[§28 Maximum and Minimum Values#^cor-28-3|Corollary §28.3]]) a local extremum can only occur at a critical number, but not every critical number gives one. In [[§30 What Derivatives Tell Us About the Shape of a Graph#^ex-30-1|Example §30.1]], $f(0) = 5$ is a local maximum because $f$ rises up to $0$ and falls after it: $f'$ changes sign from positive to negative at $0$.

> [!theorem] Theorem §30.2: The First Derivative Test
> Suppose that $c$ is a critical number of a continuous function $f$.
>
> (a) If $f'$ changes from positive to negative at $c$, then $f$ has a local maximum at $c$.
>
> (b) If $f'$ changes from negative to positive at $c$, then $f$ has a local minimum at $c$.
>
> (c) If $f'$ is positive to the left and right of $c$, or negative to the left and right of $c$, then $f$ has no local maximum or minimum at $c$.
>
> *Stewart: 4.3, The First Derivative Test*

^thm-30-2

> [!proof]+ Proof
> Stewart's argument: in (a), $f$ is increasing to the left of $c$ and decreasing to the right of $c$ (I/D Test), so $f$ has a local maximum at $c$. (The I/D Test applies to the open intervals on either side; that $c$ itself fits in needs the continuity of $f$ at $c$. Here is the argument with that step included.)
>
> "$f'$ changes from positive to negative at $c$" means: there is $\delta > 0$ such that $f'(x) > 0$ for $c - \delta < x < c$ and $f'(x) < 0$ for $c < x < c + \delta$.
>
> (a) Let $c - \delta < x < c$. $f$ is continuous on $[x, c]$ and differentiable on $(x, c)$, so the Mean Value Theorem gives $\xi \in (x, c)$ with $f(c) - f(x) = f'(\xi)(c - x) > 0$, since $f'(\xi) > 0$ and $c - x > 0$. So $f(x) < f(c)$. Let $c < x < c + \delta$. Then $f(x) - f(c) = f'(\xi)(x - c) < 0$ for some $\xi \in (c, x)$, since $f'(\xi) < 0$. So again $f(x) < f(c)$. Hence $f(c) \ge f(x)$ for all $x$ in the open interval $(c - \delta, c + \delta)$: a local maximum ([[§28 Maximum and Minimum Values#^def-28-2|Def. §28.2]]).
>
> (b) The same argument with all signs reversed gives $f(x) > f(c)$ for $0 < |x - c| < \delta$: a local minimum.
>
> (c) Say $f' > 0$ on both sides (the other case is the same with signs reversed). The argument of (a) gives $f(x) < f(c)$ for $c - \delta < x < c$ and $f(x) > f(c)$ for $c < x < c + \delta$. Every open interval containing $c$ contains points of both kinds, so $f(c)$ is neither $\ge$ all nearby values nor $\le$ all of them: no local maximum or minimum at $c$.

^pf-30-2

*Uses:* [[§29 Rolle's Theorem and the Mean Value Theorem#^thm-29-2|§29.2]], [[§30 What Derivatives Tell Us About the Shape of a Graph#^thm-30-1|§30.1]], [[§28 Maximum and Minimum Values#^def-28-2|Def. §28.2]]

> [!example] Example §33.2: A Trigonometric Function
> Find the local maximum and minimum values of $g(x) = x + 2\sin x$, $0 \le x \le 2\pi$.
>
> $g'(x) = 1 + 2\cos x$, so $g'(x) = 0$ when $\cos x = -\frac12$, that is, at $x = 2\pi/3$ and $x = 4\pi/3$. Since $g$ is differentiable everywhere, these are the only critical numbers. On each interval between them $g'$ has constant sign, which a test value shows (or the graph of $\cos$: $g'(x) > 0$ exactly when $\cos x > -\frac12$):
>
> | interval | $g'(x) = 1 + 2\cos x$ | $g$ |
> |---|---|---|
> | $0 < x < 2\pi/3$ | $+$ | increasing on $(0, 2\pi/3)$ |
> | $2\pi/3 < x < 4\pi/3$ | $-$ | decreasing on $(2\pi/3, 4\pi/3)$ |
> | $4\pi/3 < x < 2\pi$ | $+$ | increasing on $(4\pi/3, 2\pi)$ |
>
> $g'$ changes from positive to negative at $2\pi/3$, so by the First Derivative Test the local maximum value is
>
> $$
> g(2\pi/3) = \frac{2\pi}{3} + 2\sin\frac{2\pi}{3} = \frac{2\pi}{3} + 2\cdot\frac{\sqrt3}{2} = \frac{2\pi}{3} + \sqrt3 \approx 3.83 .
> $$
>
> $g'$ changes from negative to positive at $4\pi/3$, so the local minimum value is
>
> $$
> g(4\pi/3) = \frac{4\pi}{3} + 2\sin\frac{4\pi}{3} = \frac{4\pi}{3} + 2\Big(-\frac{\sqrt3}{2}\Big) = \frac{4\pi}{3} - \sqrt3 \approx 2.46 .
> $$
>
> *Stewart: Example 4.3.3*

^ex-30-2

## What Does f″ Say About f?

Two increasing functions on $(a, b)$ can join the same two points and still look different, because they bend in different directions. The tangent lines tell them apart.

> [!definition] Definition §30.1: Concave Upward and Concave Downward
> If the graph of $f$ lies above all of its tangents on an interval $I$, then $f$ is called **concave upward** on $I$. If the graph of $f$ lies below all of its tangents on $I$, then $f$ is called **concave downward** on $I$.
>
> Stewart abbreviates these as **CU** and **CD**.
>
> *Stewart: 4.3, Definition (concavity)*

^def-30-1

On a CU curve, going from left to right, the slope of the tangent increases: $f'$ is increasing, so $f''$ is positive. On a CD curve $f'$ decreases and $f''$ is negative. The reverse reasoning is the Concavity Test.

> [!theorem] Theorem §30.3: The Concavity Test
> (a) If $f''(x) > 0$ on an interval $I$, then the graph of $f$ is concave upward on $I$.
>
> (b) If $f''(x) < 0$ on an interval $I$, then the graph of $f$ is concave downward on $I$.
>
> *Stewart: 4.3, Concavity Test; proof in Appendix F*

^thm-30-3

> [!proof]+ Proof
> (a) Let $a$ be any number in $I$. We must show that the curve $y = f(x)$ lies above the tangent line at $(a, f(a))$, whose equation is $y = f(a) + f'(a)(x - a)$. That is, we must show that
>
> $$
> f(x) > f(a) + f'(a)(x - a) \qquad\text{whenever } x \in I,\ x \ne a .
> $$
>
> *The case $x > a$.* Applying the Mean Value Theorem to $f$ on $[a, x]$ (where $f$ is differentiable, since $f''$ exists on $I$), we get a number $c$ with $a < c < x$ such that
>
> $$
> f(x) - f(a) = f'(c)(x - a) . \qquad (1)
> $$
>
> Since $f'' > 0$ on $I$, the I/D Test applied to $f'$ shows that $f'$ is increasing on $I$. Since $a < c$, $f'(a) < f'(c)$, and multiplying by the positive number $x - a$,
>
> $$
> f'(a)(x - a) < f'(c)(x - a) . \qquad (2)
> $$
>
> Adding $f(a)$ to both sides, $f(a) + f'(a)(x - a) < f(a) + f'(c)(x - a)$. By (1) the right side is $f(x)$, so
>
> $$
> f(x) > f(a) + f'(a)(x - a) , \qquad (3)
> $$
>
> which is what we wanted.
>
> *The case $x < a$.* Now the Mean Value Theorem on $[x, a]$ gives (1) with $x < c < a$, so $f'(c) < f'(a)$. Multiplying by the *negative* number $x - a$ reverses the inequality, and we get (2) and then (3) as before.
>
> (b) (Not written out by Stewart.) If $f'' < 0$ on $I$, then $(-f)'' = -f'' > 0$, so by (a) the graph of $-f$ lies above its tangents: $-f(x) > -f(a) - f'(a)(x - a)$. Multiplying by $-1$, $f(x) < f(a) + f'(a)(x - a)$: the graph of $f$ lies below its tangents.

^pf-30-3

*Uses:* [[§30 What Derivatives Tell Us About the Shape of a Graph#^def-30-1|Def. §30.1]], [[§29 Rolle's Theorem and the Mean Value Theorem#^thm-29-2|§29.2]], [[§30 What Derivatives Tell Us About the Shape of a Graph#^thm-30-1|§30.1]]

![[m233-27-1.svg]]
*The proof of the Concavity Test. For $x > a$ the Mean Value Theorem writes $f(x) = f(a) + f'(c)(x - a)$ with $c$ between $a$ and $x$. Because $f'$ is increasing, the slope $f'(c)$ of the secant (blue) beats the slope $f'(a)$ of the tangent (red), so over the run $x - a$ the graph climbs higher than the tangent line: the green gap is positive.*

> [!definition] Definition §30.2: Inflection Point
> A point $P$ on a curve $y = f(x)$ is called an **inflection point** if $f$ is continuous there and the curve changes from concave upward to concave downward or from concave downward to concave upward at $P$.
>
> If the curve has a tangent at an inflection point, then the curve crosses its tangent there. By the Concavity Test, there is an inflection point at any point where $f$ is continuous and $f''$ changes sign.
>
> *Stewart: 4.3, Definition (inflection point)*

^def-30-2

For example, in a population curve $P(t)$ that grows slowly, then quickly, then levels off toward a carrying capacity, the inflection point is where the growth rate $P'(t)$ is largest (Stewart's Example 4.3.4, a honeybee population with inflection near $t = 12$ weeks).

## The Second Derivative Test

> [!theorem] Theorem §30.4: The Second Derivative Test
> Suppose $f''$ is continuous near $c$.
>
> (a) If $f'(c) = 0$ and $f''(c) > 0$, then $f$ has a local minimum at $c$.
>
> (b) If $f'(c) = 0$ and $f''(c) < 0$, then $f$ has a local maximum at $c$.
>
> *Stewart: 4.3, The Second Derivative Test*

^thm-30-4

> [!proof]+ Proof
> Stewart's argument for (a): $f''(x) > 0$ near $c$, so $f$ is concave upward near $c$, so the graph lies above its horizontal tangent at $c$, and $f$ has a local minimum at $c$. In detail:
>
> (a) (Stewart asserts that $f'' > 0$ near $c$; here is why.) $f''$ is continuous at $c$ and $f''(c) > 0$, so $\lim_{x \to c} f''(x) = f''(c) > 0$. Taking $\varepsilon = f''(c)$ in the definition of the limit ([[§11 The Precise Definition of a Limit#^def-11-1|Def. §11.1]]), there is $\delta > 0$ such that $|f''(x) - f''(c)| < f''(c)$, hence $f''(x) > 0$, for all $x$ in the open interval $I = (c - \delta, c + \delta)$. By the Concavity Test the graph of $f$ lies above its tangent line at $c$ on $I$:
>
> $$
> f(x) > f(c) + f'(c)(x - c) = f(c) \qquad\text{for } x \in I,\ x \ne c ,
> $$
>
> since $f'(c) = 0$. So $f(c) \le f(x)$ for all $x$ in $I$: $f$ has a local minimum at $c$.
>
> (b) Apply (a) to $-f$: $(-f)'(c) = 0$ and $(-f)''(c) > 0$, so $-f$ has a local minimum at $c$, that is, $f$ has a local maximum at $c$.

^pf-30-4

*Uses:* [[§30 What Derivatives Tell Us About the Shape of a Graph#^thm-30-3|§30.3]], [[§30 What Derivatives Tell Us About the Shape of a Graph#^def-30-1|Def. §30.1]], [[§28 Maximum and Minimum Values#^def-28-2|Def. §28.2]], [[§11 The Precise Definition of a Limit#^def-11-1|Def. §11.1]]

> [!remark]- Connections
> - Several variables: the Hessian test, [[§18 Second-Order Sufficient Conditions#^thm-18-1|452 Thm. §18.1]]; in this subject, [[§113 Maximum and Minimum Values#^thm-113-2|Theorem §113.2]].

> [!remark] Remark: When the Second Derivative Test Is Inconclusive
> If $f''(c) = 0$, the test gives no information: at such a point there might be a maximum, a minimum, or neither. The functions $x^4$, $-x^4$ and $x^3$ all have $f'(0) = f''(0) = 0$, and they have a minimum, a maximum and neither at $0$. The test also fails when $f''(c)$ does not exist. In such cases use the First Derivative Test. Even when both tests apply, the First Derivative Test is often easier.

^rem-30-1

> [!example] Example §33.3: Concavity, Inflection Points and the Second Derivative Test
> Discuss the curve $y = x^4 - 4x^3$ with respect to concavity, points of inflection, and local maxima and minima.
>
> With $f(x) = x^4 - 4x^3$,
>
> $$
> f'(x) = 4x^3 - 12x^2 = 4x^2(x - 3), \qquad f''(x) = 12x^2 - 24x = 12x(x - 2) .
> $$
>
> **Critical numbers.** $f'$ is a polynomial, defined everywhere, so the critical numbers are the solutions of $f'(x) = 0$: $x = 0$ and $x = 3$.
>
> **Second Derivative Test.** $f''(3) = 36 > 0$, and $f'(3) = 0$, so $f(3) = 81 - 108 = -27$ is a local minimum. $f''(0) = 0$, so the test gives no information about $0$. But $f'(x) = 4x^2(x - 3) < 0$ for $x < 0$ and for $0 < x < 3$, so $f'$ does not change sign at $0$, and by the First Derivative Test $f$ has no local maximum or minimum at $0$.
>
> **Concavity.** $f''(x) = 0$ at $x = 0$ and $x = 2$:
>
> | interval | $f''(x) = 12x(x - 2)$ | concavity |
> |---|---|---|
> | $(-\infty, 0)$ | $+$ | upward |
> | $(0, 2)$ | $-$ | downward |
> | $(2, \infty)$ | $+$ | upward |
>
> $(0, 0)$ is an inflection point, since the curve changes from CU to CD there. $(2, f(2)) = (2, -16)$ is an inflection point, since the curve changes from CD to CU.
>
> *Stewart: Example 4.3.6*

^ex-30-3

![[m233-27-2.svg]]
*[[§30 What Derivatives Tell Us About the Shape of a Graph#^ex-30-3|Example §30.3]]: $y = x^4 - 4x^3$. At $0$ the tangent is horizontal ($f'(0) = 0$) but there is no extremum: the curve crosses its tangent, since $(0, 0)$ is also an inflection point. The only local extremum is the minimum $(3, -27)$ (blue); the second inflection point is $(2, -16)$ (red). The shading marks where the curve is concave upward.*

## Curve Sketching

The first and second derivatives together determine the shape of a graph.

> [!example] Example §33.4: A Graph with a Cusp and Vertical Tangents
> Sketch the graph of $f(x) = x^{2/3}(6 - x)^{1/3}$.
>
> The domain is $\mathbb{R}$. By the Product and Chain Rules,
>
> $$
> f'(x) = \tfrac23 x^{-1/3}(6 - x)^{1/3} - \tfrac13 x^{2/3}(6 - x)^{-2/3} = \frac{2(6 - x) - x}{3x^{1/3}(6 - x)^{2/3}} = \frac{4 - x}{x^{1/3}(6 - x)^{2/3}} ,
> $$
>
> and differentiating again and simplifying,
>
> $$
> f''(x) = \frac{-8}{x^{4/3}(6 - x)^{5/3}} .
> $$
>
> **Critical numbers.** $f'(x) = 0$ when $x = 4$, and $f'(x)$ does not exist when $x = 0$ or $x = 6$. So the critical numbers are $0$, $4$ and $6$.
>
> | interval | $4 - x$ | $x^{1/3}$ | $(6 - x)^{2/3}$ | $f'(x)$ | $f$ |
> |---|---|---|---|---|---|
> | $x < 0$ | $+$ | $-$ | $+$ | $-$ | decreasing on $(-\infty, 0)$ |
> | $0 < x < 4$ | $+$ | $+$ | $+$ | $+$ | increasing on $(0, 4)$ |
> | $4 < x < 6$ | $-$ | $+$ | $+$ | $-$ | decreasing on $(4, 6)$ |
> | $x > 6$ | $-$ | $+$ | $+$ | $-$ | decreasing on $(6, \infty)$ |
>
> **Local extrema (First Derivative Test).** $f'$ changes from negative to positive at $0$, so $f(0) = 0$ is a local minimum. $f'$ changes from positive to negative at $4$, so $f(4) = 4^{2/3}\cdot 2^{1/3} = 2^{4/3}\cdot 2^{1/3} = 2^{5/3} \approx 3.17$ is a local maximum. The sign of $f'$ does not change at $6$: no extremum there. (The Second Derivative Test could be used at $4$, but not at $0$ or $6$, where $f''$ does not exist.)
>
> **Concavity.** $x^{4/3} = (x^{1/3})^4 \ge 0$, and $(6 - x)^{5/3}$ has the sign of $6 - x$. So $f''(x) < 0$ for $x < 0$ and for $0 < x < 6$, and $f''(x) > 0$ for $x > 6$. Thus $f$ is concave downward on $(-\infty, 0)$ and $(0, 6)$ and concave upward on $(6, \infty)$, and the only inflection point is $(6, 0)$.
>
> **The sketch.** Since $|f'(x)| \to \infty$ as $x \to 0$ and as $x \to 6$, the curve has vertical tangents at $(0, 0)$ (a cusp, as $f'$ changes from $-\infty$ to $+\infty$) and at $(6, 0)$. The curve comes down to the cusp at $0$, rises to the maximum $(4, 2^{5/3})$, and falls through the inflection point $(6, 0)$, where it is momentarily vertical.
>
> *Stewart: Example 4.3.7*

^ex-30-4

> [!example] Example §30.5: Using Asymptotes as Well
> Use the first and second derivatives of $f(x) = e^{1/x}$, together with asymptotes, to sketch its graph.
>
> **Asymptotes.** The domain is $\{x \mid x \ne 0\}$. As $x \to 0^+$, $t = 1/x \to \infty$, and as $x \to 0^-$, $t = 1/x \to -\infty$, so
>
> $$
> \lim_{x \to 0^+} e^{1/x} = \lim_{t \to \infty} e^t = \infty, \qquad \lim_{x \to 0^-} e^{1/x} = \lim_{t \to -\infty} e^t = 0 .
> $$
>
> So $x = 0$ is a vertical asymptote (from the right). As $x \to \pm\infty$, $1/x \to 0$ and $e^{1/x} \to e^0 = 1$, so $y = 1$ is a horizontal asymptote on both sides ([[§13 Limits at Infinity; Horizontal Asymptotes#^def-13-2|Def. §13.2]]).
>
> **First derivative.** By the Chain Rule,
>
> $$
> f'(x) = -\frac{e^{1/x}}{x^2} .
> $$
>
> Since $e^{1/x} > 0$ and $x^2 > 0$ for $x \ne 0$, $f'(x) < 0$ for all $x \ne 0$: $f$ is decreasing on $(-\infty, 0)$ and on $(0, \infty)$. There is no critical number, so no local maximum or minimum.
>
> **Second derivative.**
>
> $$
> f''(x) = -\frac{x^2 e^{1/x}(-1/x^2) - e^{1/x}(2x)}{x^4} = \frac{e^{1/x}(2x + 1)}{x^4} .
> $$
>
> Since $e^{1/x} > 0$ and $x^4 > 0$, $f''(x) > 0$ when $x > -\frac12$ ($x \ne 0$) and $f''(x) < 0$ when $x < -\frac12$. So the curve is concave downward on $(-\infty, -\frac12)$ and concave upward on $(-\frac12, 0)$ and $(0, \infty)$, with one inflection point, $(-\frac12, e^{-2})$.
>
> **The sketch.** Draw the asymptote $y = 1$. On the left, the curve starts just below $y = 1$, falls (concave downward) to the inflection point $(-\frac12, e^{-2}) \approx (-0.5, 0.14)$, and then flattens toward the origin: $f(x) \to 0$ as $x \to 0^-$, although $f(0)$ is not defined. On the right, the curve comes down from $+\infty$ along the $y$-axis and decreases toward $y = 1$, concave upward.
>
> *Stewart: Example 4.3.8*

^ex-30-5
