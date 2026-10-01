---
type: section
subject: "[[Calculus]]"
chapter: 3
section: 16
stewart: "3.3"
aliases: ["Stewart 3.3"]
tags: [calculus]
---
← [[§15 The Product and Quotient Rules]] · ↑ [[· 3 Differentiation Rules]] · [[§17 The Chain Rule]] →

*Stewart, Section 3.3 · Appendix F.*

The derivative of $\sin x$ is $\cos x$ and the derivative of $\cos x$ is $-\sin x$. Both come from the addition formulas and two special limits, $\lim_{\theta \to 0} (\sin\theta)/\theta = 1$ and $\lim_{\theta \to 0} (\cos\theta - 1)/\theta = 0$, which are proved at the end of the section by comparing $\sin\theta$, $\theta$ and $\tan\theta$ on the unit circle. The Quotient Rule ([[§15 The Product and Quotient Rules|§15]]) then gives the derivatives of the other four trigonometric functions. The two limits are also useful in their own right for computing other limits.

Throughout, $\sin x$ means the sine of the angle whose **radian** measure is $x$, and likewise for the other trigonometric functions. All six are continuous at every number in their domains ([[§10 Continuity#^thm-10-4|Theorem §10.4]]). The formulas below hold only for radian measure.

## Derivatives of the Trigonometric Functions

Sketching the slopes of the tangent lines to $y = \sin x$ (zero at the peaks and troughs, largest at $0, \pm 2\pi, \ldots$, most negative at $\pm\pi, \ldots$) suggests that the graph of the derivative is the cosine curve.

> [!theorem] Theorem §16.1: Derivative of Sine
> $$
> \frac{d}{dx}(\sin x) = \cos x .
> $$
>
> *Stewart: 3.3, Formula 2*

^thm-16-1

> [!proof]+ Proof
> From the definition of the derivative and the addition formula $\sin(x + h) = \sin x \cos h + \cos x \sin h$,
>
> $$
> \begin{aligned}
> f'(x) &= \lim_{h \to 0} \frac{\sin(x + h) - \sin x}{h} = \lim_{h \to 0} \frac{\sin x \cos h + \cos x \sin h - \sin x}{h} \\
> &= \lim_{h \to 0} \left[ \sin x \left( \frac{\cos h - 1}{h} \right) + \cos x \left( \frac{\sin h}{h} \right) \right] \\
> &= \lim_{h \to 0} \sin x \cdot \lim_{h \to 0} \frac{\cos h - 1}{h} + \lim_{h \to 0} \cos x \cdot \lim_{h \to 0} \frac{\sin h}{h} . \qquad (1)
> \end{aligned}
> $$
>
> The Limit Laws apply provided all four limits exist. Since $x$ is constant as $h \to 0$, $\lim_{h \to 0} \sin x = \sin x$ and $\lim_{h \to 0} \cos x = \cos x$. The other two limits are $0$ and $1$ ([[§16 Derivatives of Trigonometric Functions#^thm-16-7|Theorem §16.7]] and [[§16 Derivatives of Trigonometric Functions#^thm-16-6|Theorem §16.6]], proved below). So
>
> $$
> f'(x) = (\sin x) \cdot 0 + (\cos x) \cdot 1 = \cos x .
> $$

^pf-16-1

*Uses:* [[§13 The Derivative as a Function|§13]] (definition of $f'(x)$), [[§8 Calculating Limits Using the Limit Laws|§8]] (Limit Laws), [[§16 Derivatives of Trigonometric Functions#^thm-16-6|§16.6]], [[§16 Derivatives of Trigonometric Functions#^thm-16-7|§16.7]]

> [!remark]- Connections
> - In 451, sine and cosine can be *defined* by power series; term-by-term differentiation then gives $s' = c$ and $c' = -s$ without any geometry: [[§26 Differentiation and Integration of Power Series#^ex-26-8|451 Ex. §26.8]], using [[§26 Differentiation and Integration of Power Series#^thm-26-4|451 Thm. §26.4]].

For example, by the Product Rule, $\dfrac{d}{dx}(x^2 \sin x) = x^2 \cos x + 2x \sin x$.

> [!theorem] Theorem §16.2: Derivative of Cosine
> $$
> \frac{d}{dx}(\cos x) = -\sin x .
> $$
>
> *Stewart: 3.3, Formula 3 (Exercise 26)*

^thm-16-2

> [!proof]+ Proof
> Stewart leaves this as Exercise 26, by the method of Theorem §16.1. With the addition formula $\cos(x + h) = \cos x \cos h - \sin x \sin h$,
>
> $$
> \begin{aligned}
> \frac{d}{dx}(\cos x) &= \lim_{h \to 0} \frac{\cos x \cos h - \sin x \sin h - \cos x}{h} = \lim_{h \to 0} \left[ \cos x \left( \frac{\cos h - 1}{h} \right) - \sin x \left( \frac{\sin h}{h} \right) \right] \\
> &= (\cos x) \cdot 0 - (\sin x) \cdot 1 = -\sin x ,
> \end{aligned}
> $$
>
> by the Limit Laws and Theorems §16.6 and §16.7.

^pf-16-2

*Uses:* [[§13 The Derivative as a Function|§13]] (definition of $f'(x)$), [[§8 Calculating Limits Using the Limit Laws|§8]] (Limit Laws), [[§16 Derivatives of Trigonometric Functions#^thm-16-6|§16.6]], [[§16 Derivatives of Trigonometric Functions#^thm-16-7|§16.7]]

> [!theorem] Theorem §16.3: Derivative of Tangent
> $$
> \frac{d}{dx}(\tan x) = \sec^2 x .
> $$
>
> *Stewart: 3.3, Formula 4*

^thm-16-3

> [!proof]+ Proof
> The definition would work, but the Quotient Rule with Theorems §16.1 and §16.2 is easier. Wherever $\cos x \ne 0$,
>
> $$
> \begin{aligned}
> \frac{d}{dx}(\tan x) &= \frac{d}{dx}\left( \frac{\sin x}{\cos x} \right) = \frac{\cos x \dfrac{d}{dx}(\sin x) - \sin x \dfrac{d}{dx}(\cos x)}{\cos^2 x} \\
> &= \frac{\cos x \cdot \cos x - \sin x\,(-\sin x)}{\cos^2 x} = \frac{\cos^2 x + \sin^2 x}{\cos^2 x} = \frac{1}{\cos^2 x} = \sec^2 x ,
> \end{aligned}
> $$
>
> using $\cos^2 x + \sin^2 x = 1$.

^pf-16-3

*Uses:* [[§15 The Product and Quotient Rules#^thm-15-2|§15.2]], [[§16 Derivatives of Trigonometric Functions#^thm-16-1|§16.1]], [[§16 Derivatives of Trigonometric Functions#^thm-16-2|§16.2]]

> [!theorem] Theorem §16.4: Derivatives of the Trigonometric Functions
> On their domains,
>
> $$
> \begin{aligned}
> \frac{d}{dx}(\sin x) &= \cos x & \frac{d}{dx}(\csc x) &= -\csc x \cot x \\
> \frac{d}{dx}(\cos x) &= -\sin x & \frac{d}{dx}(\sec x) &= \sec x \tan x \\
> \frac{d}{dx}(\tan x) &= \sec^2 x & \frac{d}{dx}(\cot x) &= -\csc^2 x
> \end{aligned}
> $$
>
> The minus signs go with the derivatives of the "cofunctions": cosine, cosecant and cotangent.
>
> *Stewart: 3.3, Derivatives of Trigonometric Functions (Exercises 23–25)*

^thm-16-4

> [!proof]+ Proof
> The left column is Theorems §16.1–§16.3. Stewart leaves the right column as Exercises 23–25. By the Quotient Rule and Theorems §16.1 and §16.2:
>
> $$
> \begin{aligned}
> \frac{d}{dx}\left( \frac{1}{\sin x} \right) &= \frac{\sin x \cdot 0 - 1 \cdot \cos x}{\sin^2 x} = -\frac{1}{\sin x} \cdot \frac{\cos x}{\sin x} = -\csc x \cot x , \\
> \frac{d}{dx}\left( \frac{1}{\cos x} \right) &= \frac{\cos x \cdot 0 - 1 \cdot (-\sin x)}{\cos^2 x} = \frac{1}{\cos x} \cdot \frac{\sin x}{\cos x} = \sec x \tan x , \\
> \frac{d}{dx}\left( \frac{\cos x}{\sin x} \right) &= \frac{\sin x\,(-\sin x) - \cos x \cdot \cos x}{\sin^2 x} = -\frac{\sin^2 x + \cos^2 x}{\sin^2 x} = -\frac{1}{\sin^2 x} = -\csc^2 x .
> \end{aligned}
> $$

^pf-16-4

*Uses:* [[§15 The Product and Quotient Rules#^thm-15-2|§15.2]], [[§16 Derivatives of Trigonometric Functions#^thm-16-1|§16.1]], [[§16 Derivatives of Trigonometric Functions#^thm-16-2|§16.2]], [[§16 Derivatives of Trigonometric Functions#^thm-16-3|§16.3]]

> [!example] Example §16.1: Horizontal Tangents of a Trigonometric Quotient
> Differentiate $f(x) = \dfrac{\sec x}{1 + \tan x}$. For what values of $x$ does the graph of $f$ have a horizontal tangent?
>
> By the Quotient Rule and Theorem §16.4,
>
> $$
> \begin{aligned}
> f'(x) &= \frac{(1 + \tan x) \dfrac{d}{dx}(\sec x) - \sec x \dfrac{d}{dx}(1 + \tan x)}{(1 + \tan x)^2}
> = \frac{(1 + \tan x)\sec x \tan x - \sec x \cdot \sec^2 x}{(1 + \tan x)^2} \\
> &= \frac{\sec x\,(\tan x + \tan^2 x - \sec^2 x)}{(1 + \tan x)^2} = \frac{\sec x\,(\tan x - 1)}{(1 + \tan x)^2} ,
> \end{aligned}
> $$
>
> using $\sec^2 x = \tan^2 x + 1$. Since $\sec x = 1/\cos x$ is never $0$, $f'(x) = 0$ exactly when $\tan x = 1$, that is, when $x = \pi/4 + n\pi$ for an integer $n$.
>
> *Stewart: Example 3.3.2*

^ex-16-1

> [!example] Example §16.2: Simple Harmonic Motion
> An object fastened to the end of a vertical spring is stretched $4$ cm beyond its rest position and released at time $t = 0$. With the downward direction positive, its position at time $t$ is $s = f(t) = 4\cos t$. Find the velocity and acceleration at time $t$ and use them to analyze the motion.
>
> $$
> v = \frac{ds}{dt} = \frac{d}{dt}(4\cos t) = 4\frac{d}{dt}(\cos t) = -4\sin t, \qquad
> a = \frac{dv}{dt} = \frac{d}{dt}(-4\sin t) = -4\frac{d}{dt}(\sin t) = -4\cos t .
> $$
>
> - The object oscillates from the lowest point ($s = 4$ cm) to the highest point ($s = -4$ cm). The period is $2\pi$, the period of $\cos t$.
> - The speed is $|v| = 4|\sin t|$. It is greatest when $|\sin t| = 1$, that is, when $\cos t = 0$, so the object moves fastest as it passes through the equilibrium position $s = 0$. Its speed is $0$ when $\sin t = 0$, at the highest and lowest points.
> - The acceleration $a = -4\cos t = -s$ is $0$ when $s = 0$ and has its greatest magnitude at the highest and lowest points. It always points back toward equilibrium.
>
> *Stewart: Example 3.3.3*

^ex-16-2

> [!example] Example §16.3: The 27th Derivative of Cosine
> Find the 27th derivative of $\cos x$.
>
> For $f(x) = \cos x$,
>
> $$
> f'(x) = -\sin x, \quad f''(x) = -\cos x, \quad f'''(x) = \sin x, \quad f^{(4)}(x) = \cos x, \quad f^{(5)}(x) = -\sin x .
> $$
>
> The derivatives repeat in a cycle of length $4$, so $f^{(n)}(x) = \cos x$ whenever $n$ is a multiple of $4$. Hence $f^{(24)}(x) = \cos x$, and differentiating three more times, $f^{(27)}(x) = f'''(x) = \sin x$.
>
> *Stewart: Example 3.3.4*

^ex-16-3

## Two Special Trigonometric Limits

The proof of Theorem §16.1 used two limits, proved now. The first needs a comparison of $\theta$ with $\tan\theta$.

> [!theorem] Lemma §16.5: The Angle Is at Most Its Tangent
> If $0 < \theta < \pi/2$, then $\theta \le \tan\theta$.
>
> *Stewart: Appendix F (Section 3.3)*

^lem-16-5

> [!proof]- Proof
> Take a sector of the unit circle with center $O$, central angle $\theta$, from $A = (1, 0)$ to $B = (\cos\theta, \sin\theta)$. Let the tangent line to the circle at $A$ meet the line $OB$ at $D$. Then $|AD| = |OA|\tan\theta = \tan\theta$.
>
> Arc length is defined as the limit of the lengths of inscribed polygonal paths ([[§52 Arc Length|§52]], Equation 8.1.1). So approximate the arc $AB$ by an inscribed polygonal path of $n$ equal segments, and look at a typical segment $PQ$ ($P$ nearer to $A$). Extend $OP$ and $OQ$ to meet $AD$ at $R$ and $S$, and draw $RT$ parallel to $PQ$ with $T$ on $OS$.
> - Triangle $OPQ$ is isosceles ($|OP| = |OQ| = 1$), so its base angle $\angle PQO$ is less than $90^\circ$. Since $RT \parallel PQ$, $\angle RTO = \angle PQO < 90^\circ$, and so $\angle RTS = 180^\circ - \angle RTO > 90^\circ$.
> - Triangles $OPQ$ and $ORT$ are similar, with ratio $|OR|/|OP| = |OR| \ge 1$ (the point $R$ on the tangent line is not inside the circle). So $|PQ| \le |RT|$.
> - In triangle $RTS$ the angle at $T$ is obtuse, so the opposite side $RS$ is the longest: $|RT| < |RS|$.
>
> Hence $|PQ| < |RS|$ (Stewart writes $|PQ| < |RT|$; equality occurs for the segment with $P = A$, which does not affect the conclusion). As $PQ$ runs over the $n$ segments, the segments $RS$ fill out $AD$ without overlapping. Adding the $n$ inequalities,
>
> $$
> L_n < |AD| = \tan\theta ,
> $$
>
> where $L_n$ is the length of the inscribed polygonal path. Since limits preserve inequalities ([[§8 Calculating Limits Using the Limit Laws|§8]], Theorem 2.3.2), $\lim_{n \to \infty} L_n \le \tan\theta$. By the definition of arc length and of radian measure, $\theta = \text{arc } AB = \lim_{n \to \infty} L_n \le \tan\theta$.

^pf-16-5

*Uses:* [[§52 Arc Length|§52]] (definition of arc length), [[§8 Calculating Limits Using the Limit Laws|§8]] (Theorem 2.3.2)

> [!theorem] Theorem §16.6: The Limit of sin θ over θ
> $$
> \lim_{\theta \to 0} \frac{\sin\theta}{\theta} = 1 .
> $$
>
> *Stewart: 3.3, Equation 5*

^thm-16-6

> [!proof]+ Proof
> First let $0 < \theta < \pi/2$. With $O$, $A$, $B$, $D$ as in Lemma §16.5, let $C$ be the foot of the perpendicular from $B$ to $OA$. By the definition of radian measure, arc $AB = \theta$, and $|BC| = |OB|\sin\theta = \sin\theta$.
>
> **Upper bound.** The leg $BC$ of the right triangle $ABC$ is shorter than its hypotenuse $AB$, and the chord $AB$ is shorter than the arc $AB$:
>
> $$
> |BC| < |AB| < \text{arc } AB, \qquad\text{so}\qquad \sin\theta < \theta, \qquad \frac{\sin\theta}{\theta} < 1 .
> $$
>
> **Lower bound.** By Lemma §16.5, $\theta \le \tan\theta = \dfrac{\sin\theta}{\cos\theta}$. (Stewart's text argues this geometrically: with $E$ the point where the tangent lines at $A$ and $B$ meet, a circumscribed polygon is longer than the circle, so $\theta = \text{arc } AB < |AE| + |EB| < |AE| + |ED| = |AD| = \tan\theta$. Appendix F gives the proof from the definition of arc length.) Since $\cos\theta > 0$ and $\theta > 0$, this gives
>
> $$
> \cos\theta \le \frac{\sin\theta}{\theta} < 1 .
> $$
>
> **Squeeze.** $\lim_{\theta \to 0} 1 = 1$ and $\lim_{\theta \to 0} \cos\theta = 1$ ([[§10 Continuity#^thm-10-3|Theorem §10.3]]), so by the Squeeze Theorem
>
> $$
> \lim_{\theta \to 0^+} \frac{\sin\theta}{\theta} = 1 .
> $$
>
> **Left side.** $(\sin\theta)/\theta$ is an even function: $\dfrac{\sin(-\theta)}{-\theta} = \dfrac{-\sin\theta}{-\theta} = \dfrac{\sin\theta}{\theta}$. So its left-hand limit at $0$ equals its right-hand limit, and the two-sided limit is $1$.

^pf-16-6

*Uses:* [[§16 Derivatives of Trigonometric Functions#^lem-16-5|§16.5]], [[§10 Continuity#^thm-10-3|§10.3]], [[§8 Calculating Limits Using the Limit Laws|§8]] (Squeeze Theorem; one-sided limits)

![[m233-16-1.svg]]
*The three lengths in the proof, on the unit circle: $\sin\theta = |BC|$ (blue), $\theta = \text{arc } AB$ (red) and $\tan\theta = |AD|$ (green). As $\theta \to 0$ they become indistinguishable, and dividing $\sin\theta \le \theta \le \tan\theta$ by $\sin\theta$ squeezes $\theta/\sin\theta$ between $1$ and $1/\cos\theta$.*

> [!theorem] Theorem §16.7: The Limit of (cos θ − 1) over θ
> $$
> \lim_{\theta \to 0} \frac{\cos\theta - 1}{\theta} = 0 .
> $$
>
> *Stewart: 3.3, Equation 6*

^thm-16-7

> [!proof]+ Proof
> Multiply numerator and denominator by $\cos\theta + 1$ (which is near $2$ for $\theta$ near $0$, so not $0$), to reach limits we know:
>
> $$
> \begin{aligned}
> \lim_{\theta \to 0} \frac{\cos\theta - 1}{\theta}
> &= \lim_{\theta \to 0} \left( \frac{\cos\theta - 1}{\theta} \cdot \frac{\cos\theta + 1}{\cos\theta + 1} \right)
> = \lim_{\theta \to 0} \frac{\cos^2\theta - 1}{\theta(\cos\theta + 1)}
> = \lim_{\theta \to 0} \frac{-\sin^2\theta}{\theta(\cos\theta + 1)} \\
> &= -\lim_{\theta \to 0} \left( \frac{\sin\theta}{\theta} \cdot \frac{\sin\theta}{\cos\theta + 1} \right)
> = -\lim_{\theta \to 0} \frac{\sin\theta}{\theta} \cdot \lim_{\theta \to 0} \frac{\sin\theta}{\cos\theta + 1}
> = -1 \cdot \left( \frac{0}{1 + 1} \right) = 0 ,
> \end{aligned}
> $$
>
> by Theorem §16.6 and the continuity of sine and cosine at $0$.

^pf-16-7

*Uses:* [[§16 Derivatives of Trigonometric Functions#^thm-16-6|§16.6]], [[§10 Continuity#^thm-10-3|§10.3]], [[§8 Calculating Limits Using the Limit Laws|§8]] (Limit Laws 4 and 5)

> [!example] Example §16.4: Rescaling the Angle
> Find $\displaystyle\lim_{x \to 0} \frac{\sin 7x}{4x}$.
>
> To apply Theorem §16.6, the argument of sine must match the denominator. Multiply and divide by $7$ (note that $\sin 7x \ne 7\sin x$):
>
> $$
> \frac{\sin 7x}{4x} = \frac74 \left( \frac{\sin 7x}{7x} \right) .
> $$
>
> Let $\theta = 7x$. Then $\theta \to 0$ as $x \to 0$, and $\theta \ne 0$ when $x \ne 0$, so
>
> $$
> \lim_{x \to 0} \frac{\sin 7x}{4x} = \frac74 \lim_{x \to 0} \frac{\sin 7x}{7x} = \frac74 \lim_{\theta \to 0} \frac{\sin\theta}{\theta} = \frac74 \cdot 1 = \frac74 .
> $$
>
> *Stewart: Example 3.3.5*

^ex-16-4

> [!example] Example §16.5: Dividing by the Variable
> **(a)** Calculate $\displaystyle\lim_{x \to 0} x\cot x$. Divide numerator and denominator by $x$:
>
> $$
> \lim_{x \to 0} x\cot x = \lim_{x \to 0} \frac{x\cos x}{\sin x} = \lim_{x \to 0} \frac{\cos x}{\dfrac{\sin x}{x}} = \frac{\lim_{x \to 0} \cos x}{\lim_{x \to 0} \dfrac{\sin x}{x}} = \frac{\cos 0}{1} = 1 ,
> $$
>
> by the continuity of cosine and Theorem §16.6.
>
> **(b)** Find $\displaystyle\lim_{\theta \to 0} \frac{\cos\theta - 1}{\sin\theta}$. Divide numerator and denominator by $\theta$, to use Theorems §16.6 and §16.7:
>
> $$
> \lim_{\theta \to 0} \frac{\cos\theta - 1}{\sin\theta} = \lim_{\theta \to 0} \frac{\dfrac{\cos\theta - 1}{\theta}}{\dfrac{\sin\theta}{\theta}} = \frac{\lim_{\theta \to 0} \dfrac{\cos\theta - 1}{\theta}}{\lim_{\theta \to 0} \dfrac{\sin\theta}{\theta}} = \frac01 = 0 .
> $$
>
> In both parts the denominator's limit is $1 \ne 0$, so Limit Law 5 applies.
>
> *Stewart: Examples 3.3.6 and 3.3.7*

^ex-16-5
