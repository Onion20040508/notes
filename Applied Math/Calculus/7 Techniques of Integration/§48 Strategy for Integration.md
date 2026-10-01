---
type: section
subject: "[[Calculus]]"
chapter: 7
section: 48
stewart: "7.5"
aliases: ["Stewart 7.5"]
tags: [calculus]
---
← [[§47 Integration of Rational Functions by Partial Fractions]] · ↑ [[· 7 Techniques of Integration]] · [[§49 Integration Using Tables and Technology]] →

*Stewart, Section 7.5.*

In differentiation it is always clear which rule to apply; in integration it is not. This section collects the basic integration formulas that should be known by heart and gives a four-step strategy for recognizing which technique fits a given integral: simplify, look for a substitution, classify the integrand by its form, and otherwise try again with substitution or parts. It ends with a limitation of the whole enterprise. Many elementary functions, such as $e^{x^2}$, have antiderivatives that are not elementary, so no strategy can find them in closed form.

## Guidelines for Integration

> [!theorem] Theorem §48.1: Table of Integration Formulas
> Constants of integration are omitted.
>
> | | | | |
> |---|---|---|---|
> | 1. | $\displaystyle\int x^n\,dx = \frac{x^{n+1}}{n + 1}$ $(n \ne -1)$ | 2. | $\displaystyle\int \frac1x\,dx = \ln\lvert x\rvert$ |
> | 3. | $\displaystyle\int e^x\,dx = e^x$ | 4. | $\displaystyle\int b^x\,dx = \frac{b^x}{\ln b}$ |
> | 5. | $\displaystyle\int \sin x\,dx = -\cos x$ | 6. | $\displaystyle\int \cos x\,dx = \sin x$ |
> | 7. | $\displaystyle\int \sec^2 x\,dx = \tan x$ | 8. | $\displaystyle\int \csc^2 x\,dx = -\cot x$ |
> | 9. | $\displaystyle\int \sec x \tan x\,dx = \sec x$ | 10. | $\displaystyle\int \csc x \cot x\,dx = -\csc x$ |
> | 11. | $\displaystyle\int \sec x\,dx = \ln\lvert\sec x + \tan x\rvert$ | 12. | $\displaystyle\int \csc x\,dx = \ln\lvert\csc x - \cot x\rvert$ |
> | 13. | $\displaystyle\int \tan x\,dx = \ln\lvert\sec x\rvert$ | 14. | $\displaystyle\int \cot x\,dx = \ln\lvert\sin x\rvert$ |
> | 15. | $\displaystyle\int \sinh x\,dx = \cosh x$ | 16. | $\displaystyle\int \cosh x\,dx = \sinh x$ |
> | 17. | $\displaystyle\int \frac{dx}{x^2 + a^2} = \frac1a \tan^{-1}\Big(\frac{x}{a}\Big)$ | 18. | $\displaystyle\int \frac{dx}{\sqrt{a^2 - x^2}} = \sin^{-1}\Big(\frac{x}{a}\Big)$, $a > 0$ |
> | \*19. | $\displaystyle\int \frac{dx}{x^2 - a^2} = \frac{1}{2a}\ln\left\lvert\frac{x - a}{x + a}\right\rvert$ | \*20. | $\displaystyle\int \frac{dx}{\sqrt{x^2 \pm a^2}} = \ln\Big\lvert x + \sqrt{x^2 \pm a^2}\Big\rvert$ |
>
> Most of these should be memorized. The ones marked with an asterisk need not be, since they are easily derived: Formula 19 can be avoided by using partial fractions, and trigonometric substitutions can be used in place of Formula 20.
>
> *Stewart: 7.5, Table of Integration Formulas*

^thm-48-1

