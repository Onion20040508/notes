---
type: section
subject: "[[Calculus]]"
chapter: 7
section: 44
stewart: "7.1"
aliases: ["Stewart 7.1"]
tags: [calculus]
---
← [[§43 Average Value of a Function]] · ↑ [[· 7 Techniques of Integration]] · [[§45 Trigonometric Integrals]] →

*Stewart, Section 7.1 · MATH 233 (UMass, Spring 2023): Practice Final Set 2 (Q3(b)).*

Every differentiation rule gives an integration rule. The Chain Rule gives the Substitution Rule ([[§38 The Substitution Rule#^thm-38-1|Theorem §38.1]]), and the Product Rule gives **integration by parts**, the second of the two general methods of integration. It trades the integral of $u\,dv$ for the integral of $v\,du$. This helps when $u$ becomes simpler on differentiation and $dv$ can be integrated. Typical integrands are a polynomial times $e^x$, $\sin x$ or $\cos x$, and functions such as $\ln x$ and $\tan^{-1} x$ whose derivatives are algebraic. Repeating the method, or solving the resulting equation for the unknown integral, handles $e^x \sin x$ and produces reduction formulas for powers.

## Integration by Parts: Indefinite Integrals

> [!theorem] Theorem §44.1: Integration by Parts
> If $f$ and $g$ are differentiable, then
>
> $$
> \int f(x)\,g'(x)\,dx = f(x)\,g(x) - \int g(x)\,f'(x)\,dx . \qquad (1)
> $$
>
> With $u = f(x)$ and $v = g(x)$, so that $du = f'(x)\,dx$ and $dv = g'(x)\,dx$, this reads
>
> $$
> \int u\,dv = uv - \int v\,du . \qquad (2)
> $$
>
> *Stewart: 7.1, Formulas 1 and 2*

^thm-44-1

> [!proof]+ Proof
> By the Product Rule ([[§15 The Product and Quotient Rules#^thm-15-1|Theorem §15.1]]),
>
> $$
> \frac{d}{dx}\big[f(x)\,g(x)\big] = f(x)\,g'(x) + g(x)\,f'(x) .
> $$
>
> So $fg$ is an antiderivative of $fg' + gf'$. In the notation of indefinite integrals ([[§37 Indefinite Integrals and the Net Change Theorem#^def-37-1|Definition §37.1]]),
>
> $$
> \int \big[f(x)\,g'(x) + g(x)\,f'(x)\big]\,dx = f(x)\,g(x), \qquad\text{that is,}\qquad \int f(x)\,g'(x)\,dx + \int g(x)\,f'(x)\,dx = f(x)\,g(x) ,
> $$
>
> where both sides are understood up to an additive constant. Rearranging gives (1). Formula (2) is (1) rewritten with $u = f(x)$, $v = g(x)$ and the differentials $du = f'(x)\,dx$, $dv = g'(x)\,dx$, as in the Substitution Rule.

^pf-44-1

*Uses:* [[§15 The Product and Quotient Rules#^thm-15-1|§15.1]] (Product Rule), [[§37 Indefinite Integrals and the Net Change Theorem#^def-37-1|Def. §37.1]] (indefinite integrals), [[§38 The Substitution Rule#^thm-38-1|§38.1]] (differential notation)

> [!remark] Remark: Method — Choosing u and dv
> 1. Write the integrand as a product $u \cdot dv$. Choose $u$ to be a function that becomes simpler when differentiated (or at least no more complicated), as long as $dv$ can readily be integrated to give $v$. Any antiderivative of $dv$ will do for $v$; the constant is added at the end.
> 2. Use the pattern
>
>    $$
>    u = \square \qquad dv = \square \qquad\qquad du = \square \qquad v = \square
>    $$
>
>    and substitute into $uv - \int v\,du$.
> 3. **Polynomial times $e^{x}$, $\sin x$, $\cos x$:** take $u$ = the polynomial. Each application lowers its degree by one, so a polynomial of degree $n$ needs $n$ applications (Example §44.2).
> 4. **$\ln x$, $\tan^{-1} x$, $\sin^{-1} x$ alone:** take $u$ = the function and $dv = dx$. The derivative is algebraic, so $\int v\,du$ is simpler (Example §44.4).
> 5. **Neither factor simplifies** ($e^x \sin x$, $e^x \cos x$): integrate by parts twice, *with the same kind of choice both times*, until the original integral reappears. Then solve the equation for it (Example §44.3).
> 6. Check the answer by differentiating it.
>
> A bad choice makes things worse. In $\int x \sin x\,dx$, the choice $u = \sin x$, $dv = x\,dx$ gives $du = \cos x\,dx$, $v = x^2/2$ and
>
> $$
> \int x \sin x\,dx = \frac{x^2}{2}\sin x - \frac12 \int x^2 \cos x\,dx ,
> $$
>
> which is true but leads to a harder integral.

^rem-44-1

> [!example] Example §44.1: A Polynomial Times a Sine
> Find $\displaystyle\int x \sin x\,dx$.
>
> **With Formula 1.** Take $f(x) = x$ and $g'(x) = \sin x$. Then $f'(x) = 1$ and $g(x) = -\cos x$ (any antiderivative of $g'$ will do). So
>
> $$
> \int x \sin x\,dx = f(x)\,g(x) - \int g(x)\,f'(x)\,dx = x(-\cos x) - \int (-\cos x)\,dx = -x\cos x + \int \cos x\,dx = -x \cos x + \sin x + C .
> $$
>
> **With Formula 2.** Let
>
> $$
> u = x \qquad dv = \sin x\,dx \qquad\qquad du = dx \qquad v = -\cos x .
> $$
>
> Then
>
> $$
> \int x \sin x\,dx = \int \underbrace{x}_{u}\, \underbrace{\sin x\,dx}_{dv} = \underbrace{x}_{u}\,\underbrace{(-\cos x)}_{v} - \int \underbrace{(-\cos x)}_{v}\,\underbrace{dx}_{du} = -x\cos x + \sin x + C .
> $$
>
> **Check.** $\dfrac{d}{dx}(-x\cos x + \sin x) = -\cos x + x \sin x + \cos x = x \sin x$.
>
> *Stewart: Example 7.1.1*

^ex-44-1

> [!example] Example §44.2: Integrating by Parts Twice
> Find $\displaystyle\int t^2 e^t\,dt$.
>
> $e^t$ is unchanged by differentiation and integration, while $t^2$ becomes simpler when differentiated. So take
>
> $$
> u = t^2 \qquad dv = e^t\,dt \qquad\qquad du = 2t\,dt \qquad v = e^t ,
> $$
>
> and
>
> $$
> \int t^2 e^t\,dt = t^2 e^t - 2 \int t\,e^t\,dt . \qquad (3)
> $$
>
> The new integral is simpler but still not obvious, so integrate by parts again, with $u = t$, $dv = e^t\,dt$, $du = dt$, $v = e^t$:
>
> $$
> \int t\,e^t\,dt = t\,e^t - \int e^t\,dt = t\,e^t - e^t + C .
> $$
>
> Putting this into (3),
>
> $$
> \int t^2 e^t\,dt = t^2 e^t - 2(t\,e^t - e^t + C) = t^2 e^t - 2t\,e^t + 2e^t + C_1, \qquad C_1 = -2C .
> $$
>
> **Check.** $\dfrac{d}{dt}\big[(t^2 - 2t + 2)e^t\big] = (2t - 2)e^t + (t^2 - 2t + 2)e^t = t^2 e^t$.
>
> *Stewart: Example 7.1.3*

^ex-44-2

> [!example] Example §44.3: Solving for the Integral
> Evaluate $\displaystyle\int e^x \sin x\,dx$.
>
> Neither factor becomes simpler when differentiated. Try $u = e^x$, $dv = \sin x\,dx$, so $du = e^x\,dx$, $v = -\cos x$:
>
> $$
> \int e^x \sin x\,dx = -e^x \cos x + \int e^x \cos x\,dx . \qquad (4)
> $$
>
> The new integral is no simpler, but no harder either. Integrate by parts again, *again* with $u = e^x$ (now $dv = \cos x\,dx$, $du = e^x\,dx$, $v = \sin x$):
>
> $$
> \int e^x \cos x\,dx = e^x \sin x - \int e^x \sin x\,dx . \qquad (5)
> $$
>
> Putting (5) into (4) returns the original integral:
>
> $$
> \int e^x \sin x\,dx = -e^x \cos x + e^x \sin x - \int e^x \sin x\,dx .
> $$
>
> Regard this as an equation for the unknown integral. Adding $\int e^x \sin x\,dx$ to both sides gives $2\int e^x \sin x\,dx = -e^x \cos x + e^x \sin x$, and dividing by $2$ and adding the constant of integration,
>
> $$
> \int e^x \sin x\,dx = \tfrac12 e^x (\sin x - \cos x) + C .
> $$
>
> (Had we chosen $u = \sin x$ in the second step, (5) would have undone the first step and led back to $0 = 0$. The choice $u = \sin x$, $dv = e^x\,dx$ in *both* steps also works.)
>
> **Check.** $\dfrac{d}{dx}\big[\tfrac12 e^x(\sin x - \cos x)\big] = \tfrac12 e^x(\sin x - \cos x) + \tfrac12 e^x(\cos x + \sin x) = e^x \sin x$. As a visual check, $F(x) = \frac12 e^x(\sin x - \cos x)$ has its maxima and minima exactly where $F'(x) = e^x \sin x = 0$.
>
> *Stewart: Example 7.1.4*

^ex-44-3

## Integration by Parts: Definite Integrals

> [!theorem] Theorem §44.2: Integration by Parts for Definite Integrals
> If $f'$ and $g'$ are continuous on $[a, b]$, then
>
> $$
> \int_a^b f(x)\,g'(x)\,dx = f(x)\,g(x)\Big]_a^b - \int_a^b g(x)\,f'(x)\,dx . \qquad (6)
> $$
>
> *Stewart: 7.1, Formula 6*

^thm-44-2

> [!proof]+ Proof
> By the Product Rule, $(fg)' = fg' + gf'$ on $[a, b]$. The right side is continuous, since $f$, $g$ are continuous (being differentiable) and $f'$, $g'$ are continuous by hypothesis. So Part 2 of the Fundamental Theorem of Calculus ([[§36 The Fundamental Theorem of Calculus#^thm-36-2|Theorem §36.2]]) applies to $fg$:
>
> $$
> \int_a^b \big[f(x)\,g'(x) + g(x)\,f'(x)\big]\,dx = f(x)\,g(x)\Big]_a^b .
> $$
>
> Both $fg'$ and $gf'$ are continuous, hence integrable, so the integral of the sum is the sum of the integrals ([[§35 The Definite Integral#^thm-35-1|Theorem §35.1]], [[§35 The Definite Integral#^thm-35-4|Theorem §35.4]]). Subtracting $\int_a^b g(x) f'(x)\,dx$ from both sides gives (6).

^pf-44-2

*Uses:* [[§15 The Product and Quotient Rules#^thm-15-1|§15.1]] (Product Rule), [[§36 The Fundamental Theorem of Calculus#^thm-36-2|§36.2]] (FTC Part 2), [[§35 The Definite Integral#^thm-35-1|§35.1]], [[§35 The Definite Integral#^thm-35-4|§35.4]] (properties of the integral)

Theorem §44.2 is used, by forward reference, in the proof of the shell formula ([[§41 Volumes by Cylindrical Shells#^pf-41-2|proof of Theorem §41.2]], Stewart's Exercise 7.1.81).

> [!remark]- Connections
> - Rigorous treatment: [[§34 Fundamental Theorem of Calculus#^thm-34-3|451 Thm. §34.3]], under weaker hypotheses ($u$, $v$ continuous on $[a, b]$, differentiable inside, with integrable derivatives), by the same proof.
> - In several variables it becomes Green's first identity, [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-2|452 Thm. §17.2]] (hub [[Green's First Identity]]).

> [!example] Example §44.4: Inverse Functions: dv = dx
> **(a)** Evaluate $\displaystyle\int \ln x\,dx$. **(b)** Calculate $\displaystyle\int_0^1 \tan^{-1} x\,dx$.
>
> **(a)** There is not much choice: $u = \ln x$, $dv = dx$, so $du = \dfrac1x\,dx$, $v = x$, and
>
> $$
> \int \ln x\,dx = x \ln x - \int x \cdot \frac1x\,dx = x \ln x - \int dx = x \ln x - x + C .
> $$
>
> It works because the derivative of $\ln x$ is simpler than $\ln x$. Check: $\frac{d}{dx}(x\ln x - x) = \ln x + 1 - 1 = \ln x$.
>
> **(b)** Let $u = \tan^{-1} x$, $dv = dx$, so $du = \dfrac{dx}{1 + x^2}$, $v = x$. Formula (6) gives
>
> $$
> \int_0^1 \tan^{-1} x\,dx = x \tan^{-1} x\Big]_0^1 - \int_0^1 \frac{x}{1 + x^2}\,dx = 1 \cdot \tan^{-1} 1 - 0 \cdot \tan^{-1} 0 - \int_0^1 \frac{x}{1 + x^2}\,dx = \frac{\pi}{4} - \int_0^1 \frac{x}{1 + x^2}\,dx .
> $$
>
> For the last integral substitute $t = 1 + x^2$ (the letter $u$ is taken). Then $dt = 2x\,dx$, so $x\,dx = \frac12\,dt$; $x = 0$ gives $t = 1$ and $x = 1$ gives $t = 2$:
>
> $$
> \int_0^1 \frac{x}{1 + x^2}\,dx = \frac12 \int_1^2 \frac{dt}{t} = \frac12 \ln|t|\Big]_1^2 = \frac12(\ln 2 - \ln 1) = \frac12 \ln 2 .
> $$
>
> Therefore
>
> $$
> \int_0^1 \tan^{-1} x\,dx = \frac{\pi}{4} - \frac{\ln 2}{2} \approx 0.4388 .
> $$
>
> Since $\tan^{-1} x \ge 0$ for $x \ge 0$, this is the area under $y = \tan^{-1} x$ from $0$ to $1$.
>
> *Stewart: Examples 7.1.2 and 7.1.5*

^ex-44-4

> [!example] Example §44.5: The Work Integral of a Non-Conservative Field
> The work done by $\mathbf{F}(x, y) = e^y \sin x\,\mathbf{i} + e^y \cos x\,\mathbf{j}$ along the segment $\mathbf{r}(t) = \langle \pi t, t \rangle$, $0 \le t \le 1$, from $(0, 0)$ to $(\pi, 1)$ is
>
> $$
> I = \int_0^1 \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt = \int_0^1 \langle e^t \sin \pi t,\ e^t \cos \pi t \rangle \cdot \langle \pi, 1 \rangle\,dt = \int_0^1 e^t\big(\pi \sin \pi t + \cos \pi t\big)\,dt .
> $$
>
> (Line integrals: [[§108 Line Integrals#^def-108-8|Def. §108.8]].) Evaluate $I$.
>
> This is Example §44.3 again: integrate by parts twice, each time with $dv = e^t\,dt$, $v = e^t$, until $I$ reappears.
>
> **First step.** $u = \pi \sin \pi t + \cos \pi t$, $du = (\pi^2 \cos \pi t - \pi \sin \pi t)\,dt = \pi(\pi \cos \pi t - \sin \pi t)\,dt$:
>
> $$
> I = e^t\big(\pi \sin \pi t + \cos \pi t\big)\Big]_0^1 - \pi \int_0^1 e^t\big(\pi \cos \pi t - \sin \pi t\big)\,dt .
> $$
>
> The boundary term is $e(0 - 1) - (0 + 1) = -(e + 1)$.
>
> **Second step.** $u = \pi \cos \pi t - \sin \pi t$, $du = (-\pi^2 \sin \pi t - \pi \cos \pi t)\,dt = -\pi(\pi \sin \pi t + \cos \pi t)\,dt$:
>
> $$
> \int_0^1 e^t\big(\pi \cos \pi t - \sin \pi t\big)\,dt = e^t\big(\pi \cos \pi t - \sin \pi t\big)\Big]_0^1 + \pi \int_0^1 e^t\big(\pi \sin \pi t + \cos \pi t\big)\,dt = -\pi(e + 1) + \pi I ,
> $$
>
> since the boundary term is $e(-\pi - 0) - (\pi - 0) = -\pi(e + 1)$.
>
> **Solve.** Combining, $I = -(e + 1) - \pi\big[-\pi(e + 1) + \pi I\big] = (\pi^2 - 1)(e + 1) - \pi^2 I$, so
>
> $$
> (1 + \pi^2)\,I = (\pi^2 - 1)(e + 1), \qquad I = \frac{(e + 1)(\pi^2 - 1)}{\pi^2 + 1} \approx 3.034 .
> $$
>
> (The field is not conservative, so this value depends on the path, not only on the endpoints; see [[§109 The Fundamental Theorem for Line Integrals#^thm-109-2|Theorem §109.2]]. The same work integral is set up from the field, and evaluated with the two antiderivatives written out, in [[§109 The Fundamental Theorem for Line Integrals#^ex-109-5|Example §109.5]](b).)
>
> *Source: 233 Practice Final Set 2, Q3(b)*

^ex-44-5

## Reduction Formulas

Integration by parts often expresses an integral in terms of a simpler one. When the integrand is a power of a function, it can lower the power.

> [!theorem] Proposition §44.3: Reduction Formula for Powers of Sine
> For every integer $n \ge 2$,
>
> $$
> \int \sin^n x\,dx = -\frac1n \cos x \sin^{n-1} x + \frac{n-1}{n} \int \sin^{n-2} x\,dx . \qquad (7)
> $$
>
> *Stewart: 7.1, Equation 7 (Example 7.1.6)*

^prop-44-3

> [!proof]+ Proof
> Let
>
> $$
> u = \sin^{n-1} x \qquad dv = \sin x\,dx \qquad\qquad du = (n - 1)\sin^{n-2} x \cos x\,dx \qquad v = -\cos x .
> $$
>
> Integration by parts gives
>
> $$
> \int \sin^n x\,dx = -\cos x \sin^{n-1} x + (n - 1) \int \sin^{n-2} x \cos^2 x\,dx .
> $$
>
> Since $\cos^2 x = 1 - \sin^2 x$,
>
> $$
> \int \sin^n x\,dx = -\cos x \sin^{n-1} x + (n - 1) \int \sin^{n-2} x\,dx - (n - 1) \int \sin^n x\,dx .
> $$
>
> As in Example §44.3, solve for the desired integral by moving the last term to the left side:
>
> $$
> n \int \sin^n x\,dx = -\cos x \sin^{n-1} x + (n - 1) \int \sin^{n-2} x\,dx ,
> $$
>
> and divide by $n$.

^pf-44-3

*Uses:* [[§44 Integration by Parts#^thm-44-1|§44.1]]

Applying (7) repeatedly lowers the exponent by $2$ each time, until $\int \sin x\,dx$ (if $n$ is odd) or $\int (\sin x)^0\,dx = \int dx$ (if $n$ is even) is left. For example, with $n = 2$, (7) gives $\int \sin^2 x\,dx = \frac{x}{2} - \frac12 \sin x \cos x + C = \frac{x}{2} - \frac{\sin 2x}{4} + C$. The same method gives reduction formulas for $\int \cos^n x\,dx$, $\int x^n e^x\,dx$, $\int (\ln x)^n\,dx$, $\int \tan^n x\,dx$ and $\int \sec^n x\,dx$ (Stewart's Exercises 54 and 57–60); tables of integrals list such formulas ([[§49 Integration Using Tables and Technology#^prop-49-1|Proposition §49.1]]).
