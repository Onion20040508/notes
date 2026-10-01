---
type: section
subject: "[[Calculus]]"
chapter: 7
section: 49
stewart: "7.6"
aliases: ["Stewart 7.6"]
tags: [calculus]
---
← [[§48 Strategy for Integration]] · ↑ [[· 7 Techniques of Integration]] · [[§50 Approximate Integration]] →

*Stewart, Section 7.6.*

Tables of integrals list antiderivatives by the form of the integrand; Stewart's has 120 entries (Reference Pages 6–10), and larger tables have thousands. An integral rarely occurs exactly in a listed form, so using a table means first transforming the integral with a substitution, by completing the square, or with a reduction formula, which is the same skill as in [[§48 Strategy for Integration#^rem-48-1|Remark: Method — Strategy for Integration]]. Computer algebra systems do the same pattern matching automatically. Neither can find an elementary antiderivative where none exists ([[§48 Strategy for Integration#^thm-48-2|Theorem §48.2]]).

## Tables of Integrals

The entries used below are typical. Each one is proved by differentiating the right side, or derived by the methods of this chapter.

> [!theorem] Proposition §49.1: Reduction Formulas for a Power Times Sine or Cosine
> For $n \ge 1$,
>
> $$
> \int u^n \sin u\,du = -u^n \cos u + n \int u^{n-1} \cos u\,du , \qquad \int u^n \cos u\,du = u^n \sin u - n \int u^{n-1} \sin u\,du ,
> $$
>
> and in particular $\displaystyle\int u \sin u\,du = \sin u - u\cos u + C$.
>
> *Stewart: 7.6 (Table of Integrals, entries 84, 85 and 82)*

^prop-49-1