> [!proof]- Proof
> Each formula says that the derivative of the right side is the integrand. Formulas 1–10 and 15–16 are the differentiation formulas of Chapter 3 read backwards, as collected in [[§37 Indefinite Integrals and the Net Change Theorem#^thm-37-1|Theorem §37.1]] ([[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-2|Theorem §14.2]] and [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-6|Theorem §19.6]] for powers, [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-6|Theorem §14.6]] and [[§17 The Chain Rule#^thm-17-5|Theorem §17.5]] for exponentials, [[§16 Derivatives of Trigonometric Functions#^thm-16-4|Theorem §16.4]], [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-5|Theorem §19.5]], [[§24 Hyperbolic Functions#^thm-24-2|Theorem §24.2]]); for Formula 2, $\frac{d}{dx}\ln|x| = \frac1x$ for $x \ne 0$ on either side of $0$. The others were derived in this chapter or follow the same way:
> - **11** is [[§45 Trigonometric Integrals#^thm-45-3|Theorem §45.3]] and **13** is [[§45 Trigonometric Integrals#^thm-45-2|Theorem §45.2]].
> - **12.** $\dfrac{d}{dx}\ln|\csc x - \cot x| = \dfrac{-\csc x \cot x + \csc^2 x}{\csc x - \cot x} = \dfrac{\csc x(\csc x - \cot x)}{\csc x - \cot x} = \csc x$.
> - **14.** With $u = \sin x$, $\int \cot x\,dx = \int \frac{\cos x}{\sin x}\,dx = \int \frac{du}{u} = \ln|\sin x|$.
> - **17** is [[§47 Integration of Rational Functions by Partial Fractions#^thm-47-4|Theorem §47.4]] and **19** is [[§47 Integration of Rational Functions by Partial Fractions#^prop-47-5|Proposition §47.5]].
> - **18.** $\dfrac{d}{dx}\sin^{-1}\dfrac{x}{a} = \dfrac{1}{\sqrt{1 - x^2/a^2}} \cdot \dfrac1a = \dfrac{1}{\sqrt{a^2 - x^2}}$, using $a > 0$ to write $a\sqrt{1 - x^2/a^2} = \sqrt{a^2 - x^2}$.
> - **20** with the minus sign is [[§46 Trigonometric Substitution#^prop-46-2|Proposition §46.2]]. With the plus sign, $\dfrac{d}{dx}\ln\big(x + \sqrt{x^2 + a^2}\big) = \dfrac{1 + x/\sqrt{x^2 + a^2}}{x + \sqrt{x^2 + a^2}} = \dfrac{1}{\sqrt{x^2 + a^2}}$ (and $x + \sqrt{x^2 + a^2} > 0$, so the absolute value is harmless).

^pf-48-1

*Uses:* [[§45 Trigonometric Integrals#^thm-45-2|§45.2]], [[§45 Trigonometric Integrals#^thm-45-3|§45.3]], [[§46 Trigonometric Substitution#^prop-46-2|§46.2]], [[§47 Integration of Rational Functions by Partial Fractions#^thm-47-4|§47.4]], [[§47 Integration of Rational Functions by Partial Fractions#^prop-47-5|§47.5]], [[§38 The Substitution Rule#^thm-38-1|§38.1]], [[§37 Indefinite Integrals and the Net Change Theorem#^thm-37-1|§37.1]], [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-2|§14.2]], [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-6|§14.6]], [[§16 Derivatives of Trigonometric Functions#^thm-16-4|§16.4]], [[§17 The Chain Rule#^thm-17-2|§17.2]], [[§17 The Chain Rule#^thm-17-5|§17.5]], [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-5|§19.5]], [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-6|§19.6]], [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-8|§19.8]], [[§24 Hyperbolic Functions#^thm-24-2|§24.2]]

> [!remark] Remark: Method — Strategy for Integration
> 1. **Simplify the integrand if possible.** Algebra or a trigonometric identity may make the method obvious:
>
>    $$
>    \int \sqrt{x}\,(1 + \sqrt{x})\,dx = \int (\sqrt{x} + x)\,dx, \qquad \int \frac{\tan\theta}{\sec^2\theta}\,d\theta = \int \sin\theta\cos\theta\,d\theta = \frac12 \int \sin 2\theta\,d\theta ,
>    $$
>
>    $$
>    \int (\sin x + \cos x)^2\,dx = \int (\sin^2 x + 2\sin x\cos x + \cos^2 x)\,dx = \int (1 + 2\sin x \cos x)\,dx .
>    $$
>
> 2. **Look for an obvious substitution.** Find a function $u = g(x)$ whose differential $du = g'(x)\,dx$ also occurs in the integrand, apart from a constant factor. In $\int \frac{x}{x^2 - 1}\,dx$, $u = x^2 - 1$ does it, and partial fractions are not needed.
> 3. **Classify the integrand according to its form.**
>    1. *Trigonometric functions:* products of powers of $\sin x$ and $\cos x$, of $\tan x$ and $\sec x$, or of $\cot x$ and $\csc x$: [[§45 Trigonometric Integrals#^rem-45-1|Remark: Method (sine and cosine)]] and [[§45 Trigonometric Integrals#^rem-45-2|Remark: Method (tangent and secant)]].
>    2. *Rational functions:* partial fractions, [[§47 Integration of Rational Functions by Partial Fractions#^rem-47-1|Remark: Method — Partial Fractions]].
>    3. *Integration by parts:* a power of $x$ (or a polynomial) times a transcendental function (trigonometric, exponential or logarithmic), with $u$ and $dv$ chosen as in [[§44 Integration by Parts#^rem-44-1|§44]].
>    4. *Radicals:* if $\sqrt{x^2 + a^2}$, $\sqrt{x^2 - a^2}$ or $\sqrt{a^2 - x^2}$ occurs, a trigonometric substitution ([[§46 Trigonometric Substitution#^rem-46-1|§46]]); if $\sqrt[n]{ax + b}$ occurs, the rationalizing substitution $u = \sqrt[n]{ax + b}$ ([[§47 Integration of Rational Functions by Partial Fractions#^ex-47-5|§47]]), which sometimes also works for $\sqrt[n]{g(x)}$.
> 4. **Try again.** There are basically only two methods of integration, substitution and parts.
>    1. *Try substitution.* Even if none is obvious, inspiration or ingenuity (or desperation) may suggest one.
>    2. *Try parts.* Besides the products of step 3(c), parts works on single functions whose derivatives are simpler: $\tan^{-1} x$, $\sin^{-1} x$, $\ln x$, which are all inverse functions.
>    3. *Manipulate the integrand.* Rationalize a denominator or use identities, for instance
>
>       $$
>       \int \frac{dx}{1 - \cos x} = \int \frac{1 + \cos x}{1 - \cos^2 x}\,dx = \int \frac{1 + \cos x}{\sin^2 x}\,dx = \int \Big(\csc^2 x + \frac{\cos x}{\sin^2 x}\Big)\,dx .
>       $$
>
>    4. *Relate the problem to previous problems.* For example $\int \tan^2 x \sec x\,dx = \int \sec^3 x\,dx - \int \sec x\,dx$, and $\int \sec^3 x\,dx$ is known ([[§45 Trigonometric Integrals#^ex-45-4|Example §45.4]]).
>    5. *Use several methods.* Successive substitutions of different types, or parts combined with substitutions.
>
> *Stewart: 7.5, steps 1–4*

^rem-48-1

## Examples

Stewart only indicates the method of attack in these examples. Here each is carried out to the end.

> [!example] Example §48.1: Simplify First
> Find $\displaystyle\int \frac{\tan^3 x}{\cos^3 x}\,dx$.
>
> **Step 1:** $\dfrac{\tan^3 x}{\cos^3 x} = \tan^3 x \sec^3 x$. This is $\int \tan^m x \sec^n x\,dx$ with $m$ odd ([[§45 Trigonometric Integrals#^rem-45-2|§45, step 2]]): save $\sec x \tan x$, write $\tan^2 x = \sec^2 x - 1$ and put $u = \sec x$:
>
> $$
> \int \tan^3 x \sec^3 x\,dx = \int (\sec^2 x - 1)\sec^2 x\,\sec x \tan x\,dx = \int (u^4 - u^2)\,du = \tfrac15 \sec^5 x - \tfrac13 \sec^3 x + C .
> $$
>
> **Alternatively**, step 1 could have given $\dfrac{\sin^3 x}{\cos^6 x}$. With $u = \cos x$, $du = -\sin x\,dx$,
>
> $$
> \int \frac{\sin^3 x}{\cos^6 x}\,dx = \int \frac{1 - \cos^2 x}{\cos^6 x}\,\sin x\,dx = \int \frac{1 - u^2}{u^6}\,(-du) = \int (u^{-4} - u^{-6})\,du = -\frac{1}{3u^3} + \frac{1}{5u^5} + C ,
> $$
>
> which is the same answer, since $1/u = \sec x$.
>
> *Stewart: Example 7.5.1*

^ex-48-1

> [!example] Example §48.2: A Substitution Leading to Parts
> Find $\displaystyle\int \sin\sqrt{x}\,dx$.
>
> By step 3(d), substitute $u = \sqrt{x}$. Then $x = u^2$, $dx = 2u\,du$, and $\int \sin\sqrt{x}\,dx = 2\int u \sin u\,du$. This is a power of $u$ times $\sin u$, so integrate by parts as in [[§44 Integration by Parts#^ex-44-1|Example §44.1]]: $\int u\sin u\,du = -u\cos u + \sin u + C$. Hence
>
> $$
> \int \sin\sqrt{x}\,dx = 2\sin\sqrt{x} - 2\sqrt{x}\cos\sqrt{x} + C .
> $$
>
> *Stewart: Example 7.5.2*

^ex-48-2

> [!example] Example §48.3: A Rational Function
> Find $\displaystyle\int \frac{x^5 + 1}{x^3 - 3x^2 - 10x}\,dx$.
>
> No simplification or substitution is apparent (steps 1 and 2 fail). The integrand is rational, so use partial fractions (step 3(b)), starting with division:
>
> $$
> x^5 + 1 = (x^2 + 3x + 19)(x^3 - 3x^2 - 10x) + (87x^2 + 190x + 1) .
> $$
>
> The denominator factors as $x(x^2 - 3x - 10) = x(x - 5)(x + 2)$, three distinct linear factors, so
>
> $$
> \frac{87x^2 + 190x + 1}{x(x - 5)(x + 2)} = \frac{A}{x} + \frac{B}{x - 5} + \frac{C}{x + 2}, \qquad 87x^2 + 190x + 1 = A(x - 5)(x + 2) + Bx(x + 2) + Cx(x - 5) .
> $$
>
> Substituting $x = 0$: $1 = -10A$, so $A = -\frac{1}{10}$. $x = 5$: $2175 + 950 + 1 = 3126 = 35B$, so $B = \frac{3126}{35}$. $x = -2$: $348 - 380 + 1 = -31 = 14C$, so $C = -\frac{31}{14}$. (Check: the coefficient of $x^2$ is $A + B + C = -\frac{1}{10} + \frac{3126}{35} - \frac{31}{14} = \frac{-7 + 6252 - 155}{70} = \frac{6090}{70} = 87$.) Therefore
>
> $$
> \int \frac{x^5 + 1}{x^3 - 3x^2 - 10x}\,dx = \frac{x^3}{3} + \frac{3x^2}{2} + 19x - \frac{1}{10}\ln|x| + \frac{3126}{35}\ln|x - 5| - \frac{31}{14}\ln|x + 2| + C .
> $$
>
> *Stewart: Example 7.5.3*

^ex-48-3

> [!example] Example §48.4: Only Step 2 Is Needed
> Find $\displaystyle\int \frac{dx}{x\sqrt{\ln x}}$.
>
> The differential of $u = \ln x$ is $du = dx/x$, which occurs in the integral:
>
> $$
> \int \frac{dx}{x\sqrt{\ln x}} = \int u^{-1/2}\,du = 2u^{1/2} + C = 2\sqrt{\ln x} + C .
> $$
>
> *Stewart: Example 7.5.4*

^ex-48-4

> [!example] Example §48.5: Manipulation Beats the Obvious Substitution
> Find $\displaystyle\int \sqrt{\frac{1 - x}{1 + x}}\,dx$.
>
> The rationalizing substitution $u = \sqrt{(1 - x)/(1 + x)}$ works but leads to a complicated rational function. Instead (step 1 or 4(c)) multiply numerator and denominator by $\sqrt{1 - x}$; for $-1 < x < 1$, $\sqrt{1 - x}\sqrt{1 + x} = \sqrt{1 - x^2}$, so
>
> $$
> \int \sqrt{\frac{1 - x}{1 + x}}\,dx = \int \frac{1 - x}{\sqrt{1 - x^2}}\,dx = \int \frac{dx}{\sqrt{1 - x^2}} - \int \frac{x}{\sqrt{1 - x^2}}\,dx = \sin^{-1} x + \sqrt{1 - x^2} + C ,
> $$
>
> using Formula 18 and the substitution $u = 1 - x^2$ in the second integral ($\int \frac{x\,dx}{\sqrt{1 - x^2}} = -\frac12 \int u^{-1/2}\,du = -\sqrt{1 - x^2}$).
>
> *Stewart: Example 7.5.5*

^ex-48-5

## Can We Integrate All Continuous Functions?

> [!definition] Definition §48.1: Elementary Function
> The **elementary functions** are the polynomials, rational functions, power functions ($x^a$), exponential functions ($b^x$), logarithmic functions, trigonometric and inverse trigonometric functions, hyperbolic and inverse hyperbolic functions, and all functions obtained from these by the five operations of addition, subtraction, multiplication, division and composition.
>
> For instance, $f(x) = \sqrt{\dfrac{x^2 - 1}{x^3 + 2x - 1}} + \ln(\cosh x) - x e^{\sin 2x}$ is elementary.
>
> *Stewart: 7.5 (text)*

^def-48-1

The derivative of an elementary function is elementary, by the differentiation rules. Integration is different.

> [!theorem] Theorem §48.2: Antiderivatives That Are Not Elementary
> The continuous function $f(x) = e^{x^2}$ has an antiderivative, $F(x) = \int_0^x e^{t^2}\,dt$, but $F$ is not an elementary function. The same holds for
>
> $$
> \int \frac{e^x}{x}\,dx, \quad \int \sin(x^2)\,dx, \quad \int \cos(e^x)\,dx, \quad \int \sqrt{x^3 + 1}\,dx, \quad \int \frac{1}{\ln x}\,dx, \quad \int \frac{\sin x}{x}\,dx .
> $$
>
> In fact, most elementary functions do not have elementary antiderivatives.
>
> *Stewart: 7.5 (text)*

^thm-48-2

*That $F$ exists and $F'(x) = e^{x^2}$ is Part 1 of the Fundamental Theorem of Calculus ([[§36 The Fundamental Theorem of Calculus#^thm-36-1|Theorem §36.1]]). Stewart omits the proof that $F$ is not elementary ("it has been proved"); it is a theorem of Liouville from differential algebra, and no note in the vault proves it.*

So no strategy, however clever, evaluates $\int e^{x^2}\,dx$ in terms of familiar functions. Such integrals are handled instead by numerical methods ([[§50 Approximate Integration|§50]]) or by infinite series ([[§78 Taylor and Maclaurin Series|§78]]).
