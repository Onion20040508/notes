---
type: section
subject: "[[Calculus]]"
chapter: 4
section: 32
stewart: "4.5"
aliases: ["Stewart 4.5"]
tags: [calculus]
---
← [[§31 Indeterminate Forms and L'Hospital's Rule]] · ↑ [[· 4 Applications of Differentiation]] · [[§33 Graphing with Calculus and Technology]] →

*Stewart, Section 4.5.*

This section puts together everything known so far about a function to sketch its graph by hand: domain, symmetry and periodicity ([[§1 Four Ways to Represent a Function#^def-1-7|Def. §1.7]]), asymptotes ([[§8 The Limit of a Function#^def-8-6|Def. §8.6]], [[§13 Limits at Infinity; Horizontal Asymptotes#^def-13-2|Def. §13.2]]), intervals of increase and decrease, extreme values, concavity and inflection points ([[§30 What Derivatives Tell Us About the Shape of a Graph|§30]]), and l'Hospital's Rule for the limits ([[§31 Indeterminate Forms and L'Hospital's Rule#^thm-31-2|Theorem §31.2]]). Calculus finds the important features *exactly*, and it finds features that a machine-drawn graph can hide. For instance, the graph of $f(x) = 8x^3 - 21x^2 + 18x + 2$ in a standard window looks like a cubic with no extreme points, but $f'(x) = 24x^2 - 42x + 18 = 6(4x - 3)(x - 1)$ shows a local maximum $f(0.75) = 7.0625$ and a local minimum $f(1) = 7$, visible only after zooming in. The one new notion is the slant asymptote.

## Guidelines for Sketching a Curve

> [!definition] Definition §35.1: Periodic Function
> If $f(x + p) = f(x)$ for all $x$ in the domain $D$ of $f$, where $p$ is a positive constant, then $f$ is called a **periodic function**, and the smallest such number $p$ is called the **period**.
>
> For instance, $\sin x$ has period $2\pi$ and $\tan x$ has period $\pi$. If we know what the graph looks like on an interval of length $p$, the rest is obtained by translation.
>
> *Stewart: 4.5 (text)*

^def-32-1

> [!remark] Remark: Method — Guidelines for Sketching a Curve
> Not every item is relevant to every function, but together they give everything needed for a sketch of $y = f(x)$ that shows its important features.
>
> **A. Domain.** Determine the domain $D$ of $f$: the set of $x$ for which $f(x)$ is defined.
>
> **B. Intercepts.** The $y$-intercept is $f(0)$. For the $x$-intercepts, set $y = 0$ and solve for $x$ (omit this if the equation is hard to solve).
>
> **C. Symmetry.**
> - If $f(-x) = f(x)$ for all $x$ in $D$ ($f$ is *even*), the curve is symmetric about the $y$-axis: sketch it for $x \ge 0$ and reflect about the $y$-axis. Examples: $x^2$, $x^4$, $|x|$, $\cos x$.
> - If $f(-x) = -f(x)$ for all $x$ in $D$ ($f$ is *odd*), the curve is symmetric about the origin: sketch it for $x \ge 0$ and rotate $180°$ about the origin. Examples: $x$, $x^3$, $1/x$, $\sin x$.
> - If $f$ is periodic with period $p$ ([[§32 Summary of Curve Sketching#^def-32-1|Definition §32.1]]), sketch it on an interval of length $p$ and translate.
>
> **D. Asymptotes.**
> - *Horizontal:* if $\lim_{x \to \infty} f(x) = L$ or $\lim_{x \to -\infty} f(x) = L$, then $y = L$ is a horizontal asymptote. If $\lim_{x \to \infty} f(x) = \pm\infty$, there is no asymptote to the right, but this is still useful information.
> - *Slant:* see [[§32 Summary of Curve Sketching#^def-32-2|Definition §32.2]] below.
> - *Vertical:* $x = a$ is a vertical asymptote if at least one of the following holds:
>
> $$
> \lim_{x \to a^+} f(x) = \infty, \quad \lim_{x \to a^-} f(x) = \infty, \quad \lim_{x \to a^+} f(x) = -\infty, \quad \lim_{x \to a^-} f(x) = -\infty . \qquad (1)
> $$
>
> For rational functions, the vertical asymptotes are found by setting the denominator equal to $0$ after cancelling common factors; for other functions this does not apply. It is useful to know exactly which of the statements in (1) holds. If $f(a)$ is not defined but $a$ is an endpoint of $D$, compute the one-sided limit at $a$, whether or not it is infinite.
>
> **E. Intervals of increase or decrease.** Compute $f'(x)$ and use the I/D Test ([[§30 What Derivatives Tell Us About the Shape of a Graph#^thm-30-1|Theorem §30.1]]): $f$ is increasing where $f' > 0$ and decreasing where $f' < 0$.
>
> **F. Local maximum and minimum values.** Find the critical numbers ($f'(c) = 0$ or $f'(c)$ does not exist) and use the First Derivative Test ([[§30 What Derivatives Tell Us About the Shape of a Graph#^thm-30-2|Theorem §30.2]]). The Second Derivative Test ([[§30 What Derivatives Tell Us About the Shape of a Graph#^thm-30-4|Theorem §30.4]]) can be used where $f'(c) = 0$ and $f''(c) \ne 0$, but the First Derivative Test is usually preferable.
>
> **G. Concavity and points of inflection.** Compute $f''(x)$ and use the Concavity Test ([[§30 What Derivatives Tell Us About the Shape of a Graph#^thm-30-3|Theorem §30.3]]). Inflection points occur where the direction of concavity changes.
>
> **H. Sketch the curve.** Draw the asymptotes as dashed lines. Plot the intercepts, the maximum and minimum points and the inflection points. Then draw the curve through these points, rising and falling according to E, with concavity according to G, and approaching the asymptotes. For more accuracy near a point, compute $f'$ there: the tangent shows the direction of the curve.

^rem-32-1

> [!example] Example §35.1: A Rational Function with Three Asymptotes
> Use the guidelines to sketch the curve $y = \dfrac{2x^2}{x^2 - 1}$.
>
> **A.** The domain is $\{x \mid x^2 - 1 \ne 0\} = \{x \mid x \ne \pm 1\} = (-\infty, -1) \cup (-1, 1) \cup (1, \infty)$.
>
> **B.** The $x$- and $y$-intercepts are both $0$.
>
> **C.** $f(-x) = f(x)$: $f$ is even, and the curve is symmetric about the $y$-axis.
>
> **D.** Dividing by $x^2$,
>
> $$
> \lim_{x \to \pm\infty} \frac{2x^2}{x^2 - 1} = \lim_{x \to \pm\infty} \frac{2}{1 - 1/x^2} = 2 ,
> $$
>
> so $y = 2$ is a horizontal asymptote on both sides. The denominator is $0$ at $x = \pm 1$, where the numerator is $2 \ne 0$. Near $x = 1$ the numerator is near $2$ and $x^2 - 1$ has the sign of $x - 1$; near $x = -1$, $x^2 - 1$ has the sign of $-(x + 1)$. So
>
> $$
> \lim_{x \to 1^+} \frac{2x^2}{x^2 - 1} = \infty, \quad \lim_{x \to 1^-} \frac{2x^2}{x^2 - 1} = -\infty, \quad \lim_{x \to -1^+} \frac{2x^2}{x^2 - 1} = -\infty, \quad \lim_{x \to -1^-} \frac{2x^2}{x^2 - 1} = \infty ,
> $$
>
> and $x = 1$, $x = -1$ are vertical asymptotes.
>
> **E.** By the Quotient Rule,
>
> $$
> f'(x) = \frac{(x^2 - 1)(4x) - 2x^2 \cdot 2x}{(x^2 - 1)^2} = \frac{-4x}{(x^2 - 1)^2} .
> $$
>
> $f'(x) > 0$ when $x < 0$ ($x \ne -1$) and $f'(x) < 0$ when $x > 0$ ($x \ne 1$). So $f$ is increasing on $(-\infty, -1)$ and $(-1, 0)$ and decreasing on $(0, 1)$ and $(1, \infty)$.
>
> **F.** The only critical number is $x = 0$. Since $f'$ changes from positive to negative there, $f(0) = 0$ is a local maximum.
>
> **G.**
>
> $$
> f''(x) = \frac{(x^2 - 1)^2(-4) + 4x \cdot 2(x^2 - 1)(2x)}{(x^2 - 1)^4} = \frac{12x^2 + 4}{(x^2 - 1)^3} .
> $$
>
> Since $12x^2 + 4 > 0$ for all $x$, $f''(x) > 0 \iff x^2 - 1 > 0 \iff |x| > 1$, and $f''(x) < 0 \iff |x| < 1$. So the curve is concave upward on $(-\infty, -1)$ and $(1, \infty)$ and concave downward on $(-1, 1)$. There is no inflection point: concavity changes only at $\pm 1$, which are not in the domain.
>
> **H.** See the figure. (On the outer branches the curve approaches $y = 2$ from above, consistent with E: on $(1, \infty)$ it decreases from $\infty$ toward $2$.)
>
> *Stewart: Example 4.5.1*

^ex-32-1

![[m233-29-1.svg]]
*[[§32 Summary of Curve Sketching#^ex-32-1|Example §32.1]]: $y = 2x^2/(x^2 - 1)$ with its asymptotes $y = 2$ and $x = \pm 1$ (dashed). The middle branch has its local maximum at the origin and is concave downward; the outer branches are concave upward and approach $y = 2$ from above. The curve is symmetric about the $y$-axis.*

> [!example] Example §35.2: An Asymptote Found by L'Hospital's Rule
> Sketch the graph of $f(x) = xe^x$.
>
> **A.** The domain is $\mathbb{R}$. **B.** The $x$- and $y$-intercepts are both $0$. **C.** No symmetry.
>
> **D.** As $x \to \infty$, both $x$ and $e^x$ become large, so $\lim_{x \to \infty} xe^x = \infty$. As $x \to -\infty$, $e^x \to 0$: an indeterminate product of type $0 \cdot \infty$. By l'Hospital's Rule,
>
> $$
> \lim_{x \to -\infty} xe^x = \lim_{x \to -\infty} \frac{x}{e^{-x}} = \lim_{x \to -\infty} \frac{1}{-e^{-x}} = \lim_{x \to -\infty} (-e^x) = 0 .
> $$
>
> So the $x$-axis is a horizontal asymptote (on the left).
>
> **E.** $f'(x) = xe^x + e^x = (x + 1)e^x$. Since $e^x > 0$, $f'(x) > 0$ when $x > -1$ and $f'(x) < 0$ when $x < -1$: $f$ is increasing on $(-1, \infty)$ and decreasing on $(-\infty, -1)$.
>
> **F.** $f'(-1) = 0$ and $f'$ changes from negative to positive at $-1$, so $f(-1) = -e^{-1} \approx -0.37$ is a local minimum; since $f$ decreases before $-1$ and increases after, it is in fact the absolute minimum.
>
> **G.** $f''(x) = (x + 1)e^x + e^x = (x + 2)e^x$. So $f'' > 0$ for $x > -2$ and $f'' < 0$ for $x < -2$: $f$ is concave upward on $(-2, \infty)$ and concave downward on $(-\infty, -2)$, with inflection point $(-2, -2e^{-2}) \approx (-2, -0.27)$.
>
> **H.** Coming in from the left just below the $x$-axis, the curve falls (concave downward) through the inflection point $(-2, -0.27)$, reaches its minimum $(-1, -1/e)$, then rises through the origin and grows rapidly, concave upward.
>
> *Stewart: Example 4.5.3*

^ex-32-2

> [!example] Example §35.3: A Periodic Function
> Sketch the graph of $f(x) = \dfrac{\cos x}{2 + \sin x}$.
>
> **A.** The domain is $\mathbb{R}$, since $2 + \sin x \ge 1$.
>
> **B.** The $y$-intercept is $f(0) = \frac12$. The $x$-intercepts occur where $\cos x = 0$: $x = \frac{\pi}{2} + n\pi$, $n$ an integer.
>
> **C.** $f$ is neither even nor odd, but $f(x + 2\pi) = f(x)$ for all $x$, so $f$ is periodic with period $2\pi$. We consider only $0 \le x \le 2\pi$ and extend by translation in H.
>
> **D.** No asymptotes: $f$ is continuous everywhere and periodic.
>
> **E.**
>
> $$
> f'(x) = \frac{(2 + \sin x)(-\sin x) - \cos x\,(\cos x)}{(2 + \sin x)^2} = \frac{-2\sin x - (\sin^2 x + \cos^2 x)}{(2 + \sin x)^2} = -\frac{2\sin x + 1}{(2 + \sin x)^2} .
> $$
>
> The denominator is positive, so $f'(x) > 0 \iff 2\sin x + 1 < 0 \iff \sin x < -\frac12 \iff 7\pi/6 < x < 11\pi/6$ (on $[0, 2\pi]$). So $f$ is increasing on $(7\pi/6, 11\pi/6)$ and decreasing on $(0, 7\pi/6)$ and $(11\pi/6, 2\pi)$.
>
> **F.** By E and the First Derivative Test, the local minimum value is
>
> $$
> f(7\pi/6) = \frac{-\sqrt3/2}{2 - 1/2} = -\frac{1}{\sqrt3}
> $$
>
> and the local maximum value is $f(11\pi/6) = \dfrac{\sqrt3/2}{2 - 1/2} = \dfrac{1}{\sqrt3}$.
>
> **G.** Using the Quotient Rule again and simplifying,
>
> $$
> f''(x) = -\frac{2\cos x\,(1 - \sin x)}{(2 + \sin x)^3} .
> $$
>
> Because $(2 + \sin x)^3 > 0$ and $1 - \sin x \ge 0$ for all $x$, $f''(x) > 0$ when $\cos x < 0$, that is, $\pi/2 < x < 3\pi/2$, and $f''(x) < 0$ on $(0, \pi/2)$ and $(3\pi/2, 2\pi)$. So $f$ is concave upward on $(\pi/2, 3\pi/2)$ and concave downward on $(0, \pi/2)$ and $(3\pi/2, 2\pi)$. The inflection points are $(\pi/2, 0)$ and $(3\pi/2, 0)$.
>
> **H.** On $[0, 2\pi]$ the curve starts at $(0, \frac12)$, falls through the inflection point $(\pi/2, 0)$ to the minimum $(7\pi/6, -1/\sqrt3)$, rises through the inflection point $(3\pi/2, 0)$ to the maximum $(11\pi/6, 1/\sqrt3)$, and returns to $\frac12$ at $2\pi$. Repeating this piece with period $2\pi$ gives the whole graph.
>
> *Stewart: Example 4.5.4*

^ex-32-3

## Slant Asymptotes

> [!definition] Definition §32.2: Slant Asymptote
> If
>
> $$
> \lim_{x \to \infty} [f(x) - (mx + b)] = 0 ,
> $$
>
> where $m \ne 0$, then the line $y = mx + b$ is called a **slant asymptote** of the curve $y = f(x)$: the vertical distance between the curve and the line approaches $0$. The same applies with $x \to -\infty$.
>
> For rational functions, slant asymptotes occur when the degree of the numerator is one more than the degree of the denominator, and the asymptote is found by long division.
>
> *Stewart: 4.5 (text)*

^def-32-2

> [!example] Example §32.4: A Slant Asymptote
> Sketch the graph of $f(x) = \dfrac{x^3}{x^2 + 1}$.
>
> **A.** The domain is $\mathbb{R}$. **B.** The $x$- and $y$-intercepts are both $0$. **C.** $f(-x) = -f(x)$: $f$ is odd, and its graph is symmetric about the origin.
>
> **D.** $x^2 + 1$ is never $0$, so there is no vertical asymptote. Since $f(x) \to \infty$ as $x \to \infty$ and $f(x) \to -\infty$ as $x \to -\infty$, there is no horizontal asymptote. But long division gives
>
> $$
> f(x) = \frac{x^3}{x^2 + 1} = x - \frac{x}{x^2 + 1} ,
> $$
>
> which suggests the line $y = x$. Indeed,
>
> $$
> f(x) - x = -\frac{x}{x^2 + 1} = -\frac{1/x}{1 + 1/x^2} \to 0 \qquad\text{as } x \to \pm\infty ,
> $$
>
> so $y = x$ is a slant asymptote.
>
> **E.**
>
> $$
> f'(x) = \frac{(x^2 + 1)(3x^2) - x^3 \cdot 2x}{(x^2 + 1)^2} = \frac{x^2(x^2 + 3)}{(x^2 + 1)^2} .
> $$
>
> Since $f'(x) > 0$ for all $x$ except $0$, $f$ is increasing on $(-\infty, \infty)$.
>
> **F.** $f'(0) = 0$, but $f'$ does not change sign at $0$, so there is no local maximum or minimum.
>
> **G.**
>
> $$
> f''(x) = \frac{(x^2 + 1)^2(4x^3 + 6x) - (x^4 + 3x^2)\cdot 2(x^2 + 1)\cdot 2x}{(x^2 + 1)^4} = \frac{2x(3 - x^2)}{(x^2 + 1)^3} .
> $$
>
> $f''(x) = 0$ when $x = 0$ or $x = \pm\sqrt3$:
>
> | interval | $x$ | $3 - x^2$ | $(x^2 + 1)^3$ | $f''(x)$ | $f$ |
> |---|---|---|---|---|---|
> | $x < -\sqrt3$ | $-$ | $-$ | $+$ | $+$ | CU on $(-\infty, -\sqrt3)$ |
> | $-\sqrt3 < x < 0$ | $-$ | $+$ | $+$ | $-$ | CD on $(-\sqrt3, 0)$ |
> | $0 < x < \sqrt3$ | $+$ | $+$ | $+$ | $+$ | CU on $(0, \sqrt3)$ |
> | $x > \sqrt3$ | $+$ | $-$ | $+$ | $-$ | CD on $(\sqrt3, \infty)$ |
>
> The points of inflection are $(-\sqrt3, -\frac34\sqrt3)$, $(0, 0)$ and $(\sqrt3, \frac34\sqrt3)$; for instance $f(\sqrt3) = \frac{3\sqrt3}{3 + 1} = \frac34\sqrt3$.
>
> **H.** See the figure.
>
> *Stewart: Example 4.5.6*

^ex-32-4

![[m233-29-2.svg]]
*[[§32 Summary of Curve Sketching#^ex-32-4|Example §32.4]]: $y = x^3/(x^2 + 1)$ and its slant asymptote $y = x$ (dashed). The curve is increasing everywhere, with a horizontal tangent at the origin, which is one of its three inflection points (red). For $x > 0$ it lies below the asymptote, since $f(x) - x = -x/(x^2 + 1) < 0$; for $x < 0$ it lies above.*
