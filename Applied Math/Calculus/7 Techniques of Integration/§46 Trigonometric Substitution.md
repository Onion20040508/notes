---
type: section
subject: "[[Calculus]]"
chapter: 7
section: 46
stewart: "7.3"
aliases: ["Stewart 7.3"]
tags: [calculus]
---
← [[§45 Trigonometric Integrals]] · ↑ [[· 7 Techniques of Integration]] · [[§47 Integration of Rational Functions by Partial Fractions]] →

*Stewart, Section 7.3.*

Integrals containing $\sqrt{a^2 - x^2}$, $\sqrt{a^2 + x^2}$ or $\sqrt{x^2 - a^2}$ arise from circles, ellipses and hyperbolas. For $\int x\sqrt{a^2 - x^2}\,dx$ the substitution $u = a^2 - x^2$ works, but $\int \sqrt{a^2 - x^2}\,dx$ has no factor $x$ to serve as $du$. The way out is to run the Substitution Rule backwards: make the *old* variable a function of a new one, $x = a\sin\theta$, chosen so that a Pythagorean identity removes the root. What remains is a trigonometric integral ([[§45 Trigonometric Integrals|§45]]). For an indefinite integral, a right triangle translates the answer back into $x$.

## Inverse Substitution

> [!theorem] Theorem §46.1: Inverse Substitution Rule
> Let $x = g(t)$, where $g$ is differentiable and one-to-one on an interval, with inverse $t = g^{-1}(x)$. Then
>
> $$
> \int f(x)\,dx = \int f(g(t))\,g'(t)\,dt ,
> $$
>
> in the sense that if $G(t)$ is an antiderivative of $f(g(t))\,g'(t)$, then $G(g^{-1}(x))$ is an antiderivative of $f(x)$. For a definite integral, with $g(\alpha) = a$ and $g(\beta) = b$ and $f$, $g'$ continuous,
>
> $$
> \int_a^b f(x)\,dx = \int_\alpha^\beta f(g(t))\,g'(t)\,dt .
> $$
>
> *Stewart: 7.3 (text)*

^thm-46-1

> [!proof]+ Proof
> This is the Substitution Rule ([[§38 The Substitution Rule|§38]]), $\int f(g(t))\,g'(t)\,dt = \int f(u)\,du$ with $u = g(t)$, read from right to left with the letter $x$ in place of $u$. Stewart leaves it at that; here is the check. Let $F$ be an antiderivative of $f$. By the Chain Rule, $\frac{d}{dt} F(g(t)) = f(g(t))\,g'(t)$, so $G(t) = F(g(t)) + C$ for some constant $C$. Then $G(g^{-1}(x)) = F(x) + C$, an antiderivative of $f$. For the definite version, the Substitution Rule for definite integrals gives $\int_\alpha^\beta f(g(t))\,g'(t)\,dt = \int_{g(\alpha)}^{g(\beta)} f(u)\,du = \int_a^b f(x)\,dx$.

^pf-46-1

*Uses:* [[§38 The Substitution Rule|§38]], [[§17 The Chain Rule|§17]]

