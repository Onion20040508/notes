---
type: section
subject: "[[Calculus]]"
chapter: 4
section: 30
stewart: "4.6"
aliases: ["Stewart 4.6"]
tags: [calculus]
---
← [[§29 Summary of Curve Sketching]] · ↑ [[· 4 Applications of Differentiation]] · [[§31 Optimization Problems]] →

*Stewart, Section 4.6.*

In [[§29 Summary of Curve Sketching|§29]] the graph was the end product of a calculation. Here the order is reversed: one starts from a machine-drawn graph and uses calculus to check it and to find what it hides. A single viewing window often cannot show all the features of a function at once: some live on a tiny vertical scale near the origin, others far out. The derivatives say where to look, and they give exact values where the graph only gives estimates. The section has no new theorems; its content is the interplay, shown in the examples below, and the study of *families* of functions depending on a parameter.

> [!remark] Remark: Method — Graphing with Calculus and Technology
> 1. Graph $f$ in a first window; then let the formula guide the choice of further windows. Look for vertical asymptotes (zeros of denominators), horizontal or slant asymptotes (end behavior), and the behavior at $x$-intercepts (a factor $(x - r)^k$ with $k$ even touches the axis without crossing; with $k \ge 3$ odd it crosses with a horizontal tangent).
> 2. Compute $f'$ and $f''$. Their sign changes locate the extreme values and inflection points. Where they cannot be found exactly, graph $f'$ and $f''$ (which magnifies small features of $f$) or solve numerically, for instance by Newton's method ([[§32 Newton's Method#^def-32-1|Def. §32.1]]).
> 3. Zoom in on each critical number and inflection point, and zoom out to see the end behavior. Several windows may be needed to show everything.
> 4. For a family of functions $f_c$, find what all members have in common, then the values of $c$ at which the qualitative picture changes (number of asymptotes, critical numbers or inflection points), and how the features move as $c$ varies.

^rem-30-1