> [!proof]+ Proof
> In the first formula integrate by parts ([[§44 Integration by Parts#^thm-44-1|Theorem §44.1]]) with $U = u^n$, $dV = \sin u\,du$, so $dU = nu^{n-1}\,du$ and $V = -\cos u$: the result is $-u^n\cos u - \int (-\cos u)\,nu^{n-1}\,du$. In the second, $U = u^n$, $dV = \cos u\,du$, $V = \sin u$, giving $u^n\sin u - \int \sin u \cdot nu^{n-1}\,du$. Entry 82 is the first formula with $n = 1$, as in [[§44 Integration by Parts#^ex-44-1|Example §44.1]].

^pf-49-1

*Uses:* [[§44 Integration by Parts#^thm-44-1|§44.1]]

> [!theorem] Proposition §49.2: Three Table Entries
> For $a > 0$,
>
> $$
> \begin{aligned}
> &(21)\quad \int \sqrt{a^2 + u^2}\,du = \frac{u}{2}\sqrt{a^2 + u^2} + \frac{a^2}{2}\ln\big(u + \sqrt{a^2 + u^2}\big) + C , \\
> &(34)\quad \int \frac{u^2}{\sqrt{a^2 - u^2}}\,du = -\frac{u}{2}\sqrt{a^2 - u^2} + \frac{a^2}{2}\sin^{-1}\Big(\frac{u}{a}\Big) + C , \\
> &(92)\quad \int u \tan^{-1} u\,du = \frac{u^2 + 1}{2}\tan^{-1} u - \frac{u}{2} + C .
> \end{aligned}
> $$
>
> *Stewart: 7.6 (Table of Integrals, entries 21, 34 and 92)*

^prop-49-2

> [!proof]- Proof
> Differentiate each right side.
>
> **(21)** Write $s = \sqrt{a^2 + u^2}$, so $s' = u/s$. Then
>
> $$
> \frac{d}{du}\Big[\frac{u s}{2} + \frac{a^2}{2}\ln(u + s)\Big] = \frac{s}{2} + \frac{u^2}{2s} + \frac{a^2}{2} \cdot \frac{1 + u/s}{u + s} = \frac{s}{2} + \frac{u^2}{2s} + \frac{a^2}{2s} = \frac{s}{2} + \frac{u^2 + a^2}{2s} = \frac{s}{2} + \frac{s}{2} = s .
> $$
>
> **(34)** Write $r = \sqrt{a^2 - u^2}$, so $r' = -u/r$. Then
>
> $$
> \frac{d}{du}\Big[-\frac{u r}{2} + \frac{a^2}{2}\sin^{-1}\frac{u}{a}\Big] = -\frac{r}{2} + \frac{u^2}{2r} + \frac{a^2}{2r} = \frac{-r^2 + u^2 + a^2}{2r} = \frac{2u^2}{2r} = \frac{u^2}{\sqrt{a^2 - u^2}} ,
> $$
>
> using Formula 18 of [[§48 Strategy for Integration#^thm-48-1|Theorem §48.1]] for the derivative of $\sin^{-1}(u/a)$. (It can also be derived with $u = a\sin\theta$, [[§46 Trigonometric Substitution#^rem-46-1|Remark: Method — Trigonometric Substitution]].)
>
> **(92)**
>
> $$
> \frac{d}{du}\Big[\frac{u^2 + 1}{2}\tan^{-1} u - \frac{u}{2}\Big] = u\tan^{-1} u + \frac{u^2 + 1}{2} \cdot \frac{1}{1 + u^2} - \frac12 = u\tan^{-1} u .
> $$
>
> (It can also be derived by parts with $dv = u\,du$.)

^pf-49-2

*Uses:* [[§48 Strategy for Integration#^thm-48-1|§48.1]] (Formula 18), [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^cor-19-4|§19.4]], [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-8|§19.8]]

> [!remark] Remark: Method — Using a Table of Integrals
> 1. Identify the family the integrand belongs to (forms involving $\sqrt{a^2 - u^2}$, trigonometric forms, inverse trigonometric forms, …) and find the closest entry.
> 2. Transform the integral to match it: a linear substitution such as $u = 2x$ (remembering to replace $dx$ by $du/2$), completing the square for $\sqrt{ax^2 + bx + c}$, splitting the integral into pieces, or algebra.
> 3. If the entry is a reduction formula, apply it repeatedly until a listed integral remains.
> 4. Read off the constants (such as $a^2 = 5$) and substitute back.
>
> **Technology.** A computer algebra system works the same way, but its answer may omit the constant of integration and the absolute value signs (for example $\frac13\ln(3x - 2)$ for $\int \frac{dx}{3x - 2}$, valid only for $x > \frac23$). It may also come in a different but equivalent form, such as $\sinh^{-1}$ in place of $\ln$, which differ by a constant, or a fully expanded polynomial where a hand substitution gives $\frac1{18}(x^2 + 5)^9$.

^rem-49-1

## Examples

> [!example] Example §49.1: A Volume by Shells
> The region bounded by $y = \tan^{-1} x$, $y = 0$ and $x = 1$ is rotated about the $y$-axis. Find the volume of the solid.
>
> By cylindrical shells ([[§41 Volumes by Cylindrical Shells#^thm-41-2|Theorem §41.2]]), $V = \int_0^1 2\pi x \tan^{-1} x\,dx$. Entry 92 (Proposition §49.2) gives
>
> $$
> V = 2\pi\Big[\frac{x^2 + 1}{2}\tan^{-1} x - \frac{x}{2}\Big]_0^1 = \pi\Big[(x^2 + 1)\tan^{-1} x - x\Big]_0^1 = \pi(2\tan^{-1} 1 - 1) = \pi\Big(\frac{\pi}{2} - 1\Big) = \tfrac12 \pi^2 - \pi .
> $$
>
> *Stewart: Example 7.6.1*

^ex-49-1

> [!example] Example §49.2: A Substitution to Match an Entry
> Use the table to find $\displaystyle\int \frac{x^2}{\sqrt{5 - 4x^2}}\,dx$.
>
> The closest entry is 34, with $\sqrt{a^2 - u^2}$. Substitute $u = 2x$, so $x = u/2$ and $dx = du/2$:
>
> $$
> \int \frac{x^2}{\sqrt{5 - 4x^2}}\,dx = \int \frac{(u/2)^2}{\sqrt{5 - u^2}}\,\frac{du}{2} = \frac18 \int \frac{u^2}{\sqrt{5 - u^2}}\,du .
> $$
>
> Entry 34 with $a^2 = 5$ ($a = \sqrt5$):
>
> $$
> \frac18\Big(-\frac{u}{2}\sqrt{5 - u^2} + \frac52 \sin^{-1}\frac{u}{\sqrt5}\Big) + C = -\frac{x}{8}\sqrt{5 - 4x^2} + \frac{5}{16}\sin^{-1}\Big(\frac{2x}{\sqrt5}\Big) + C .
> $$
>
> *Stewart: Example 7.6.2*

^ex-49-2

> [!example] Example §49.3: Reduction Formulas from the Table
> Use the table to evaluate $\displaystyle\int x^3 \sin x\,dx$.
>
> No entry contains $u^3\sin u$ explicitly, but the reduction formula 84 (Proposition §49.1) with $n = 3$ gives
>
> $$
> \int x^3 \sin x\,dx = -x^3 \cos x + 3\int x^2 \cos x\,dx .
> $$
>
> Entry 85 with $n = 2$, followed by entry 82:
>
> $$
> \int x^2 \cos x\,dx = x^2 \sin x - 2\int x \sin x\,dx = x^2 \sin x - 2(\sin x - x\cos x) + K .
> $$
>
> Combining, with $C = 3K$,
>
> $$
> \int x^3 \sin x\,dx = -x^3 \cos x + 3x^2 \sin x + 6x\cos x - 6\sin x + C .
> $$
>
> *Stewart: Example 7.6.3*

^ex-49-3

> [!example] Example §49.4: Completing the Square to Match an Entry
> Use the table to find $\displaystyle\int x\sqrt{x^2 + 2x + 4}\,dx$.
>
> The table has forms with $\sqrt{a^2 + x^2}$, $\sqrt{a^2 - x^2}$ and $\sqrt{x^2 - a^2}$, but not $\sqrt{ax^2 + bx + c}$. Complete the square: $x^2 + 2x + 4 = (x + 1)^2 + 3$. With $u = x + 1$ ($x = u - 1$),
>
> $$
> \int x\sqrt{x^2 + 2x + 4}\,dx = \int (u - 1)\sqrt{u^2 + 3}\,du = \int u\sqrt{u^2 + 3}\,du - \int \sqrt{u^2 + 3}\,du .
> $$
>
> For the first, substitute $t = u^2 + 3$: $\int u\sqrt{u^2 + 3}\,du = \frac12 \int \sqrt{t}\,dt = \frac12 \cdot \frac23 t^{3/2} = \frac13 (u^2 + 3)^{3/2}$. For the second, entry 21 with $a = \sqrt3$: $\int \sqrt{u^2 + 3}\,du = \frac{u}{2}\sqrt{u^2 + 3} + \frac32 \ln\big(u + \sqrt{u^2 + 3}\big)$. Therefore
>
> $$
> \int x\sqrt{x^2 + 2x + 4}\,dx = \tfrac13 (x^2 + 2x + 4)^{3/2} - \frac{x + 1}{2}\sqrt{x^2 + 2x + 4} - \tfrac32 \ln\big(x + 1 + \sqrt{x^2 + 2x + 4}\big) + C .
> $$
>
> A computer algebra system may return $-\frac32 \sinh^{-1}\big(\frac{\sqrt3}{3}(1 + x)\big)$ for the last term. Since $\sinh^{-1} y = \ln\big(y + \sqrt{y^2 + 1}\big)$ ([[§24 Hyperbolic Functions#^thm-24-3|Theorem §24.3]]), this is $\ln\big(x + 1 + \sqrt{x^2 + 2x + 4}\big) + \ln\frac{1}{\sqrt3}$, the same up to a constant.
>
> *Stewart: Examples 7.6.4 and 7.6.5*

^ex-49-4
