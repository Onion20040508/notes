---
type: section
subject: "[[Calculus]]"
chapter: 7
section: 45
stewart: "7.2"
aliases: ["Stewart 7.2"]
tags: [calculus]
---
← [[§44 Integration by Parts]] · ↑ [[· 7 Techniques of Integration]] · [[§46 Trigonometric Substitution]] →

*Stewart, Section 7.2 · MATH 233 (UMass, Spring 2023): Practice Exam 2 (Q1(a)).*

Trigonometric identities turn products of powers of trigonometric functions into integrals that a substitution can finish. For $\int \sin^m x \cos^n x\,dx$ the idea is to split off one factor of $\cos x$ (or $\sin x$) to serve as $du$, and to convert the remaining even power by $\sin^2 x + \cos^2 x = 1$. When both powers are even, the half-angle identities lower the powers instead. The same plan works for $\int \tan^m x \sec^n x\,dx$ with $\sec^2 x = 1 + \tan^2 x$, and the product identities handle $\sin mx \cos nx$ and its relatives. These integrals come back in trigonometric substitution ([[§46 Trigonometric Substitution|§46]]), arc length and surface area ([[§52 Arc Length|§52]]) and Fourier series.

## Integrals of Powers of Sine and Cosine

> [!theorem] Theorem §45.1: Half-Angle Identities
> For all $x$,
>
> $$
> \sin^2 x = \tfrac12 (1 - \cos 2x) \qquad\text{and}\qquad \cos^2 x = \tfrac12 (1 + \cos 2x) .
> $$
>
> Also $\sin x \cos x = \tfrac12 \sin 2x$.
>
> *Stewart: 7.2 (text); Appendix D, Equations 18a and 18b*

^thm-45-1

> [!proof]+ Proof
> By the addition formula for cosine, $\cos 2x = \cos(x + x) = \cos^2 x - \sin^2 x$. Replacing $\cos^2 x$ by $1 - \sin^2 x$ gives $\cos 2x = 1 - 2\sin^2 x$; replacing $\sin^2 x$ by $1 - \cos^2 x$ gives $\cos 2x = 2\cos^2 x - 1$. Solve these for $\sin^2 x$ and $\cos^2 x$. Likewise $\sin 2x = \sin(x + x) = 2\sin x \cos x$.

^pf-45-1

