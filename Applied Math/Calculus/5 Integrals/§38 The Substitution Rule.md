---
type: section
subject: "[[Calculus]]"
chapter: 5
section: 38
stewart: "5.5"
aliases: ["Stewart 5.5"]
tags: [calculus]
---
← [[§37 Indefinite Integrals and the Net Change Theorem]] · ↑ [[· 5 Integrals]] · [[§39 Areas Between Curves]] →

*Stewart, Section 5.5.*

The table of [[§37 Indefinite Integrals and the Net Change Theorem|§37]] does not cover integrals such as $\int 2x\sqrt{1 + x^2}\,dx$. The Substitution Rule handles them by changing from $x$ to a new variable $u = g(x)$. It is the Chain Rule read backward, and it says that one may calculate with $dx$ and $du$ as if they were differentials. For definite integrals the limits of integration change along with the variable. As an application, the integral of an even function over $[-a, a]$ is twice the integral over $[0, a]$, and that of an odd function is $0$.

## Substitution: Indefinite Integrals

To find

$$
\int 2x\sqrt{1 + x^2}\,dx , \qquad (1)
$$

introduce something extra: a new variable $u = 1 + x^2$. Its differential is $du = 2x\,dx$ ([[§23 Linear Approximations and Differentials|§23]]). If the $dx$ in the notation of an integral were a differential, $2x\,dx$ would occur in (1), and formally

$$
\int 2x\sqrt{1 + x^2}\,dx = \int \sqrt{1 + x^2}\,2x\,dx = \int \sqrt{u}\,du = \tfrac23 u^{3/2} + C = \tfrac23 (1 + x^2)^{3/2} + C . \qquad (2)
$$

The answer is correct, as the Chain Rule confirms: $\frac{d}{dx}\big[\tfrac23 (1 + x^2)^{3/2} + C\big] = \tfrac23 \cdot \tfrac32 (1 + x^2)^{1/2} \cdot 2x = 2x\sqrt{1 + x^2}$.

> [!theorem] Theorem §38.1: The Substitution Rule
> If $u = g(x)$ is a differentiable function whose range is an interval $I$ and $f$ is continuous on $I$, then
>
> $$
> \int f(g(x))\,g'(x)\,dx = \int f(u)\,du .
> $$
>
> In words: it is permissible to operate with $dx$ and $du$ after integral signs as if they were differentials, $du = g'(x)\,dx$.
>
> *Stewart: 5.5, Equation 4*

^thm-38-1

