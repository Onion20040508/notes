---
type: section
subject: "[[Calculus]]"
chapter: 3
section: 26
stewart: "3.10"
aliases: ["Stewart 3.10"]
tags: [calculus]
---
← [[§25 Related Rates]] · ↑ [[· 3 Differentiation Rules]] · [[§27 Hyperbolic Functions]] →

*Stewart, Section 3.10.*

Zooming in toward a point on the graph of a differentiable function, the graph looks more and more like its tangent line ([[§14 Derivatives and Rates of Change#^thm-14-2|Theorem §14.2]]). So near $a$ we may replace $f$ by the linear function whose graph is the tangent line, the *linearization* $L(x) = f(a) + f'(a)(x - a)$: it is easy to evaluate and gives approximate values of $f$ near $a$. The same idea in the notation of *differentials* says that the change $\Delta y$ of $f$ is approximately $dy = f'(x)\,dx$, the change along the tangent line, which is how errors in measured quantities propagate into computed ones.

## Linearization and Approximation

> [!definition] Definition §26.1: Linearization and Linear Approximation
> Let $f$ be differentiable at $a$. The tangent line to $y = f(x)$ at $(a, f(a))$ is $y = f(a) + f'(a)(x - a)$. The linear function
>
> $$
> L(x) = f(a) + f'(a)(x - a) \qquad (1)
> $$
>
> is the **linearization** of $f$ at $a$. The approximation
>
> $$
> f(x) \approx f(a) + f'(a)(x - a) \qquad (2)
> $$
>
> is the **linear approximation** or **tangent line approximation** of $f$ at $a$, used for $x$ near $a$.
>
> *Stewart: 3.10, Equations 1 and 2*

^def-26-1

> [!remark]- Connections
> - How good is it? Taylor's Theorem with $n = 2$ bounds the error: $f(x) - L(x) = \frac12 f''(c)(x - a)^2$ for some $c$ between $a$ and $x$ ([[§31 Taylor's Theorem#^thm-31-2|451 Thm. §31.2]]; in Calculus, [[§90 Taylor and Maclaurin Series#^rem-90-2|Remark: Formulas for the Remainder]]). This explains [[§26 Linear Approximations and Differentials#^ex-26-1|Example §26.1]]: the error grows like $(x - a)^2$, and its sign is that of $f''$.
> - In several variables the tangent line becomes the tangent plane: [[§109 Tangent Planes and Linear Approximations#^def-109-2|Definition §109.2]] (Stewart 14.4), and [[§7 Differentiability#^def-7-1|452 Def. §7.1]], where good linear approximation is the definition of differentiability.

> [!example] Example §29.1: Linearizing a Square Root
> Find the linearization of $f(x) = \sqrt{x + 3}$ at $a = 1$ and use it to approximate $\sqrt{3.98}$ and $\sqrt{4.05}$. Are these overestimates or underestimates?
>
> The derivative of $f(x) = (x + 3)^{1/2}$ is
>
> $$
> f'(x) = \tfrac12 (x + 3)^{-1/2} = \frac{1}{2\sqrt{x + 3}} ,
> $$
>
> so $f(1) = 2$ and $f'(1) = \frac14$. By Equation 1,
>
> $$
> L(x) = f(1) + f'(1)(x - 1) = 2 + \tfrac14 (x - 1) = \frac74 + \frac x4 ,
> $$
>
> and the linear approximation is $\sqrt{x + 3} \approx \dfrac74 + \dfrac x4$ for $x$ near $1$. In particular,
>
> $$
> \sqrt{3.98} \approx \tfrac74 + \tfrac{0.98}{4} = 1.995, \qquad \sqrt{4.05} \approx \tfrac74 + \tfrac{1.05}{4} = 2.0125 .
> $$
>
> The graph of $\sqrt{x + 3}$ is concave down, so the tangent line lies above the curve: both are overestimates. Comparing with the true values, the approximation is good near $1$ and deteriorates farther away:
>
> | | $x$ | from $L(x)$ | actual value |
> |---|---|---|---|
> | $\sqrt{3.9}$ | $0.9$ | $1.975$ | $1.97484176\ldots$ |
> | $\sqrt{3.98}$ | $0.98$ | $1.995$ | $1.99499373\ldots$ |
> | $\sqrt{4}$ | $1$ | $2$ | $2.00000000\ldots$ |
> | $\sqrt{4.05}$ | $1.05$ | $2.0125$ | $2.01246117\ldots$ |
> | $\sqrt{4.1}$ | $1.1$ | $2.025$ | $2.02484567\ldots$ |
> | $\sqrt{5}$ | $2$ | $2.25$ | $2.23606797\ldots$ |
> | $\sqrt{6}$ | $3$ | $2.5$ | $2.44948974\ldots$ |
>
> A calculator would give $\sqrt{3.98}$ and $\sqrt{4.05}$ directly, but the linear approximation gives an approximation over a whole interval.
>
> *Stewart: Example 3.10.1*

^ex-26-1

> [!example] Example §29.2: How Accurate Is the Approximation?
> For what values of $x$ is the linear approximation $\sqrt{x + 3} \approx \frac74 + \frac x4$ accurate to within $0.5$? To within $0.1$?
>
> Accuracy to within $0.5$ means $\left| \sqrt{x + 3} - \left( \frac74 + \frac x4 \right) \right| < 0.5$, that is,
>
> $$
> \sqrt{x + 3} - 0.5 < \frac74 + \frac x4 < \sqrt{x + 3} + 0.5 :
> $$
>
> the tangent line must lie between the curve shifted up by $0.5$ and the curve shifted down by $0.5$. Stewart reads the answer off a graph; it can also be found exactly. The tangent line lies above the curve, so only the right inequality matters. Put $u = \sqrt{x + 3} \ge 0$, so $x = u^2 - 3$. Then $\frac74 + \frac x4 = \frac{u^2 + 4}{4}$, and the condition becomes
>
> $$
> \frac{u^2 + 4}{4} < u + 0.5 \iff u^2 - 4u + 2 < 0 \iff 2 - \sqrt2 < u < 2 + \sqrt2 .
> $$
>
> Squaring back, $x = u^2 - 3$ runs over $\big(3 - 4\sqrt2,\ 3 + 4\sqrt2\big) \approx (-2.657, 8.657)$. So the approximation is accurate to within $0.5$ when $-2.6 < x < 8.6$ (rounding the smaller value up and the larger down), as Stewart's graph shows.
>
> For $0.1$ the same computation gives $\frac{u^2 + 4}{4} < u + 0.1 \iff u^2 - 4u + 3.6 < 0 \iff |u - 2| < \sqrt{0.4}$, so $x = u^2 - 3 \in \big(1.4 - 4\sqrt{0.4},\ 1.4 + 4\sqrt{0.4}\big) \approx (-1.130, 3.930)$: accurate to within $0.1$ when $-1.1 < x < 3.9$.
>
> *Stewart: Example 3.10.2*

^ex-26-2

> [!remark] Remark: Applications to Physics
> Physicists often replace a function by its linearization. The linearization of $\sin x$ at $a = 0$ is $L(x) = \sin 0 + \cos 0 \cdot (x - 0) = x$, so
>
> $$
> \sin x \approx x \quad \text{for } x \text{ near } 0 .
> $$
>
> The usual derivation of the period of a pendulum replaces $\sin\theta$ by $\theta$ in this way. In paraxial (Gaussian) optics, for light rays at shallow angles to the optical axis, both $\sin\theta$ and $\cos\theta$ are replaced by their linearizations, $\sin\theta \approx \theta$ and $\cos\theta \approx 1$; the resulting calculations are the basic tool for designing lenses. Further applications come with Taylor polynomials in Section 11.11.

^rem-26-1

## Differentials

> [!definition] Definition §26.2: Differentials
> Let $y = f(x)$ with $f$ differentiable. The **differential** $dx$ is an independent variable: it can be given the value of any real number. The **differential** $dy$ is then defined in terms of $dx$ by
>
> $$
> dy = f'(x)\,dx . \qquad (3)
> $$
>
> So $dy$ is a dependent variable: it depends on $x$ and $dx$. If $dx \ne 0$, dividing by $dx$ gives $\dfrac{dy}{dx} = f'(x)$, where the left side can now genuinely be read as a ratio of differentials.
>
> *Stewart: 3.10, Equation 3*

^def-26-2

> [!remark]- Connections
> - The differential of a function of several variables: [[§10 The Differential#^def-10-1|452 Def. §10.1]], again a function of the point and of the increments $dx = h$, $dy = k$.

> [!remark] Remark: dy Versus Δy
> Let $P(x, f(x))$ and $Q(x + \Delta x, f(x + \Delta x))$ be points on the graph of $f$, and let $dx = \Delta x$. The change in $y$ is
>
> $$
> \Delta y = f(x + \Delta x) - f(x) .
> $$
>
> The tangent line $PR$ has slope $f'(x)$, so over the run $dx$ it rises by $f'(x)\,dx = dy$. Thus $dy$ is the amount the tangent line rises or falls (the change in the linearization), while $\Delta y$ is the amount the curve $y = f(x)$ rises or falls when $x$ changes by $dx$. For small $dx$, $\Delta y \approx dy$, and $dy$ is usually easier to compute. With $dx = x - a$, the linear approximation (2) reads
>
> $$
> f(a + dx) \approx f(a) + dy .
> $$
>
> For instance, for $f(x) = \sqrt{x + 3}$ ([[§26 Linear Approximations and Differentials#^ex-26-1|Example §26.1]]), $dy = \dfrac{dx}{2\sqrt{x + 3}}$; with $a = 1$ and $dx = 0.05$, $dy = \dfrac{0.05}{2\sqrt{4}} = 0.0125$, and $\sqrt{4.05} = f(1.05) \approx f(1) + dy = 2.0125$, as before.

^rem-26-2

![[m233-23-1.svg]]
*Differentials. Over the run $dx = \Delta x$ from $P$, the curve rises by $\Delta y$ (to $Q$, green) and the tangent line rises by $dy = f'(x)\,dx$ (to $R$, red). Here $f$ is concave down, so $dy > \Delta y$; in general $dy - \Delta y$ is small compared with $dx$ when $dx$ is small ([[§20 The Chain Rule#^lem-20-1|Lemma §20.1]]).*

> [!example] Example §29.3: Comparing Δy and dy
> Compare $\Delta y$ and $dy$ for $y = f(x) = x^3 + x^2 - 2x + 1$ when $x$ changes (a) from $2$ to $2.05$ and (b) from $2$ to $2.01$.
>
> In general $dy = f'(x)\,dx = (3x^2 + 2x - 2)\,dx$, and at $x = 2$ the factor is $3(2)^2 + 2(2) - 2 = 14$. Also $f(2) = 8 + 4 - 4 + 1 = 9$.
>
> **(a)** $f(2.05) = (2.05)^3 + (2.05)^2 - 2(2.05) + 1 = 9.717625$, so $\Delta y = 0.717625$, while $dy = 14(0.05) = 0.7$.
>
> **(b)** $f(2.01) = (2.01)^3 + (2.01)^2 - 2(2.01) + 1 = 9.140701$, so $\Delta y = 0.140701$, while $dy = 14(0.01) = 0.14$.
>
> The approximation $\Delta y \approx dy$ improves as $\Delta x$ gets smaller: the error is $0.017625$ in (a) and $0.000701$ in (b), roughly in the ratio $(0.05/0.01)^2 = 25$. And $dy$ was easier to compute than $\Delta y$.
>
> *Stewart: Example 3.10.3*

^ex-26-3

> [!definition] Definition §26.3: Relative Error
> If a quantity $V$ is computed with an error $\Delta V$, the **relative error** is the error divided by the total value, $\Delta V / V$. Approximating $\Delta V$ by the differential, $\dfrac{\Delta V}{V} \approx \dfrac{dV}{V}$. Multiplied by $100$, it is the **percentage error**.
>
> *Stewart: 3.10 (Note)*

^def-26-3

> [!example] Example §29.4: Error in the Volume of a Sphere
> The radius of a sphere was measured to be $21$ cm with a possible error of at most $0.05$ cm. What is the maximum error in using this value to compute the volume?
>
> With radius $r$, the volume is $V = \frac43 \pi r^3$. If the error in the measured $r$ is $dr = \Delta r$, the corresponding error $\Delta V$ in the computed volume is approximately the differential
>
> $$
> dV = 4\pi r^2\,dr .
> $$
>
> With $r = 21$ and $dr = 0.05$, $dV = 4\pi (21)^2 (0.05) = 88.2\pi \approx 277$. The maximum error in the calculated volume is about $277$ cm³.
>
> **Relative error.** This looks large, but relative to the volume it is small:
>
> $$
> \frac{\Delta V}{V} \approx \frac{dV}{V} = \frac{4\pi r^2\,dr}{\frac43 \pi r^3} = 3\,\frac{dr}{r} .
> $$
>
> The relative error in the volume is about three times the relative error in the radius. Here $dr/r = 0.05/21 \approx 0.0024$, giving a relative error of about $0.007$ in the volume: percentage errors of $0.24\%$ in the radius and $0.7\%$ in the volume.
>
> *Stewart: Example 3.10.4 and Note*

^ex-26-4