*Uses:* [[§119 Trigonometry#^thm-119-6|§119.6]] (addition formulas)

The home of these identities is [[§119 Trigonometry#^cor-119-8|Corollary §119.8]] (Stewart's Appendix D, Formulas 16–18), where they are proved the same way; they are repeated here because Stewart states them at this point.

> [!remark] Remark: Method — Evaluating the Integral of a Product of Powers of Sine and Cosine
> To find $\int \sin^m x \cos^n x\,dx$ with integers $m, n \ge 0$:
> 1. **The power of cosine is odd** ($n = 2k + 1$). Save one cosine factor and use $\cos^2 x = 1 - \sin^2 x$ for the rest:
>
>    $$
>    \int \sin^m x \cos^{2k+1} x\,dx = \int \sin^m x\,(1 - \sin^2 x)^k \cos x\,dx ,
>    $$
>
>    then substitute $u = \sin x$, $du = \cos x\,dx$.
> 2. **The power of sine is odd** ($m = 2k + 1$). Save one sine factor and use $\sin^2 x = 1 - \cos^2 x$:
>
>    $$
>    \int \sin^{2k+1} x \cos^n x\,dx = \int (1 - \cos^2 x)^k \cos^n x\,\sin x\,dx ,
>    $$
>
>    then substitute $u = \cos x$, $du = -\sin x\,dx$.
>
>    If both powers are odd, either step works.
> 3. **Both powers are even.** Use the half-angle identities (Theorem §45.1), repeatedly if necessary, and sometimes $\sin x \cos x = \frac12 \sin 2x$.
>
> *Stewart: 7.2, Strategy for Evaluating* $\int \sin^m x \cos^n x\,dx$

^rem-45-1

Why save exactly one factor: $u = \sin x$ needs $du = \cos x\,dx$, and one $\cos x$ is all it needs. An even power of cosine left over converts to sine. If the power of cosine were even, saving one factor would leave an odd power, which does not convert.

> [!example] Example §45.1: Odd Powers
> **(a)** Evaluate $\displaystyle\int \cos^3 x\,dx$. **(b)** Find $\displaystyle\int \sin^5 x \cos^2 x\,dx$.
>
> **(a)** $u = \cos x$ is no help, since $du = -\sin x\,dx$ and there is no factor $\sin x$. Instead separate one cosine factor (step 1, $m = 0$, $k = 1$): $\cos^3 x = \cos^2 x \cdot \cos x = (1 - \sin^2 x)\cos x$. With $u = \sin x$, $du = \cos x\,dx$,
>
> $$
> \int \cos^3 x\,dx = \int (1 - \sin^2 x)\cos x\,dx = \int (1 - u^2)\,du = u - \tfrac13 u^3 + C = \sin x - \tfrac13 \sin^3 x + C .
> $$
>
> **(b)** Converting $\cos^2 x$ to $1 - \sin^2 x$ would leave only powers of $\sin x$ and no $\cos x$ factor. Instead separate one sine factor (step 2, $k = 2$, $n = 2$):
>
> $$
> \sin^5 x \cos^2 x = (\sin^2 x)^2 \cos^2 x \sin x = (1 - \cos^2 x)^2 \cos^2 x \sin x .
> $$
>
> With $u = \cos x$, $du = -\sin x\,dx$,
>
> $$
> \begin{aligned}
> \int \sin^5 x \cos^2 x\,dx &= \int (1 - \cos^2 x)^2 \cos^2 x \sin x\,dx = \int (1 - u^2)^2 u^2\,(-du) = -\int (u^2 - 2u^4 + u^6)\,du \\
> &= -\Big(\frac{u^3}{3} - 2\,\frac{u^5}{5} + \frac{u^7}{7}\Big) + C = -\tfrac13 \cos^3 x + \tfrac25 \cos^5 x - \tfrac17 \cos^7 x + C .
> \end{aligned}
> $$
>
> *Stewart: Examples 7.2.1 and 7.2.2*

^ex-45-1

> [!example] Example §45.2: Even Powers
> **(a)** Evaluate $\displaystyle\int_0^\pi \sin^2 x\,dx$. **(b)** Find $\displaystyle\int \sin^4 x\,dx$. **(c)** Find the area enclosed by the polar curve $r = 2\sin\theta$.
>
> **(a)** Writing $\sin^2 x = 1 - \cos^2 x$ gives an integral that is no easier. The half-angle identity does it (with the mental substitution $u = 2x$ for $\int \cos 2x\,dx$):
>
> $$
> \int_0^\pi \sin^2 x\,dx = \frac12 \int_0^\pi (1 - \cos 2x)\,dx = \Big[\tfrac12\big(x - \tfrac12 \sin 2x\big)\Big]_0^\pi = \tfrac12\big(\pi - \tfrac12 \sin 2\pi\big) - \tfrac12\big(0 - \tfrac12 \sin 0\big) = \frac{\pi}{2} .
> $$
>
> This is the area under one arch of $y = \sin^2 x$. (The reduction formula, [[§44 Integration by Parts#^prop-44-3|Proposition §44.3]] with $n = 2$, gives the same.)
>
> **(b)** Write $\sin^4 x = (\sin^2 x)^2$ and use the half-angle identity:
>
> $$
> \int \sin^4 x\,dx = \int \Big[\tfrac12 (1 - \cos 2x)\Big]^2 dx = \frac14 \int \big(1 - 2\cos 2x + \cos^2 2x\big)\,dx .
> $$
>
> Now $\cos^2 2x$ occurs, so use the half-angle identity for cosine with $2x$ in place of $x$: $\cos^2 2x = \frac12 (1 + \cos 4x)$. Then
>
> $$
> \int \sin^4 x\,dx = \frac14 \int \Big(\frac32 - 2\cos 2x + \frac12 \cos 4x\Big)\,dx = \frac14\Big(\frac32 x - \sin 2x + \frac18 \sin 4x\Big) + C .
> $$
>
> (The reduction formula applied twice also works, but this is shorter.)
>
> **(c)** The circle $r = 2\sin\theta$ is traced once for $0 \le \theta \le \pi$. As a double integral in polar coordinates ([[§100 Double Integrals in Polar Coordinates#^thm-100-2|Theorem §100.2]], [[§100 Double Integrals in Polar Coordinates#^cor-100-3|Corollary §100.3]]),
>
> $$
> A = \int_0^\pi \int_0^{2\sin\theta} r\,dr\,d\theta = \int_0^\pi \Big[\frac{r^2}{2}\Big]_0^{2\sin\theta} d\theta = 2 \int_0^\pi \sin^2\theta\,d\theta = 2 \cdot \frac{\pi}{2} = \pi ,
> $$
>
> by part (a). This agrees with geometry: $r = 2\sin\theta$ means $x^2 + y^2 = 2y$, the circle of radius $1$ centred at $(0, 1)$.
>
> *Stewart: Examples 7.2.3 and 7.2.4*
> *Source: 233 Practice Exam 2, Q1(a)*

^ex-45-2

## Integrals of Powers of Secant and Tangent

The same reasoning applies to $\int \tan^m x \sec^n x\,dx$. Since $\frac{d}{dx}\tan x = \sec^2 x$, one can save a factor $\sec^2 x$ and convert the remaining *even* power of secant to tangent by $\sec^2 x = 1 + \tan^2 x$. Since $\frac{d}{dx}\sec x = \sec x \tan x$, one can instead save a factor $\sec x \tan x$ and convert the remaining *even* power of tangent to secant.

> [!remark] Remark: Method — Evaluating the Integral of a Product of Powers of Tangent and Secant
> To find $\int \tan^m x \sec^n x\,dx$:
> 1. **The power of secant is even** ($n = 2k$, $k \ge 2$). Save a factor of $\sec^2 x$ and use $\sec^2 x = 1 + \tan^2 x$ for the rest:
>
>    $$
>    \int \tan^m x \sec^{2k} x\,dx = \int \tan^m x\,(1 + \tan^2 x)^{k-1} \sec^2 x\,dx ,
>    $$
>
>    then substitute $u = \tan x$, $du = \sec^2 x\,dx$.
> 2. **The power of tangent is odd** ($m = 2k + 1$). Save a factor of $\sec x \tan x$ and use $\tan^2 x = \sec^2 x - 1$:
>
>    $$
>    \int \tan^{2k+1} x \sec^n x\,dx = \int (\sec^2 x - 1)^k \sec^{n-1} x\,\sec x \tan x\,dx ,
>    $$
>
>    then substitute $u = \sec x$, $du = \sec x \tan x\,dx$.
> 3. **Other cases** are not as clear-cut: identities, integration by parts, and Theorems §45.2 and §45.3 below. If an even power of tangent occurs with an odd power of secant, write everything in terms of $\sec x$; powers of $\sec x$ may need integration by parts (Example §45.4). For instance, $\int \tan^3 x\,dx = \int \tan x(\sec^2 x - 1)\,dx = \frac12 \tan^2 x - \ln|\sec x| + C$.
>
> Integrals $\int \cot^m x \csc^n x\,dx$ are found in the same way with $1 + \cot^2 x = \csc^2 x$.
>
> *Stewart: 7.2, Strategy for Evaluating* $\int \tan^m x \sec^n x\,dx$

^rem-45-2

> [!example] Example §45.3: Even Secant, Odd Tangent
> **(a)** Evaluate $\displaystyle\int \tan^6 x \sec^4 x\,dx$. **(b)** Find $\displaystyle\int \tan^5\theta \sec^7\theta\,d\theta$.
>
> **(a)** The power of secant is even (step 1). Separate one $\sec^2 x$ and write the other as $1 + \tan^2 x$; with $u = \tan x$, $du = \sec^2 x\,dx$,
>
> $$
> \begin{aligned}
> \int \tan^6 x \sec^4 x\,dx &= \int \tan^6 x\,(1 + \tan^2 x)\sec^2 x\,dx = \int u^6 (1 + u^2)\,du = \int (u^6 + u^8)\,du \\
> &= \frac{u^7}{7} + \frac{u^9}{9} + C = \tfrac17 \tan^7 x + \tfrac19 \tan^9 x + C .
> \end{aligned}
> $$
>
> **(b)** Separating $\sec^2\theta$ would leave $\sec^5\theta$, an odd power, which does not convert to tangent. The power of tangent is odd (step 2), so separate $\sec\theta\tan\theta$ and write $\tan^4\theta = (\sec^2\theta - 1)^2$; with $u = \sec\theta$, $du = \sec\theta\tan\theta\,d\theta$,
>
> $$
> \begin{aligned}
> \int \tan^5\theta \sec^7\theta\,d\theta &= \int \tan^4\theta \sec^6\theta\,\sec\theta\tan\theta\,d\theta = \int (\sec^2\theta - 1)^2 \sec^6\theta\,\sec\theta\tan\theta\,d\theta \\
> &= \int (u^2 - 1)^2 u^6\,du = \int (u^{10} - 2u^8 + u^6)\,du = \frac{u^{11}}{11} - 2\,\frac{u^9}{9} + \frac{u^7}{7} + C \\
> &= \tfrac{1}{11}\sec^{11}\theta - \tfrac29 \sec^9\theta + \tfrac17 \sec^7\theta + C .
> \end{aligned}
> $$
>
> *Stewart: Examples 7.2.5 and 7.2.6*

^ex-45-3

> [!theorem] Theorem §45.2: Integral of Tangent
> $$
> \int \tan x\,dx = \ln|\sec x| + C .
> $$
>
> *Stewart: 7.2 (boxed; established in Example 5.5.6)*

^thm-45-2

> [!proof]+ Proof
> Write $\tan x = \dfrac{\sin x}{\cos x}$ and substitute $u = \cos x$, $du = -\sin x\,dx$:
>
> $$
> \int \tan x\,dx = \int \frac{\sin x}{\cos x}\,dx = -\int \frac{du}{u} = -\ln|u| + C = -\ln|\cos x| + C = \ln\frac{1}{|\cos x|} + C = \ln|\sec x| + C .
> $$

^pf-45-2

*Uses:* [[§38 The Substitution Rule#^thm-38-1|§38.1]]

This is [[§38 The Substitution Rule#^thm-38-2|Theorem §38.2]], where the formula is first proved (Stewart's Example 5.5.6); Stewart restates it here next to the integral of secant.

> [!theorem] Theorem §45.3: Integral of Secant
> $$
> \int \sec x\,dx = \ln|\sec x + \tan x| + C . \qquad (1)
> $$
>
> *Stewart: 7.2, Formula 1*

^thm-45-3

> [!proof]+ Proof
> Multiply numerator and denominator by $\sec x + \tan x$:
>
> $$
> \int \sec x\,dx = \int \sec x\,\frac{\sec x + \tan x}{\sec x + \tan x}\,dx = \int \frac{\sec^2 x + \sec x \tan x}{\sec x + \tan x}\,dx .
> $$
>
> With $u = \sec x + \tan x$, $du = (\sec x \tan x + \sec^2 x)\,dx$ is exactly the numerator, so the integral is $\int \frac{du}{u} = \ln|u| + C = \ln|\sec x + \tan x| + C$. (Alternatively, differentiate the right side of (1): $\dfrac{\sec x \tan x + \sec^2 x}{\sec x + \tan x} = \sec x$.)

^pf-45-3

*Uses:* [[§38 The Substitution Rule#^thm-38-1|§38.1]]

James Gregory found Formula 1 in 1668, while solving a problem in constructing nautical tables.

> [!example] Example §45.4: The Integral of Secant Cubed
> Find $\displaystyle\int \sec^3 x\,dx$.
>
> Integrate by parts ([[§44 Integration by Parts#^thm-44-1|Theorem §44.1]]) with
>
> $$
> u = \sec x \qquad dv = \sec^2 x\,dx \qquad\qquad du = \sec x \tan x\,dx \qquad v = \tan x .
> $$
>
> Then, using $\tan^2 x = \sec^2 x - 1$,
>
> $$
> \begin{aligned}
> \int \sec^3 x\,dx &= \sec x \tan x - \int \sec x \tan^2 x\,dx = \sec x \tan x - \int \sec x (\sec^2 x - 1)\,dx \\
> &= \sec x \tan x - \int \sec^3 x\,dx + \int \sec x\,dx .
> \end{aligned}
> $$
>
> The original integral has reappeared (as in [[§44 Integration by Parts#^ex-44-3|Example §44.3]]). Solve for it, using Theorem §45.3 for $\int \sec x\,dx$:
>
> $$
> \int \sec^3 x\,dx = \tfrac12\big(\sec x \tan x + \ln|\sec x + \tan x|\big) + C .
> $$
>
> This integral looks special, but it comes up again and again in applications: the arc length of a parabola, for instance ([[§52 Arc Length#^ex-52-2|Example §52.2]]).
>
> *Stewart: Example 7.2.8*

^ex-45-4

## Using Product Identities

> [!theorem] Theorem §45.4: Product Identities
> For all $A$ and $B$,
>
> $$
> \begin{aligned}
> &\text{(a)}\quad \sin A \cos B = \tfrac12\big[\sin(A - B) + \sin(A + B)\big] \\
> &\text{(b)}\quad \sin A \sin B = \tfrac12\big[\cos(A - B) - \cos(A + B)\big] \\
> &\text{(c)}\quad \cos A \cos B = \tfrac12\big[\cos(A - B) + \cos(A + B)\big]
> \end{aligned}
> $$
>
> They are used to evaluate (a) $\int \sin mx \cos nx\,dx$, (b) $\int \sin mx \sin nx\,dx$, (c) $\int \cos mx \cos nx\,dx$.
>
> *Stewart: 7.2, Equation 2 (identities from Appendix D)*

^thm-45-4

> [!proof]+ Proof
> By the addition formulas,
>
> $$
> \sin(A \pm B) = \sin A \cos B \pm \cos A \sin B, \qquad \cos(A \pm B) = \cos A \cos B \mp \sin A \sin B .
> $$
>
> Adding the two sine formulas gives $\sin(A + B) + \sin(A - B) = 2\sin A \cos B$, which is (a). Subtracting the cosine formulas gives $\cos(A - B) - \cos(A + B) = 2\sin A \sin B$, which is (b). Adding them gives $\cos(A - B) + \cos(A + B) = 2\cos A \cos B$, which is (c).

^pf-45-4

*Uses:* [[§119 Trigonometry#^thm-119-6|§119.6]] (addition formulas)

The home of these identities is [[§119 Trigonometry#^cor-119-9|Corollary §119.9]] (Stewart's Appendix D, Formulas 19a–19c).

> [!example] Example §45.5: A Product of Sines and Cosines of Different Frequencies
> Evaluate $\displaystyle\int \sin 4x \cos 5x\,dx$.
>
> Integration by parts would work, but Theorem §45.4(a) with $A = 4x$, $B = 5x$ is quicker:
>
> $$
> \int \sin 4x \cos 5x\,dx = \int \tfrac12\big[\sin(-x) + \sin 9x\big]\,dx = \tfrac12 \int (-\sin x + \sin 9x)\,dx = \tfrac12\big(\cos x - \tfrac19 \cos 9x\big) + C .
> $$
>
> *Stewart: Example 7.2.9*

^ex-45-5

> [!remark]- Remark: Orthogonality of Sines and Cosines
> For positive integers $m$ and $n$, the product identities give
>
> $$
> \int_{-\pi}^{\pi} \sin mx \cos nx\,dx = 0, \qquad \int_{-\pi}^{\pi} \sin mx \sin nx\,dx = \int_{-\pi}^{\pi} \cos mx \cos nx\,dx = \begin{cases} 0 & m \ne n \\ \pi & m = n . \end{cases}
> $$
>
> For instance, if $m \ne n$, (b) turns $\sin mx \sin nx$ into $\frac12[\cos(m - n)x - \cos(m + n)x]$, and each cosine integrates to a multiple of $\sin(kx)$ with $k \ne 0$ an integer, which vanishes at $\pm\pi$. If $m = n$, it is $\frac12[1 - \cos 2mx]$, with integral $\pi$. (Stewart's Exercises 75–77.) So the coefficients of a finite Fourier series $f(x) = \sum_{n=1}^N a_n \sin nx$ are recovered as $a_m = \frac1\pi \int_{-\pi}^{\pi} f(x) \sin mx\,dx$ (Exercise 78). In the language of linear algebra, the functions $\sin nx$, $\cos nx$ are orthogonal for the inner product $\langle f, g \rangle = \int_{-\pi}^{\pi} f g\,dx$ ([[§46 Inner Product Spaces#^def-46-1|235 Def. §46.1]]; the integral inner product is [[§46 Inner Product Spaces#^ex-46-4|235 Ex. §46.4]]).

^rem-45-3

> [!remark]- Connections
> - See also: [[§6 Periodic Functions and Fourier Series#^prop-6-3|341 Prop. §6.3]] (the same orthogonality relations, including the constant function $1$), which give the coefficients of a Fourier series, [[§6 Periodic Functions and Fourier Series#^prop-6-4|341 Prop. §6.4]].