> [!proof]+ Proof
> Let $F$ be an antiderivative of $f$ on $I$. (One exists because $f$ is continuous on the interval $I$: by FTC1, [[§36 The Fundamental Theorem of Calculus#^thm-36-1|Theorem §36.1]], $F(u) = \int_c^u f(t)\,dt$ for any fixed $c$ in $I$ will do. Stewart takes this for granted.) By the Chain Rule,
>
> $$
> \frac{d}{dx}\big[F(g(x))\big] = F'(g(x))\,g'(x) ,
> $$
>
> so
>
> $$
> \int F'(g(x))\,g'(x)\,dx = F(g(x)) + C . \qquad (3)
> $$
>
> With the "change of variable" or "substitution" $u = g(x)$, Equation (3) gives
>
> $$
> \int F'(g(x))\,g'(x)\,dx = F(g(x)) + C = F(u) + C = \int F'(u)\,du ,
> $$
>
> and writing $F' = f$, $\displaystyle\int f(g(x))\,g'(x)\,dx = \int f(u)\,du$.

^pf-38-1

*Uses:* [[§36 The Fundamental Theorem of Calculus#^thm-36-1|§36.1]], [[§17 The Chain Rule|§17]] (Chain Rule), [[§37 Indefinite Integrals and the Net Change Theorem#^def-37-1|Def. §37.1]]

> [!remark]- Connections
> - Rigorous treatment: [[§15 Multivariable Integration#^lem-15-13|452 Lemma §15.13]] proves the definite form from FTC and the Chain Rule for a $C^1$ bijection $g$ with $g' \ne 0$, written with $|g'(t)|$ so that the limits always run upward. It is the one-variable case of the change of variables formula for multiple integrals ([[§106 Change of Variables in Multiple Integrals|§106]]; [[§15 Multivariable Integration#^thm-15-20|452 Thm. §15.20]]).

> [!remark] Remark: Method — Choosing a Substitution
> The idea is to replace a complicated integral by a simpler one, as in Example §38.1, where $\int x^3\cos(x^4 + 2)\,dx$ becomes $\frac14 \int \cos u\,du$.
> 1. Try to choose $u$ to be some function in the integrand whose differential also occurs, apart from a constant factor.
> 2. If that is not possible, try choosing $u$ to be some complicated part of the integrand, perhaps the inner function of a composite function.
> 3. Compute $du = g'(x)\,dx$, solve for the part of the integrand it replaces (for example $x^3\,dx = \frac14 du$), and rewrite the *whole* integrand in terms of $u$. If some $x$ is left over, express it through $u$ (Example §38.2).
> 4. Integrate with respect to $u$, then return to the original variable $x$.
> 5. Check the answer by differentiating it. Finding the right substitution is a bit of an art: if the first guess does not work, try another.

^rem-38-1

> [!example] Example §38.1: Two Direct Substitutions
> **(a)** Find $\displaystyle\int x^3\cos(x^4 + 2)\,dx$.
>
> Let $u = x^4 + 2$: its differential $du = 4x^3\,dx$ occurs in the integral apart from the factor $4$. So $x^3\,dx = \frac14 du$, and
>
> $$
> \int x^3\cos(x^4 + 2)\,dx = \int \cos u \cdot \tfrac14\,du = \tfrac14 \int \cos u\,du = \tfrac14 \sin u + C = \tfrac14 \sin(x^4 + 2) + C .
> $$
>
> At the final stage we return to the original variable $x$.
>
> **(b)** Evaluate $\displaystyle\int e^{5x}\,dx$.
>
> Let $u = 5x$. Then $du = 5\,dx$, so $dx = \frac15 du$ and
>
> $$
> \int e^{5x}\,dx = \tfrac15 \int e^u\,du = \tfrac15 e^u + C = \tfrac15 e^{5x} + C .
> $$
>
> **Without writing $u$.** With some experience, one recognizes the pattern of Equation (3), an outer derivative times the derivative of the inner function:
>
> $$
> \int x^3\cos(x^4 + 2)\,dx = \tfrac14 \int \cos(x^4 + 2) \cdot \frac{d}{dx}(x^4 + 2)\,dx = \tfrac14 \sin(x^4 + 2) + C, \qquad
> \int e^{5x}\,dx = \tfrac15 \int \frac{d}{dx}(e^{5x})\,dx = \tfrac15 e^{5x} + C .
> $$
>
> *Stewart: Examples 5.5.1 and 5.5.4 and Note*

^ex-38-1

> [!example] Example §38.2: Expressing the Leftover x in Terms of u
> Find $\displaystyle\int \sqrt{1 + x^2}\,x^5\,dx$.
>
> A substitution becomes apparent after factoring $x^5 = x^4 \cdot x$. Let $u = 1 + x^2$. Then $du = 2x\,dx$, so $x\,dx = \frac12 du$. The leftover $x^4$ must also be written in terms of $u$: $x^2 = u - 1$, so $x^4 = (u - 1)^2$. Then
>
> $$
> \begin{aligned}
> \int \sqrt{1 + x^2}\,x^5\,dx &= \int \sqrt{1 + x^2}\,x^4 \cdot x\,dx = \int \sqrt{u}\,(u - 1)^2 \cdot \tfrac12\,du = \tfrac12 \int \sqrt{u}\,(u^2 - 2u + 1)\,du \\
> &= \tfrac12 \int \big(u^{5/2} - 2u^{3/2} + u^{1/2}\big)\,du = \tfrac12 \Big(\tfrac27 u^{7/2} - 2 \cdot \tfrac25 u^{5/2} + \tfrac23 u^{3/2}\Big) + C \\
> &= \tfrac17 (1 + x^2)^{7/2} - \tfrac25 (1 + x^2)^{5/2} + \tfrac13 (1 + x^2)^{3/2} + C .
> \end{aligned}
> $$
>
> *Stewart: Example 5.5.5*

^ex-38-2

> [!theorem] Theorem §38.2: Integral of the Tangent
> $$
> \int \tan x\,dx = -\ln|\cos x| + C = \ln|\sec x| + C .
> $$
>
> *Stewart: Example 5.5.6 and Equation 5*

^thm-38-2

> [!proof]+ Proof
> Write tangent in terms of sine and cosine, $\int \tan x\,dx = \int \frac{\sin x}{\cos x}\,dx$. This suggests $u = \cos x$, since then $du = -\sin x\,dx$, so $\sin x\,dx = -du$:
>
> $$
> \int \tan x\,dx = \int \frac{\sin x}{\cos x}\,dx = -\int \frac1u\,du = -\ln|u| + C = -\ln|\cos x| + C ,
> $$
>
> using $\int \frac1u\,du = \ln|u| + C$ ([[§37 Indefinite Integrals and the Net Change Theorem#^thm-37-1|Theorem §37.1]]). Finally $-\ln|\cos x| = \ln\big(|\cos x|^{-1}\big) = \ln\big(1/|\cos x|\big) = \ln|\sec x|$. (Each formula holds on any interval where $\cos x \ne 0$.)

^pf-38-2

*Uses:* [[§38 The Substitution Rule#^thm-38-1|§38.1]], [[§37 Indefinite Integrals and the Net Change Theorem#^thm-37-1|§37.1]]

## Substitution: Definite Integrals

A definite integral can be evaluated by substitution in two ways: find the indefinite integral first and then use FTC2, or, usually better, change the limits of integration along with the variable.

> [!theorem] Theorem §38.3: The Substitution Rule for Definite Integrals
> If $g'$ is continuous on $[a, b]$ and $f$ is continuous on the range of $u = g(x)$, then
>
> $$
> \int_a^b f(g(x))\,g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du .
> $$
>
> Everything is put in terms of the new variable $u$, including the limits of integration: the new limits are the values of $u$ that correspond to $x = a$ and $x = b$.
>
> *Stewart: 5.5, Equation 6*

^thm-38-3

> [!proof]+ Proof
> Let $F$ be an antiderivative of $f$. By (3), $F(g(x))$ is an antiderivative of $f(g(x))\,g'(x)$, which is continuous on $[a, b]$. So by FTC2 ([[§36 The Fundamental Theorem of Calculus#^thm-36-2|Theorem §36.2]]),
>
> $$
> \int_a^b f(g(x))\,g'(x)\,dx = F(g(x)) \Big]_a^b = F(g(b)) - F(g(a)) .
> $$
>
> Applying FTC2 a second time, now to $f$ on the interval between $g(a)$ and $g(b)$ (which lies in the range of $g$),
>
> $$
> \int_{g(a)}^{g(b)} f(u)\,du = F(u) \Big]_{g(a)}^{g(b)} = F(g(b)) - F(g(a)) .
> $$
>
> The two integrals are equal. (FTC2 also holds when $g(b) < g(a)$, by Definition §35.4.)

^pf-38-3

*Uses:* [[§38 The Substitution Rule#^thm-38-1|§38.1]] (Equation 3), [[§36 The Fundamental Theorem of Calculus#^thm-36-2|§36.2]], [[§35 The Definite Integral#^def-35-4|Def. §35.4]]

> [!example] Example §38.3: Two Substitutions, Two Methods
> **(a)** Evaluate $\displaystyle\int \sqrt{2x + 1}\,dx$.
>
> *Solution 1.* Let $u = 2x + 1$. Then $du = 2\,dx$, so $dx = \frac12 du$ and
>
> $$
> \int \sqrt{2x + 1}\,dx = \tfrac12 \int u^{1/2}\,du = \frac12 \cdot \frac{u^{3/2}}{3/2} + C = \tfrac13 u^{3/2} + C = \tfrac13 (2x + 1)^{3/2} + C .
> $$
>
> *Solution 2.* Let $u = \sqrt{2x + 1}$. Then $u^2 = 2x + 1$, so $2u\,du = 2\,dx$, that is $dx = u\,du$, and
>
> $$
> \int \sqrt{2x + 1}\,dx = \int u \cdot u\,du = \int u^2\,du = \frac{u^3}{3} + C = \tfrac13 (2x + 1)^{3/2} + C .
> $$
>
> **(b)** Evaluate $\displaystyle\int_0^4 \sqrt{2x + 1}\,dx$.
>
> *Via the indefinite integral and FTC2:*
>
> $$
> \int_0^4 \sqrt{2x + 1}\,dx = \tfrac13 (2x + 1)^{3/2} \Big]_0^4 = \tfrac13 (9)^{3/2} - \tfrac13 (1)^{3/2} = \tfrac13 (27 - 1) = \tfrac{26}{3} .
> $$
>
> *Changing the limits (Theorem §38.3).* With $u = 2x + 1$, $dx = \frac12 du$: when $x = 0$, $u = 1$, and when $x = 4$, $u = 9$. So
>
> $$
> \int_0^4 \sqrt{2x + 1}\,dx = \int_1^9 \tfrac12 \sqrt{u}\,du = \tfrac12 \cdot \tfrac23 u^{3/2} \Big]_1^9 = \tfrac13 \big(9^{3/2} - 1^{3/2}\big) = \tfrac{26}{3} .
> $$
>
> With the second method we do *not* return to $x$ after integrating: the expression in $u$ is evaluated between the new limits.
>
> *Stewart: Examples 5.5.2 and 5.5.7*

^ex-38-3

> [!example] Example §38.4: Changing the Limits
> **(a)** Evaluate $\displaystyle\int_1^2 \frac{dx}{(3 - 5x)^2}$.
>
> Let $u = 3 - 5x$. Then $du = -5\,dx$, so $dx = -\frac15 du$. When $x = 1$, $u = -2$; when $x = 2$, $u = -7$. Thus
>
> $$
> \int_1^2 \frac{dx}{(3 - 5x)^2} = -\frac15 \int_{-2}^{-7} \frac{du}{u^2} = -\frac15 \Big[-\frac1u\Big]_{-2}^{-7} = \frac{1}{5u} \Big]_{-2}^{-7} = \frac15 \Big(-\frac17 + \frac12\Big) = \frac15 \cdot \frac{5}{14} = \frac{1}{14} .
> $$
>
> The new lower limit $-2$ is larger than the upper limit $-7$; Theorem §38.3 does not mind. (The integrand is continuous on $[1, 2]$, since $3 - 5x = 0$ only at $x = \frac35$.)
>
> **(b)** Evaluate $\displaystyle\int_1^e \frac{\ln x}{x}\,dx$.
>
> Let $u = \ln x$, because its differential $du = \frac1x\,dx$ occurs in the integral. When $x = 1$, $u = \ln 1 = 0$; when $x = e$, $u = \ln e = 1$. So
>
> $$
> \int_1^e \frac{\ln x}{x}\,dx = \int_0^1 u\,du = \frac{u^2}{2} \Big]_0^1 = \frac12 .
> $$
>
> Since $(\ln x)/x > 0$ for $x > 1$, this is the area under $y = (\ln x)/x$ from $1$ to $e$.
>
> *Stewart: Examples 5.5.8 and 5.5.9*

^ex-38-4

## Symmetry

Recall ([[§1 Four Ways to Represent a Function|§1]]) that $f$ is **even** if $f(-x) = f(x)$ and **odd** if $f(-x) = -f(x)$ for all $x$ in its domain.

> [!theorem] Theorem §38.4: Integrals of Symmetric Functions
> Suppose $f$ is continuous on $[-a, a]$.
>
> (a) If $f$ is even, then $\displaystyle\int_{-a}^{a} f(x)\,dx = 2 \int_0^a f(x)\,dx$.
>
> (b) If $f$ is odd, then $\displaystyle\int_{-a}^{a} f(x)\,dx = 0$.
>
> *Stewart: 5.5, Theorem 7*

^thm-38-4

> [!remark] Remark: Why It Works
> For $f$ positive and even, the area under $y = f(x)$ from $-a$ to $0$ is the mirror image of the area from $0$ to $a$, so the total is twice the area from $0$ to $a$. For $f$ odd, the graph over $[-a, 0]$ is the graph over $[0, a]$ rotated half a turn about the origin: the area above the axis on one side equals the area below the axis on the other, and in the net area $\int_{-a}^{a} f(x)\,dx$ they cancel.

^rem-38-2

> [!proof]+ Proof
> Split the integral in two, using Property 5 ([[§35 The Definite Integral#^thm-35-5|Theorem §35.5]]) and Definition §35.4:
>
> $$
> \int_{-a}^{a} f(x)\,dx = \int_{-a}^{0} f(x)\,dx + \int_0^a f(x)\,dx = -\int_0^{-a} f(x)\,dx + \int_0^a f(x)\,dx . \qquad (8)
> $$
>
> In the first integral on the far right substitute $u = -x$. Then $du = -dx$, and when $x = -a$, $u = a$. By Theorem §38.3,
>
> $$
> -\int_0^{-a} f(x)\,dx = -\int_0^a f(-u)\,(-du) = \int_0^a f(-u)\,du ,
> $$
>
> so Equation (8) becomes
>
> $$
> \int_{-a}^{a} f(x)\,dx = \int_0^a f(-u)\,du + \int_0^a f(x)\,dx . \qquad (9)
> $$
>
> **(a)** If $f$ is even, $f(-u) = f(u)$, and (9) gives $\displaystyle\int_{-a}^{a} f(x)\,dx = \int_0^a f(u)\,du + \int_0^a f(x)\,dx = 2\int_0^a f(x)\,dx$.
>
> **(b)** If $f$ is odd, $f(-u) = -f(u)$, and (9) gives $\displaystyle\int_{-a}^{a} f(x)\,dx = -\int_0^a f(u)\,du + \int_0^a f(x)\,dx = 0$.
>
> (In both cases the last step uses that the name of the variable of integration does not matter.)

^pf-38-4

*Uses:* [[§35 The Definite Integral#^thm-35-5|§35.5]], [[§35 The Definite Integral#^def-35-4|Def. §35.4]], [[§38 The Substitution Rule#^thm-38-3|§38.3]]

![[m233-38-1.svg]]
*Theorem §38.4. (a) For an even $f$ the region over $[-a, 0]$ is the mirror image of the region over $[0, a]$, so the two areas are equal. (b) For an odd $f$ the region below the axis on $[-a, 0]$ is the region above the axis on $[0, a]$ turned half a turn about the origin; in the net area the two cancel.*

> [!example] Example §38.5: Using Symmetry
> **(a)** $f(x) = x^6 + 1$ satisfies $f(-x) = f(x)$, so it is even, and
>
> $$
> \int_{-2}^{2} (x^6 + 1)\,dx = 2 \int_0^2 (x^6 + 1)\,dx = 2 \Big[\tfrac17 x^7 + x\Big]_0^2 = 2 \Big(\tfrac{128}{7} + 2\Big) = \tfrac{284}{7} .
> $$
>
> **(b)** $f(x) = \dfrac{\tan x}{1 + x^2 + x^4}$ satisfies $f(-x) = \dfrac{-\tan x}{1 + x^2 + x^4} = -f(x)$, so it is odd, and it is continuous on $[-1, 1]$ (since $1 < \pi/2$). Therefore
>
> $$
> \int_{-1}^{1} \frac{\tan x}{1 + x^2 + x^4}\,dx = 0 ,
> $$
>
> although no antiderivative of the integrand is available.
>
> *Stewart: Examples 5.5.10 and 5.5.11*

^ex-38-5
