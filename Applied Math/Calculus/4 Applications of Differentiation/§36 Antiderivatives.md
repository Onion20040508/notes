---
type: section
subject: "[[Calculus]]"
chapter: 4
section: 36
stewart: "4.9"
aliases: ["Stewart 4.9"]
tags: [calculus]
---
← [[§35 Newton's Method]] · ↑ [[· 4 Applications of Differentiation]] · [[§37 The Cubic x³ − 3x² + 1]] →

*Stewart, Section 4.9.*

Often the derivative of a function is known and the function itself is wanted: position from velocity, the amount of water leaked from the rate of leaking, a population from its growth rate. A function $F$ with $F' = f$ is an antiderivative of $f$. The Mean Value Theorem ([[§29 Rolle's Theorem and the Mean Value Theorem#^cor-29-4|Corollary §29.4]]) shows that on an interval all antiderivatives of $f$ differ by constants, so one antiderivative gives them all. Reading the table of derivatives backwards gives a table of antiderivatives. Extra conditions, such as an initial position and velocity, then pick out one function from the family; this is the first step toward solving differential equations and toward the Fundamental Theorem of Calculus ([[§41 The Fundamental Theorem of Calculus|§41]]).

## The Antiderivative of a Function

> [!definition] Definition §36.1: Antiderivative
> A function $F$ is called an **antiderivative** of $f$ on an interval $I$ if $F'(x) = f(x)$ for all $x$ in $I$.
>
> *Stewart: 4.9, Definition*

^def-36-1

For instance, $F(x) = \frac13 x^3$ is an antiderivative of $f(x) = x^2$, by the Power Rule. So is $G(x) = \frac13 x^3 + 100$, and so is every $\frac13 x^3 + C$ with $C$ a constant. There are no others:

> [!theorem] Theorem §36.1: The Most General Antiderivative
> If $F$ is an antiderivative of $f$ on an interval $I$, then the most general antiderivative of $f$ on $I$ is
>
> $$
> F(x) + C
> $$
>
> where $C$ is an arbitrary constant. That is, every $F + C$ is an antiderivative of $f$ on $I$, and every antiderivative of $f$ on $I$ has this form.
>
> *Stewart: 4.9, Theorem 1*

^thm-36-1

> [!proof]+ Proof
> For every constant $C$, $(F + C)' = F' + 0 = f$ on $I$, so $F + C$ is an antiderivative. Conversely, let $G$ be any antiderivative of $f$ on $I$. Then
>
> $$
> F'(x) = f(x) = G'(x) \qquad\text{for all } x \in I ,
> $$
>
> so by [[§29 Rolle's Theorem and the Mean Value Theorem#^cor-29-4|Corollary §29.4]] (two functions with the same derivative on an interval differ by a constant), $G(x) - F(x) = C$ for some constant $C$; that is, $G(x) = F(x) + C$.

^pf-36-1

*Uses:* [[§29 Rolle's Theorem and the Mean Value Theorem#^cor-29-4|§29.4]], [[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-1|§17.1]] (derivative of a constant), [[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-4|§17.4]] (Sum Rule)

> [!remark]- Connections
> - Rigorous treatment: [[§29 The Mean Value Theorem#^cor-29-5|451 Cor. §29.5]]. Integrals produce antiderivatives of continuous functions: [[§41 The Fundamental Theorem of Calculus#^thm-41-1|Theorem §41.1]] and [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]]; the general antiderivative is written $\int f(x)\,dx$ in [[§42 Indefinite Integrals and the Net Change Theorem#^def-42-1|Def. §42.1]].

![[m233-33-1.svg]]
*Members of the family of antiderivatives $\frac13 x^3 + C$ of $f(x) = x^2$, for $C = -2, -1, 0, 1, 2, 3$. They are vertical translates of one another, since all have the same slope $x^2$ at each $x$. By [[§36 Antiderivatives#^thm-36-1|Theorem §36.1]] there are no other antiderivatives on $\mathbb{R}$.*

> [!example] Example §36.1: Three General Antiderivatives
> Find the most general antiderivative of (a) $f(x) = \sin x$, (b) $f(x) = 1/x$, (c) $f(x) = x^n$, $n \ne -1$.
>
> **(a)** If $F(x) = -\cos x$, then $F'(x) = \sin x$. By [[§36 Antiderivatives#^thm-36-1|Theorem §36.1]], the most general antiderivative is $G(x) = -\cos x + C$.
>
> **(b)** Since $\frac{d}{dx}(\ln x) = \frac1x$ ([[§22 Derivatives of Logarithmic and Inverse Trigonometric Functions#^cor-22-3|Corollary §22.3]], with [[§22 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-22-5|Theorem §22.5]] for the absolute value below), on the interval $(0, \infty)$ the general antiderivative of $1/x$ is $\ln x + C$. More generally, $\frac{d}{dx}\ln|x| = \frac1x$ for all $x \ne 0$, so by [[§36 Antiderivatives#^thm-36-1|Theorem §36.1]] the general antiderivative of $1/x$ is $\ln|x| + C$ on any interval that does not contain $0$, in particular on $(-\infty, 0)$ and on $(0, \infty)$. The domain of $1/x$ is not an interval, so the constants on the two pieces are independent ([[§29 Rolle's Theorem and the Mean Value Theorem#^rem-29-2|Remark: The Interval Matters]]): the general antiderivative of $f$ is
>
> $$
> F(x) = \begin{cases} \ln x + C_1 & \text{if } x > 0 \\ \ln(-x) + C_2 & \text{if } x < 0 . \end{cases}
> $$
>
> **(c)** By the Power Rule, for $n \ne -1$,
>
> $$
> \frac{d}{dx}\Big(\frac{x^{n+1}}{n + 1}\Big) = \frac{(n + 1)x^n}{n + 1} = x^n ,
> $$
>
> so the general antiderivative of $x^n$ is $F(x) = \dfrac{x^{n+1}}{n + 1} + C$. This is valid for $n \ge 0$, since then $x^n$ is defined on the interval $\mathbb{R}$. If $n$ is negative (but $n \ne -1$), it is valid on any interval that does not contain $0$.
>
> *Stewart: Example 4.9.1*

^ex-36-1

## Antidifferentiation Formulas

Every differentiation formula, read from right to left, gives an antidifferentiation formula.

> [!theorem] Theorem §36.2: Table of Antidifferentiation Formulas
> Let $F' = f$ and $G' = g$. Then, on any interval where the functions are defined, the right column is a particular antiderivative of the left column:
>
> | Function | Particular antiderivative | Function | Particular antiderivative |
> |---|---|---|---|
> | $cf(x)$ | $cF(x)$ | $\sin x$ | $-\cos x$ |
> | $f(x) + g(x)$ | $F(x) + G(x)$ | $\sec^2 x$ | $\tan x$ |
> | $x^n$ $(n \ne -1)$ | $\dfrac{x^{n+1}}{n + 1}$ | $\sec x \tan x$ | $\sec x$ |
> | $\dfrac1x$ | $\ln\lvert x\rvert$ | $\dfrac{1}{\sqrt{1 - x^2}}$ | $\sin^{-1} x$ |
> | $e^x$ | $e^x$ | $\dfrac{1}{1 + x^2}$ | $\tan^{-1} x$ |
> | $b^x$ | $\dfrac{b^x}{\ln b}$ | $\cosh x$ | $\sinh x$ |
> | $\cos x$ | $\sin x$ | $\sinh x$ | $\cosh x$ |
>
> The first two rows say that an antiderivative of a constant times a function is the constant times an antiderivative, and an antiderivative of a sum is the sum of the antiderivatives. To obtain the most general antiderivative, add a constant (or constants) as in [[§36 Antiderivatives#^thm-36-1|Theorem §36.1]].
>
> *Stewart: 4.9, Table 2*

^thm-36-2

> [!proof]+ Proof
> Each formula is true because the derivative of the function in the right column is the function in the left column:
> - $(cF)' = cF' = cf$ and $(F + G)' = F' + G' = f + g$ (Constant Multiple and Sum Rules, [[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-3|Theorems §17.3]] and [[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-4|§17.4]]);
> - $\big(\frac{x^{n+1}}{n + 1}\big)' = x^n$ (Power Rule, [[§36 Antiderivatives#^ex-36-1|Example §36.1]](c)) and $(e^x)' = e^x$ ([[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-6|Theorem §17.6]]);
> - $(\ln|x|)' = \frac1x$, $\big(\frac{b^x}{\ln b}\big)' = \frac{b^x \ln b}{\ln b} = b^x$, $(\sin^{-1} x)' = \frac{1}{\sqrt{1 - x^2}}$, $(\tan^{-1} x)' = \frac{1}{1 + x^2}$ ([[§22 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-22-5|Theorem §22.5]], [[§20 The Chain Rule#^thm-20-5|Theorem §20.5]], [[§22 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-22-8|Theorem §22.8]]);
> - $(\sin x)' = \cos x$, $(-\cos x)' = \sin x$, $(\tan x)' = \sec^2 x$, $(\sec x)' = \sec x \tan x$ ([[§19 Derivatives of Trigonometric Functions#^thm-19-4|Theorem §19.4]]);
> - $(\sinh x)' = \cosh x$ and $(\cosh x)' = \sinh x$ ([[§27 Hyperbolic Functions#^thm-27-2|Theorem §27.2]]).

^pf-36-2

*Uses:* [[§36 Antiderivatives#^def-36-1|Def. §36.1]], [[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-3|§17.3]], [[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-4|§17.4]], [[§17 Derivatives of Polynomials and Exponential Functions#^thm-17-6|§17.6]], [[§36 Antiderivatives#^ex-36-1|Ex. §36.1]], [[§19 Derivatives of Trigonometric Functions#^thm-19-4|§19.4]], [[§20 The Chain Rule#^thm-20-5|§20.5]], [[§22 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-22-5|§22.5]], [[§22 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-22-8|§22.8]], [[§27 Hyperbolic Functions#^thm-27-2|§27.2]]

> [!example] Example §36.2: Using the Table
> Find all functions $g$ such that
>
> $$
> g'(x) = 4\sin x + \frac{2x^5 - \sqrt{x}}{x} .
> $$
>
> First rewrite the given function term by term:
>
> $$
> g'(x) = 4\sin x + \frac{2x^5}{x} - \frac{\sqrt{x}}{x} = 4\sin x + 2x^4 - x^{-1/2} .
> $$
>
> By the table (rows $cf$, $f + g$, $\sin x$ and $x^n$ with $n = 4$ and $n = -\frac12$) and [[§36 Antiderivatives#^thm-36-1|Theorem §36.1]],
>
> $$
> g(x) = 4(-\cos x) + 2\,\frac{x^5}{5} - \frac{x^{1/2}}{\frac12} + C = -4\cos x + \tfrac25 x^5 - 2\sqrt{x} + C ,
> $$
>
> on the interval $(0, \infty)$ where $g'$ is defined. (Check: differentiating gives back $4\sin x + 2x^4 - x^{-1/2}$.)
>
> *Stewart: Example 4.9.2*

^ex-36-2

> [!definition] Definition §36.2: Differential Equation
> An equation that involves the derivatives of a function is called a **differential equation**.
>
> Finding a function from its derivative, as in [[§36 Antiderivatives#^ex-36-2|Example §36.2]], is solving the simplest kind of differential equation, $y' = f(x)$. The general solution involves an arbitrary constant (or constants, if higher derivatives are given). Extra conditions, such as the value of the function at one point (an *initial condition*), may determine the constants and so specify the solution uniquely. Differential equations are studied in Chapter 9 ([[§66 Modeling with Differential Equations#^def-66-5|Def. §66.5]]).
>
> *Stewart: 4.9 (text)*

^def-36-2

> [!example] Example §36.3: Using Initial Conditions
> **(a)** Find $f$ if $f'(x) = e^x + 20(1 + x^2)^{-1}$ and $f(0) = -2$.
>
> By the table, the general antiderivative of $f'(x) = e^x + \dfrac{20}{1 + x^2}$ is
>
> $$
> f(x) = e^x + 20\tan^{-1} x + C .
> $$
>
> To determine $C$, use $f(0) = -2$: $f(0) = e^0 + 20\tan^{-1} 0 + C = 1 + C = -2$, so $C = -3$, and the particular solution is
>
> $$
> f(x) = e^x + 20\tan^{-1} x - 3 .
> $$
>
> (Since $f' > 0$ everywhere, this $f$ is increasing, and it has an inflection point wherever $f'$ has a maximum or minimum.)
>
> **(b)** Find $f$ if $f''(x) = 12x^2 + 6x - 4$, $f(0) = 4$ and $f(1) = 1$.
>
> The general antiderivative of $f''$ is
>
> $$
> f'(x) = 12\,\frac{x^3}{3} + 6\,\frac{x^2}{2} - 4x + C = 4x^3 + 3x^2 - 4x + C .
> $$
>
> Antidifferentiating once more,
>
> $$
> f(x) = 4\,\frac{x^4}{4} + 3\,\frac{x^3}{3} - 4\,\frac{x^2}{2} + Cx + D = x^4 + x^3 - 2x^2 + Cx + D .
> $$
>
> Two conditions determine the two constants. $f(0) = 0 + D = 4$ gives $D = 4$. Then $f(1) = 1 + 1 - 2 + C + 4 = C + 4 = 1$ gives $C = -3$. Therefore
>
> $$
> f(x) = x^4 + x^3 - 2x^2 - 3x + 4 .
> $$
>
> *Stewart: Examples 4.9.3 and 4.9.4*

^ex-36-3

## Graphing Antiderivatives

The principles of this chapter let one sketch an antiderivative $F$ of $f$ from the graph of $f$ alone (for instance when $f$ comes from experimental data). Since $F' = f$, the slope of $y = F(x)$ at each $x$ is $f(x)$, and $F'' = f'$:
- $F$ increases where $f > 0$ and decreases where $f < 0$;
- $F$ has horizontal tangents at the zeros of $f$, with a local minimum where $f$ changes from negative to positive and a local maximum where it changes from positive to negative;
- $F$ has inflection points where $f'$ changes sign, that is, at the local maxima and minima of $f$;
- where $f(x) \to 0$, the graph of $F$ flattens out.

A given value such as $F(0) = 2$ fixes the starting point, and hence the one member of the family $F + C$ to draw. (Stewart's Example 4.9.5.)

## Linear Motion

If an object moves in a straight line with position function $s = f(t)$, its velocity is $v(t) = s'(t)$ and its acceleration is $a(t) = v'(t)$ ([[§14 Derivatives and Rates of Change#^def-14-2|Def. §14.2]], [[§23 Rates of Change in the Natural and Social Sciences#^def-23-3|Def. §23.3]]). So the velocity is an antiderivative of the acceleration, and the position is an antiderivative of the velocity. If $a(t)$ and the initial values $s(0)$ and $v(0)$ are known, the position is found by antidifferentiating twice.

> [!example] Example §36.4: Motion with Given Acceleration
> **(a)** A particle moves in a straight line with acceleration $a(t) = 6t + 4$. Its initial velocity is $v(0) = -6$ cm/s and its initial displacement is $s(0) = 9$ cm. Find its position function.
>
> Since $v'(t) = a(t) = 6t + 4$, antidifferentiation gives $v(t) = 3t^2 + 4t + C$. Then $v(0) = C = -6$, so $v(t) = 3t^2 + 4t - 6$. Since $s'(t) = v(t)$, $s(t) = t^3 + 2t^2 - 6t + D$, and $s(0) = D = 9$. So
>
> $$
> s(t) = t^3 + 2t^2 - 6t + 9 .
> $$
>
> **(b)** Near the earth's surface the acceleration due to gravity is constant, $g \approx 9.8$ m/s² $\approx 32$ ft/s², directed downward. A ball is thrown upward with a speed of $48$ ft/s from the edge of a cliff, $432$ ft above the ground. Find its height above the ground $t$ seconds later. When does it reach its maximum height? When does it hit the ground?
>
> Choose the positive direction upward, and let $s(t)$ be the height above the ground. The velocity decreases, so the acceleration is negative:
>
> $$
> a(t) = \frac{dv}{dt} = -32 .
> $$
>
> Antidifferentiating, $v(t) = -32t + C$, and $v(0) = 48$ gives $C = 48$: $v(t) = -32t + 48$. The maximum height is reached when $v(t) = 0$, that is, after $1.5$ seconds (the velocity changes from positive to negative there). Antidifferentiating again, $s(t) = -16t^2 + 48t + D$, and $s(0) = 432$ gives $D = 432$:
>
> $$
> s(t) = -16t^2 + 48t + 432 .
> $$
>
> (So the maximum height is $s(1.5) = -36 + 72 + 432 = 468$ ft.) The formula is valid until the ball hits the ground, when $s(t) = 0$:
>
> $$
> -16t^2 + 48t + 432 = 0 \iff t^2 - 3t - 27 = 0 \iff t = \frac{3 \pm \sqrt{9 + 108}}{2} = \frac{3 \pm 3\sqrt{13}}{2} .
> $$
>
> The solution with the minus sign is negative, so it is rejected. The ball hits the ground after $\frac32(1 + \sqrt{13}) \approx 6.9$ seconds.
>
> *Stewart: Examples 4.9.6 and 4.9.7*

^ex-36-4