> [!remark]- Connections
> - Rigorous treatment of the definite version: [[§15 Multivariable Integration#^lem-15-13|452 Lemma §15.13]] (one-dimensional change of variables, with $|g'(t)|$ and the limits in increasing order), the case $n = 1$ of the change of variables formula.

The one-to-one requirement is what makes going back to $x$ possible. For $x = a\sin\theta$ it is met by restricting $\theta$ to $[-\pi/2, \pi/2]$, the interval used to define $\sin^{-1}$ ([[§5 Inverse Functions and Logarithms|§5]]).

> [!remark] Remark: Method — Trigonometric Substitution
> 1. **Choose the substitution** from the table. The restriction on $\theta$ makes the substitution one-to-one; these are the intervals used to define the inverse trigonometric functions.
>
>    | Expression | Substitution | Identity |
>    |---|---|---|
>    | $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$, $\ -\frac{\pi}{2} \le \theta \le \frac{\pi}{2}$ | $1 - \sin^2\theta = \cos^2\theta$ |
>    | $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$, $\ -\frac{\pi}{2} < \theta < \frac{\pi}{2}$ | $1 + \tan^2\theta = \sec^2\theta$ |
>    | $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$, $\ 0 \le \theta < \frac{\pi}{2}$ or $\pi \le \theta < \frac{3\pi}{2}$ | $\sec^2\theta - 1 = \tan^2\theta$ |
>
> 2. **Remove the root.** For example $\sqrt{a^2 - a^2\sin^2\theta} = a|\cos\theta| = a\cos\theta$, because $\cos\theta \ge 0$ on $[-\pi/2, \pi/2]$. On the stated intervals $\sec\theta > 0$ for the second row and $\tan\theta \ge 0$ for the third, so in each row the absolute value can be dropped.
> 3. **Replace $dx$** by $g'(\theta)\,d\theta$ (e.g. $dx = a\cos\theta\,d\theta$) and evaluate the trigonometric integral ([[§45 Trigonometric Integrals|§45]]).
> 4. **Return to $x$.** For an indefinite integral, draw a right triangle with angle $\theta$ whose sides express the substitution (figure below), and read off the other trigonometric functions of $\theta$; $\theta$ itself is $\sin^{-1}(x/a)$, $\tan^{-1}(x/a)$ or $\sec^{-1}(x/a)$. For a definite integral, change the limits instead.
> 5. **Preliminary steps.** If the radicand is $b^2 - c^2x^2$ or similar, substitute $u = cx$ first. If it is a general quadratic $ax^2 + bx + c$, complete the square first. The same substitutions help with $(a^2 \pm x^2)^{n/2}$ and $(x^2 - a^2)^{n/2}$ for any integer $n$.
> 6. **Look for something simpler first.** $\displaystyle\int \frac{x}{\sqrt{x^2 + 4}}\,dx$ could be done with $x = 2\tan\theta$, but $u = x^2 + 4$, $du = 2x\,dx$ gives $\frac12 \int u^{-1/2}\,du = \sqrt{x^2 + 4} + C$ at once (Stewart, Example 7.3.4).
>
> *Stewart: 7.3, Table of Trigonometric Substitutions*

^rem-46-1

![[m233-46-1.svg]]
*The reference triangles. Label the sides so that the substitution holds (hypotenuse $a$ and opposite side $x$ for $\sin\theta = x/a$, and so on). The Pythagorean Theorem gives the third side, which is the radical. Any other trigonometric function of $\theta$ can then be read off; for example, in the first triangle $\cot\theta = \sqrt{a^2 - x^2}/x$. The formulas read off this way hold for negative $\theta$ too, although the picture has $\theta > 0$.*

## Examples

> [!example] Example §46.1: The Sine Substitution, Indefinite
> Evaluate $\displaystyle\int \frac{\sqrt{9 - x^2}}{x^2}\,dx$.
>
> Let $x = 3\sin\theta$, $-\pi/2 \le \theta \le \pi/2$. Then $dx = 3\cos\theta\,d\theta$ and
>
> $$
> \sqrt{9 - x^2} = \sqrt{9 - 9\sin^2\theta} = \sqrt{9\cos^2\theta} = 3|\cos\theta| = 3\cos\theta ,
> $$
>
> since $\cos\theta \ge 0$ there. By Theorem §46.1,
>
> $$
> \int \frac{\sqrt{9 - x^2}}{x^2}\,dx = \int \frac{3\cos\theta}{9\sin^2\theta}\,3\cos\theta\,d\theta = \int \frac{\cos^2\theta}{\sin^2\theta}\,d\theta = \int \cot^2\theta\,d\theta = \int (\csc^2\theta - 1)\,d\theta = -\cot\theta - \theta + C .
> $$
>
> **Back to $x$.** $\sin\theta = x/3$: in a right triangle with angle $\theta$, opposite side $x$ and hypotenuse $3$, the adjacent side is $\sqrt{9 - x^2}$, so $\cot\theta = \sqrt{9 - x^2}/x$. And $\theta = \sin^{-1}(x/3)$. Therefore
>
> $$
> \int \frac{\sqrt{9 - x^2}}{x^2}\,dx = -\frac{\sqrt{9 - x^2}}{x} - \sin^{-1}\Big(\frac{x}{3}\Big) + C .
> $$
>
> (The triangle has $\theta > 0$, but $\cot\theta = \cos\theta/\sin\theta = \frac{\sqrt{9 - x^2}/3}{x/3}$ holds for $\theta < 0$ as well.)
>
> *Stewart: Example 7.3.1*

^ex-46-1

> [!example] Example §46.2: The Area of an Ellipse
> Find the area enclosed by the ellipse $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ ($a, b > 0$).
>
> Solving for $y$: $\dfrac{y^2}{b^2} = 1 - \dfrac{x^2}{a^2} = \dfrac{a^2 - x^2}{a^2}$, so $y = \pm \dfrac{b}{a}\sqrt{a^2 - x^2}$. The ellipse is symmetric in both axes, so the area $A$ is four times the area in the first quadrant, which lies under $y = \frac{b}{a}\sqrt{a^2 - x^2}$, $0 \le x \le a$:
>
> $$
> \tfrac14 A = \int_0^a \frac{b}{a}\sqrt{a^2 - x^2}\,dx .
> $$
>
> Substitute $x = a\sin\theta$, $dx = a\cos\theta\,d\theta$. **Change the limits:** $x = 0$ gives $\sin\theta = 0$, $\theta = 0$; $x = a$ gives $\sin\theta = 1$, $\theta = \pi/2$. For $0 \le \theta \le \pi/2$, $\sqrt{a^2 - x^2} = a|\cos\theta| = a\cos\theta$. So, with the half-angle identity ([[§45 Trigonometric Integrals#^thm-45-1|Theorem §45.1]]),
>
> $$
> \begin{aligned}
> A &= 4\,\frac{b}{a} \int_0^{\pi/2} a\cos\theta \cdot a\cos\theta\,d\theta = 4ab \int_0^{\pi/2} \cos^2\theta\,d\theta = 4ab \int_0^{\pi/2} \tfrac12 (1 + \cos 2\theta)\,d\theta \\
> &= 2ab\Big[\theta + \tfrac12 \sin 2\theta\Big]_0^{\pi/2} = 2ab\Big(\frac{\pi}{2} + 0 - 0\Big) = \pi ab .
> \end{aligned}
> $$
>
> With $a = b = r$ this proves that a circle of radius $r$ has area $\pi r^2$. Because the integral was definite, the limits were changed and there was no need to return to $x$. (The same area by Green's Theorem: [[§110 Green's Theorem#^ex-110-4|Example §110.4]].)
>
> *Stewart: Example 7.3.2*

^ex-46-2

> [!example] Example §46.3: The Tangent Substitution
> Find $\displaystyle\int \frac{dx}{x^2\sqrt{x^2 + 4}}$.
>
> Let $x = 2\tan\theta$, $-\pi/2 < \theta < \pi/2$. Then $dx = 2\sec^2\theta\,d\theta$ and
>
> $$
> \sqrt{x^2 + 4} = \sqrt{4(\tan^2\theta + 1)} = \sqrt{4\sec^2\theta} = 2|\sec\theta| = 2\sec\theta .
> $$
>
> So
>
> $$
> \int \frac{dx}{x^2\sqrt{x^2 + 4}} = \int \frac{2\sec^2\theta\,d\theta}{4\tan^2\theta \cdot 2\sec\theta} = \frac14 \int \frac{\sec\theta}{\tan^2\theta}\,d\theta .
> $$
>
> In terms of sine and cosine, $\dfrac{\sec\theta}{\tan^2\theta} = \dfrac{1}{\cos\theta} \cdot \dfrac{\cos^2\theta}{\sin^2\theta} = \dfrac{\cos\theta}{\sin^2\theta}$. With $u = \sin\theta$, $du = \cos\theta\,d\theta$,
>
> $$
> \frac14 \int \frac{\cos\theta}{\sin^2\theta}\,d\theta = \frac14 \int \frac{du}{u^2} = \frac14\Big(-\frac1u\Big) + C = -\frac{1}{4\sin\theta} + C = -\frac{\csc\theta}{4} + C .
> $$
>
> **Back to $x$.** $\tan\theta = x/2$: opposite side $x$, adjacent side $2$, hypotenuse $\sqrt{x^2 + 4}$, so $\csc\theta = \sqrt{x^2 + 4}/x$ and
>
> $$
> \int \frac{dx}{x^2\sqrt{x^2 + 4}} = -\frac{\sqrt{x^2 + 4}}{4x} + C .
> $$
>
> *Stewart: Example 7.3.3*

^ex-46-3

> [!theorem] Proposition §46.2: The Integral of $1/\sqrt{x^2 - a^2}$
> For $a > 0$,
>
> $$
> \int \frac{dx}{\sqrt{x^2 - a^2}} = \ln\big|x + \sqrt{x^2 - a^2}\big| + C . \qquad (1)
> $$
>
> For $x > a$ this can also be written
>
> $$
> \int \frac{dx}{\sqrt{x^2 - a^2}} = \cosh^{-1}\Big(\frac{x}{a}\Big) + C . \qquad (2)
> $$
>
> *Stewart: 7.3, Formulas 1 and 2 (Example 7.3.5)*

^prop-46-2

> [!proof]+ Proof
> **Formula 1.** Let $x = a\sec\theta$, with $0 < \theta < \pi/2$ or $\pi < \theta < 3\pi/2$ (the integrand needs $|x| > a$). Then $dx = a\sec\theta\tan\theta\,d\theta$ and
>
> $$
> \sqrt{x^2 - a^2} = \sqrt{a^2(\sec^2\theta - 1)} = \sqrt{a^2\tan^2\theta} = a|\tan\theta| = a\tan\theta ,
> $$
>
> since $\tan\theta > 0$ on both intervals. So, by [[§45 Trigonometric Integrals#^thm-45-3|Theorem §45.3]],
>
> $$
> \int \frac{dx}{\sqrt{x^2 - a^2}} = \int \frac{a\sec\theta\tan\theta}{a\tan\theta}\,d\theta = \int \sec\theta\,d\theta = \ln|\sec\theta + \tan\theta| + C .
> $$
>
> The triangle with $\sec\theta = x/a$ (hypotenuse $x$, adjacent side $a$, opposite side $\sqrt{x^2 - a^2}$) gives $\tan\theta = \sqrt{x^2 - a^2}/a$. (For $\pi < \theta < 3\pi/2$, where $x < -a$, both $\sec\theta = x/a$ and $\tan\theta = \sqrt{x^2 - a^2}/a$ still hold, since $\tan\theta > 0$ and $\tan^2\theta = \sec^2\theta - 1$.) So
>
> $$
> \int \frac{dx}{\sqrt{x^2 - a^2}} = \ln\left|\frac{x}{a} + \frac{\sqrt{x^2 - a^2}}{a}\right| + C = \ln\big|x + \sqrt{x^2 - a^2}\big| - \ln a + C ,
> $$
>
> and $C_1 = C - \ln a$ is again an arbitrary constant.
>
> **Formula 2.** For $x > a$ use the hyperbolic substitution $x = a\cosh t$, $t > 0$. By $\cosh^2 t - \sinh^2 t = 1$, $\sqrt{x^2 - a^2} = \sqrt{a^2(\cosh^2 t - 1)} = \sqrt{a^2\sinh^2 t} = a\sinh t$ (as $\sinh t > 0$), and $dx = a\sinh t\,dt$, so
>
> $$
> \int \frac{dx}{\sqrt{x^2 - a^2}} = \int \frac{a\sinh t}{a\sinh t}\,dt = \int dt = t + C = \cosh^{-1}\Big(\frac{x}{a}\Big) + C .
> $$
>
> The two formulas agree because $\cosh^{-1} y = \ln\big(y + \sqrt{y^2 - 1}\big)$ for $y \ge 1$ ([[§24 Hyperbolic Functions|§24]], Stewart 3.11.4): $\cosh^{-1}(x/a) = \ln\big(x + \sqrt{x^2 - a^2}\big) - \ln a$.

^pf-46-2

*Uses:* [[§46 Trigonometric Substitution#^thm-46-1|§46.1]], [[§45 Trigonometric Integrals#^thm-45-3|§45.3]], [[§24 Hyperbolic Functions|§24]] (hyperbolic identities, Formula 3.11.4)

Hyperbolic substitutions can replace trigonometric ones and sometimes give simpler answers, but trigonometric identities are more familiar, so trigonometric substitutions are the usual choice.

> [!example] Example §46.4: A Preliminary Substitution and a Power 3/2
> Find $\displaystyle\int_0^{3\sqrt3/2} \frac{x^3}{(4x^2 + 9)^{3/2}}\,dx$.
>
> $(4x^2 + 9)^{3/2} = \big(\sqrt{4x^2 + 9}\big)^3$, so a trigonometric substitution is appropriate. The radical becomes $\sqrt{u^2 + 9}$ after the preliminary substitution $u = 2x$; then $u = 3\tan\theta$. In one step: $x = \frac32 \tan\theta$, $dx = \frac32 \sec^2\theta\,d\theta$, and
>
> $$
> \sqrt{4x^2 + 9} = \sqrt{9\tan^2\theta + 9} = 3\sec\theta .
> $$
>
> **Limits:** $x = 0$ gives $\tan\theta = 0$, $\theta = 0$; $x = 3\sqrt3/2$ gives $\tan\theta = \sqrt3$, $\theta = \pi/3$. Then
>
> $$
> \begin{aligned}
> \int_0^{3\sqrt3/2} \frac{x^3}{(4x^2 + 9)^{3/2}}\,dx &= \int_0^{\pi/3} \frac{\frac{27}{8}\tan^3\theta}{27\sec^3\theta} \cdot \frac32 \sec^2\theta\,d\theta = \frac{3}{16} \int_0^{\pi/3} \frac{\tan^3\theta}{\sec\theta}\,d\theta \\
> &= \frac{3}{16} \int_0^{\pi/3} \frac{\sin^3\theta}{\cos^2\theta}\,d\theta = \frac{3}{16} \int_0^{\pi/3} \frac{1 - \cos^2\theta}{\cos^2\theta}\,\sin\theta\,d\theta .
> \end{aligned}
> $$
>
> (An odd power of sine: step 2 of [[§45 Trigonometric Integrals#^rem-45-1|the method of §45]].) Substitute $u = \cos\theta$, $du = -\sin\theta\,d\theta$; $\theta = 0$ gives $u = 1$ and $\theta = \pi/3$ gives $u = \frac12$:
>
> $$
> \begin{aligned}
> \frac{3}{16} \int_0^{\pi/3} \frac{1 - \cos^2\theta}{\cos^2\theta}\,\sin\theta\,d\theta &= -\frac{3}{16} \int_1^{1/2} \frac{1 - u^2}{u^2}\,du = \frac{3}{16} \int_1^{1/2} (1 - u^{-2})\,du \\
> &= \frac{3}{16}\Big[u + \frac1u\Big]_1^{1/2} = \frac{3}{16}\Big[\big(\tfrac12 + 2\big) - (1 + 1)\Big] = \frac{3}{32} .
> \end{aligned}
> $$
>
> *Stewart: Example 7.3.6*

^ex-46-4

> [!example] Example §46.5: Completing the Square First
> Evaluate $\displaystyle\int \frac{x}{\sqrt{3 - 2x - x^2}}\,dx$.
>
> Complete the square under the root:
>
> $$
> 3 - 2x - x^2 = 3 - (x^2 + 2x) = 3 + 1 - (x^2 + 2x + 1) = 4 - (x + 1)^2 .
> $$
>
> Substitute $u = x + 1$, so $du = dx$ and $x = u - 1$:
>
> $$
> \int \frac{x}{\sqrt{3 - 2x - x^2}}\,dx = \int \frac{u - 1}{\sqrt{4 - u^2}}\,du .
> $$
>
> Now $u = 2\sin\theta$, $du = 2\cos\theta\,d\theta$, $\sqrt{4 - u^2} = 2\cos\theta$ ($-\pi/2 \le \theta \le \pi/2$):
>
> $$
> \begin{aligned}
> \int \frac{u - 1}{\sqrt{4 - u^2}}\,du &= \int \frac{2\sin\theta - 1}{2\cos\theta}\,2\cos\theta\,d\theta = \int (2\sin\theta - 1)\,d\theta = -2\cos\theta - \theta + C \\
> &= -\sqrt{4 - u^2} - \sin^{-1}\Big(\frac{u}{2}\Big) + C = -\sqrt{3 - 2x - x^2} - \sin^{-1}\Big(\frac{x + 1}{2}\Big) + C ,
> \end{aligned}
> $$
>
> using $2\cos\theta = \sqrt{4 - u^2}$ and $\theta = \sin^{-1}(u/2)$.
>
> *Stewart: Example 7.3.7*

^ex-46-5
