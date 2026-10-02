---
type: section
subject: "[[Complex Variables]]"
chapter: 5
section: 65
bc: "65"
aliases: ["B&C 65"]
tags: [complex-variables, math342]
---
← [[§64 Examples (Proof of Taylor's Theorem)]] · ↑ [[· 5 Series]] · [[§66 Laurent Series]] →

*Brown–Churchill, Section 65 · MAT 342 HW 9.*

If $f$ fails to be analytic at $z_0$, Taylor's theorem does not apply there, but $f(z)$ can often still be written as a series in both positive and negative powers of $z - z_0$, valid in a punctured disk or a ring around $z_0$. This section gets used to such series before their general theory, Laurent's theorem ([[§66 Laurent Series|§66]]), is stated. All the examples use only the six Maclaurin series of [[§64 Examples (Proof of Taylor's Theorem)#^prop-64-1|Proposition §64.1]], combined with multiplication by a power of $z - z_0$ or with the substitution $z \mapsto 1/z$. Terms such as $1/z^3 = z^{-3}$ and $1/z = z^{-1}$ are called **negative powers** of $z$. Whether the negative or the positive powers are written first is immaterial.

The examples rely on two facts about convergent series: a convergent series may be multiplied term by term by a constant, here $1/z^k$ for a fixed $z \ne 0$ ([[§61 Convergence of Series#^prop-61-4|Proposition §61.4]]), and it may be reindexed. In each case the condition of validity is inherited from the Maclaurin series used, with the points where the factor $1/(z - z_0)^k$ is undefined removed. Laurent's theorem later explains why each region is a punctured disk or an annulus ([[§68 Examples (Proof of Laurent's Theorem)|§68]]).

> [!example] Example §65.1: Multiplying a Maclaurin Series by a Negative Power
> **(a) $e^{-z}/z^2$.** From $e^z = 1 + \frac{z}{1!} + \frac{z^2}{2!} + \frac{z^3}{3!} + \frac{z^4}{4!} + \cdots$ $(|z| < \infty)$, with $z$ replaced by $-z$ and then multiplied by $1/z^2$,
>
> $$
> \frac{e^{-z}}{z^2} = \frac{1}{z^2}\Big(1 - \frac{z}{1!} + \frac{z^2}{2!} - \frac{z^3}{3!} + \frac{z^4}{4!} - \cdots\Big) = \frac{1}{z^2} - \frac1z + \frac{1}{2!} - \frac{z}{3!} + \frac{z^2}{4!} - \cdots
> $$
>
> when $0 < |z| < \infty$.
>
> **(b) $z^3\cosh(1/z)$.** From $\cosh z = \sum_{n=0}^{\infty}\frac{z^{2n}}{(2n)!}$ $(|z| < \infty)$, with $z$ replaced by $1/z$ (allowed for every $z \ne 0$), it follows that when $0 < |z| < \infty$,
>
> $$
> z^3\cosh\Big(\frac1z\Big) = z^3\sum_{n=0}^{\infty}\frac{1}{(2n)!\,z^{2n}} = \sum_{n=0}^{\infty}\frac{1}{(2n)!\,z^{2n-3}} .
> $$
>
> The exponent $-(2n - 3)$ is positive when $n$ is $0$ or $1$ and negative when $n \ge 2$. Separating those two terms,
>
> $$
> z^3\cosh\Big(\frac1z\Big) = z^3 + \frac z2 + \sum_{n=2}^{\infty}\frac{1}{(2n)!\,z^{2n-3}} \qquad (0 < |z| < \infty) ,
> $$
>
> and, anticipating the standard form of [[§66 Laurent Series|§66]], replacing $n$ by $n + 1$ in the last sum,
>
> $$
> z^3\cosh\Big(\frac1z\Big) = \frac z2 + z^3 + \sum_{n=1}^{\infty}\frac{1}{(2n + 2)!}\cdot\frac{1}{z^{2n-1}} = \frac z2 + z^3 + \frac{1}{24z} + \frac{1}{720z^3} + \cdots \qquad (0 < |z| < \infty) .
> $$
>
> *(B&C prints $\cos(1/z)$ on the left of this last equation, p. 194; the function is $\cosh(1/z)$ throughout.)* Here the positive powers come first, while in (a) the negative powers do.
>
> *B&C: Sec. 65, Examples 1 and 2*

^ex-65-1

> [!example] Example §65.2: A Rational Function with a Pole at the Center
> **Problem.** Expand
>
> $$
> f(z) = \frac{1 + 2z^2}{z^3 + z^5}
> $$
>
> into a series involving powers of $z$.
>
> **Rewrite.** Since $1 + 2z^2 = 2(1 + z^2) - 1$,
>
> $$
> f(z) = \frac{1}{z^3}\cdot\frac{2(1 + z^2) - 1}{1 + z^2} = \frac{1}{z^3}\Big(2 - \frac{1}{1 + z^2}\Big) .
> $$
>
> A Maclaurin series is impossible, since $f$ is not analytic at $z = 0$. But replacing $z$ by $-z^2$ in the geometric series $\frac{1}{1 - z} = 1 + z + z^2 + \cdots$ $(|z| < 1)$ gives
>
> $$
> \frac{1}{1 + z^2} = 1 - z^2 + z^4 - z^6 + z^8 - \cdots \qquad (|z| < 1) ,
> $$
>
> because $|-z^2| < 1$ exactly when $|z| < 1$. So when $0 < |z| < 1$,
>
> $$
> f(z) = \frac{1}{z^3}\big(2 - 1 + z^2 - z^4 + z^6 - z^8 + \cdots\big) = \frac{1}{z^3} + \frac1z - z + z^3 - z^5 + \cdots .
> $$
>
> The outer radius $1$ is the distance from $0$ to the singular points $\pm i$.
>
> *B&C: Sec. 65, Example 3*

^ex-65-2

> [!example] Example §65.3: Expanding About z₀ = −1
> **Problem.** Expand $\dfrac{e^z}{(z + 1)^2}$ in powers of $z + 1$.
>
> Start with $e^z = \sum_{n=0}^{\infty}z^n/n!$ $(|z| < \infty)$ and replace $z$ by $z + 1$:
>
> $$
> e^{z+1} = \sum_{n=0}^{\infty}\frac{(z + 1)^n}{n!} \qquad (|z + 1| < \infty) .
> $$
>
> Dividing through by $e(z + 1)^2$ (allowed when $z \ne -1$) gives $\dfrac{e^z}{(z + 1)^2} = \sum_{n=0}^{\infty}\dfrac{(z + 1)^{n-2}}{n!\,e}$, that is,
>
> $$
> \frac{e^z}{(z + 1)^2} = \frac1e\Big[\frac{1}{(z + 1)^2} + \frac{1}{z + 1} + \sum_{n=2}^{\infty}\frac{(z + 1)^{n-2}}{n!}\Big] = \frac1e\Big[\sum_{n=0}^{\infty}\frac{(z + 1)^n}{(n + 2)!} + \frac{1}{z + 1} + \frac{1}{(z + 1)^2}\Big] \qquad (0 < |z + 1| < \infty) .
> $$
>
> (The first terms of the bracket are $\frac{1}{(z + 1)^2} + \frac{1}{z + 1} + \frac12 + \frac{z + 1}{6} + \cdots$, confirmed with sympy.)
>
> *B&C: Sec. 65, Example 4*

^ex-65-3

> [!example] Example §65.4: A Ring Bounded by Two Singular Points
> **Problem.** Show that when $0 < |z| < 4$,
>
> $$
> \frac{1}{4z - z^2} = \frac{1}{4z} + \sum_{n=0}^{\infty}\frac{z^n}{4^{n+2}} .
> $$
>
> Factor out the singular factor at the center:
>
> $$
> \frac{1}{4z - z^2} = \frac{1}{4z}\cdot\frac{1}{1 - (z/4)} .
> $$
>
> For $0 < |z| < 4$ we have $|z/4| < 1$, so the geometric series applies:
>
> $$
> \frac{1}{4z - z^2} = \frac{1}{4z}\sum_{n=0}^{\infty}\Big(\frac z4\Big)^n = \sum_{n=0}^{\infty}\frac{z^{n-1}}{4^{n+1}} = \frac{1}{4z} + \sum_{n=1}^{\infty}\frac{z^{n-1}}{4^{n+1}} .
> $$
>
> Replacing $n$ by $n + 1$ in the last sum gives the claim: $\frac{1}{4z} + \frac{1}{16} + \frac{z}{64} + \frac{z^2}{256} + \cdots$. The function is singular at $z = 0$ and $z = 4$; the ring $0 < |z| < 4$ is punctured at the first and bounded by the second.
>
> *B&C: Sec. 65, Exercise 11; Source: 342 HW 9*

^ex-65-4