> [!example] Example §30.1: Features Hidden at Two Scales
> Graph $f(x) = 2x^6 + 3x^5 + 3x^3 - 2x^2$ and use $f'$ and $f''$ to find all maximum and minimum points and intervals of concavity.
>
> In the window $[-5, 5]$ by $[-1000, 41{,}000]$ the graph shows only the end behavior, which is like that of $y = 2x^6$. In $[-3, 2]$ by $[-50, 100]$ there is an absolute minimum of about $-15.33$ near $x \approx -1.62$, and the graph looks flat near the origin. Calculus shows what is going on there:
>
> $$
> f'(x) = 12x^5 + 15x^4 + 9x^2 - 4x = x\,(12x^4 + 15x^3 + 9x - 4), \qquad f''(x) = 60x^4 + 60x^3 + 18x - 4 .
> $$
>
> **Critical numbers.** $x = 0$ is one. The quartic factor has two real zeros, $x \approx -1.62$ and $x \approx 0.35$ (read from the graph of $f'$, or found by Newton's method). $f'$ changes from negative to positive at $-1.62$, from positive to negative at $0$, and from negative to positive at $0.35$. So by the [[§27 What Derivatives Tell Us About the Shape of a Graph#^thm-27-2|First Derivative Test]]:
> - an absolute minimum $f(-1.62) \approx -15.33$;
> - a local maximum $f(0) = 0$ (confirmed by the [[§27 What Derivatives Tell Us About the Shape of a Graph#^thm-27-4|Second Derivative Test]], since $f'(0) = 0$ and $f''(0) = -4 < 0$);
> - a local minimum $f(0.35) \approx -0.1$.
>
> The last two were invisible in the second window; zooming in to $[-1, 1]$ by $[-1, 1]$ shows them.
>
> **Concavity.** $f''$ changes from positive to negative at $x \approx -1.23$ and from negative to positive at $x \approx 0.19$. So $f$ is concave upward on $(-\infty, -1.23)$ and $(0.19, \infty)$ and concave downward on $(-1.23, 0.19)$, with inflection points about $(-1.23, -10.18)$ and $(0.19, -0.05)$.
>
> No single graph shows all these features; the windows $[-3, 2] \times [-50, 100]$ and $[-1, 1] \times [-1, 1]$ together give an accurate picture.
>
> *Stewart: Example 4.6.1*

^ex-30-1

> [!example] Example §30.2: Exact Values for a Rational Function
> Draw the graph of $f(x) = \dfrac{x^2 + 7x + 3}{x^2}$ showing all its important features, and find the local extreme values and intervals of concavity exactly.
>
> Automatic scaling produces a useless graph (the values near $0$ are huge). The formula tells where to look.
>
> **Asymptotes and intercepts.** As $x \to 0$ the numerator tends to $3 > 0$ and $x^2 \to 0^+$, so $\lim_{x \to 0} f(x) = \infty$: the $y$-axis is a vertical asymptote. Writing $f(x) = 1 + \dfrac7x + \dfrac{3}{x^2}$ shows $\lim_{x \to \pm\infty} f(x) = 1$: $y = 1$ is a horizontal asymptote. The $x$-intercepts solve $x^2 + 7x + 3 = 0$: $x = \frac{-7 \pm \sqrt{37}}{2} \approx -0.46,\ -6.54$.
>
> **First derivative.**
>
> $$
> f'(x) = -\frac{7}{x^2} - \frac{6}{x^3} = -\frac{7x + 6}{x^3} .
> $$
>
> $f'(x) > 0$ when $-\frac67 < x < 0$, and $f'(x) < 0$ when $x < -\frac67$ and when $x > 0$. So $f$ decreases on $(-\infty, -\frac67)$, increases on $(-\frac67, 0)$, and decreases on $(0, \infty)$. The minimum value is
>
> $$
> f\big(-\tfrac67\big) = 1 - \frac{49}{6} + \frac{3 \cdot 49}{36} = \frac{12 - 98 + 49}{12} = -\frac{37}{12} \approx -3.08 ,
> $$
>
> and it is the absolute minimum, since $f$ decreases toward it from the left and increases from it up to the asymptote.
>
> **Second derivative.**
>
> $$
> f''(x) = \frac{14}{x^3} + \frac{18}{x^4} = \frac{2(7x + 9)}{x^4} .
> $$
>
> $f''(x) > 0$ when $x > -\frac97$ ($x \ne 0$) and $f''(x) < 0$ when $x < -\frac97$. So $f$ is concave upward on $(-\frac97, 0)$ and $(0, \infty)$ and concave downward on $(-\infty, -\frac97)$. The inflection point is
>
> $$
> \Big(-\frac97,\ 1 - \frac{49}{9} + \frac{3 \cdot 49}{81}\Big) = \Big(-\frac97,\ \frac{27 - 147 + 49}{27}\Big) = \Big(-\frac97,\ -\frac{71}{27}\Big) .
> $$
>
> A window such as $[-20, 20]$ by $[-5, 10]$ shows all the major features.
>
> *Stewart: Example 4.6.2*

^ex-30-2

![[m233-30-1.svg]]
*[[§30 Graphing with Calculus and Technology#^ex-30-2|Example §30.2]]: $y = (x^2 + 7x + 3)/x^2$, with its asymptotes, the $y$-axis and the line $y = 1$ (dashed). The exact features from calculus: the absolute minimum $(-\frac67, -\frac{37}{12})$ (blue) and the inflection point $(-\frac97, -\frac{71}{27})$ (red), very close together. On the left the curve approaches $y = 1$ from below, on the right from above.*

> [!example] Example §30.3: Letting the Formula Guide the Zooming
> Graph $f(x) = \dfrac{x^2(x + 1)^3}{(x - 2)^2(x - 4)^4}$.
>
> **Before any derivative.** Because of the factors $(x - 2)^2$ and $(x - 4)^4$ we expect vertical asymptotes at $2$ and $4$; the numerator is positive near both and the denominator is positive on both sides, so
>
> $$
> \lim_{x \to 2} f(x) = \infty, \qquad \lim_{x \to 4} f(x) = \infty .
> $$
>
> Dividing numerator and denominator by $x^6$,
>
> $$
> f(x) = \frac{\dfrac{x^2}{x^3}\cdot\dfrac{(x + 1)^3}{x^3}}{\dfrac{(x - 2)^2}{x^2}\cdot\dfrac{(x - 4)^4}{x^4}} = \frac{\dfrac1x\Big(1 + \dfrac1x\Big)^3}{\Big(1 - \dfrac2x\Big)^2\Big(1 - \dfrac4x\Big)^4} \to 0 \qquad\text{as } x \to \pm\infty ,
> $$
>
> so the $x$-axis is a horizontal asymptote. Near the $x$-intercepts: $x^2 \ge 0$, so $f$ does not change sign at $0$ and the graph touches the axis there without crossing (so $f(0) = 0$ is a local minimum, as $f \ge 0$ near $0$). The factor $(x + 1)^3$ changes sign at $-1$ and its derivative vanishes there, so the graph crosses the axis at $-1$ with a horizontal tangent. Hence: negative for $x < -1$, positive for $x > -1$ ($x \ne 0, 2, 4$), with the shape forced by these facts.
>
> **Zooming.** Guided by this, zooming in and out shows an absolute minimum of about $-0.02$ at $x \approx -20$ (far out, on a tiny scale), a local maximum of about $0.00002$ at $x \approx -0.3$, and a local minimum of about $211$ at $x \approx 2.5$, between the asymptotes. Three different windows are needed; only a hand-drawn sketch, with exaggerations, shows all features at once. (Computing $f''$ by hand to locate the inflection points is an unreasonable chore; a computer algebra system does it easily.)
>
> *Stewart: Example 4.6.3*

^ex-30-3

> [!example] Example §30.4: A Family of Functions
> How does the graph of $f(x) = \dfrac{1}{x^2 + 2x + c}$ vary as $c$ varies?
>
> **Common features.** $\lim_{x \to \pm\infty} \frac{1}{x^2 + 2x + c} = 0$ for every $c$, so all members have the $x$-axis as a horizontal asymptote.
>
> **Vertical asymptotes.** They occur where $x^2 + 2x + c = 0$, that is, $x = -1 \pm \sqrt{1 - c}$.
> - $c > 1$: no vertical asymptote.
> - $c = 1$: a single vertical asymptote $x = -1$, since $\lim_{x \to -1} \frac{1}{(x + 1)^2} = \infty$.
> - $c < 1$: two vertical asymptotes $x = -1 \pm \sqrt{1 - c}$, a distance $2\sqrt{1 - c}$ apart.
>
> **First derivative.**
>
> $$
> f'(x) = -\frac{2x + 2}{(x^2 + 2x + c)^2} .
> $$
>
> So $f'(x) = 0$ when $x = -1$ (if $c \ne 1$), $f'(x) > 0$ when $x < -1$ and $f'(x) < 0$ when $x > -1$. For $c \ge 1$, $f$ increases on $(-\infty, -1)$ and decreases on $(-1, \infty)$. For $c > 1$ there is an absolute maximum $f(-1) = \frac{1}{c - 1}$. For $c < 1$, $f(-1) = \frac{1}{c - 1} < 0$ is a local maximum, and the intervals of increase and decrease are interrupted by the vertical asymptotes.
>
> **Second derivative.**
>
> $$
> f''(x) = \frac{2(3x^2 + 6x + 4 - c)}{(x^2 + 2x + c)^3} .
> $$
>
> The numerator is $2\big(3(x + 1)^2 + 1 - c\big)$. For $c \le 1$ it is positive wherever $f$ is defined, and $f''$ changes sign only at the vertical asymptotes, so there is no inflection point. For $c > 1$ the denominator is positive and the numerator changes sign where $3(x + 1)^2 = c - 1$, so the inflection points are at
>
> $$
> x = -1 \pm \sqrt{\frac{c - 1}{3}} .
> $$
>
> **How the picture changes.** As $c$ decreases through $1$, the graph passes from no vertical asymptote ($c > 1$, a single bump) to one ($c = 1$) to two ($c < 1$). As $c$ increases from $1$, the maximum point $\big(-1, \frac{1}{c - 1}\big)$ becomes lower, since $\frac{1}{c - 1} \to 0$ as $c \to \infty$, and the inflection points spread out. As $c$ decreases from $1$, the vertical asymptotes move apart (their distance $2\sqrt{1 - c} \to \infty$ as $c \to -\infty$) and the local maximum $\frac{1}{c - 1}$ rises toward the $x$-axis.
>
> *Stewart: Example 4.6.5*

^ex-30-4

Stewart's Example 4.6.4, $f(x) = \sin(x + \sin 2x)$, is handled the same way, but its critical numbers and inflection points can only be estimated from the graphs of $f'$ and $f''$.
