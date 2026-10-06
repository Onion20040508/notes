---
type: section
subject: "[[Calculus]]"
chapter: 4
section: 32
stewart: "4.8"
aliases: ["Stewart 4.8"]
tags: [calculus]
---
← [[§31 Optimization Problems]] · ↑ [[· 4 Applications of Differentiation]] · [[§33 Antiderivatives]] →

*Stewart, Section 4.8.*

Most equations cannot be solved by a formula. There is the quadratic formula, and there are (very complicated) formulas for degrees $3$ and $4$, but none for polynomials of degree $5$ or higher, and none for a transcendental equation such as $\cos x = x$. Even a practical question, such as the interest rate hidden in a car loan, leads to an equation like $48x(1 + x)^{60} - (1 + x)^{60} + 1 = 0$. Newton's method (the Newton–Raphson method) finds approximate solutions: replace the curve $y = f(x)$ by its tangent line at a first guess (the linearization, [[§23 Linear Approximations and Differentials#^def-23-1|Def. §23.1]]), take the $x$-intercept of the tangent as the next guess, and repeat. It usually converges very fast, and it is at the heart of how calculators and computers solve equations.

## The Method

> [!theorem] Proposition §32.1: The x-Intercept of the Tangent Line
> Let $f$ be differentiable at $x_1$ with $f'(x_1) \ne 0$. Then the tangent line to $y = f(x)$ at $(x_1, f(x_1))$ crosses the $x$-axis at
>
> $$
> x_2 = x_1 - \frac{f(x_1)}{f'(x_1)} .
> $$
>
> *Stewart: 4.8 (text)*

^prop-32-1

> [!proof]+ Proof
> The tangent line $L$ at $(x_1, f(x_1))$ has slope $f'(x_1)$, so its equation is
>
> $$
> y - f(x_1) = f'(x_1)(x - x_1) .
> $$
>
> Its $x$-intercept $x_2$ is the $x$ for which $(x_2, 0)$ lies on $L$: $0 - f(x_1) = f'(x_1)(x_2 - x_1)$. Since $f'(x_1) \ne 0$, we can solve for $x_2$: $x_2 - x_1 = -f(x_1)/f'(x_1)$.

^pf-32-1

*Uses:* [[§12 Derivatives and Rates of Change#^thm-12-2|§12.2]] (equation of the tangent line)

> [!definition] Definition §32.1: Newton's Method
> To approximate a solution $r$ of $f(x) = 0$, start with a first approximation $x_1$ (from a guess, a rough sketch, or a computer graph) and define
>
> $$
> x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \qquad (n = 1, 2, 3, \ldots) \qquad (2)
> $$
>
> as long as $f'(x_n) \ne 0$. By [[§32 Newton's Method#^prop-32-1|Proposition §32.1]], $x_{n+1}$ is the $x$-intercept of the tangent line at $(x_n, f(x_n))$. If the numbers $x_n$ become closer and closer to $r$ as $n$ becomes large, the sequence **converges** to $r$, and we write $\lim_{n \to \infty} x_n = r$ (sequences: [[§69 Sequences#^def-69-2|Def. §69.2]]).
>
> The step from $n$ to $n + 1$ is the same for every $n$: Newton's method is an **iterative** process, well suited to a programmable calculator or a computer.
>
> *Stewart: 4.8, Equation 2*

^def-32-1

![[m233-32-1.svg]]
*Newton's method on a convex increasing curve. The tangent at $(x_1, f(x_1))$ meets the $x$-axis at $x_2$; the tangent at $(x_2, f(x_2))$ meets it at $x_3$, and so on. Each step replaces the curve by its tangent line, and the approximations $x_1 > x_2 > x_3 > \cdots$ close in on the root $r$ from the right.*

> [!remark]- Connections
> - If $x_n \to r$ and $f$, $f'$ are continuous with $f'(r) \ne 0$, letting $n \to \infty$ in (2) gives $r = r - f(r)/f'(r)$, so $f(r) = 0$: a limit of the iteration is a root. This is the argument of [[§9 Limit Theorems for Sequences#^ex-9-6|451 Ex. §9.6]], whose recursion $t_{n+1} = \frac{t_n^2 + 2}{2t_n}$ is Newton's method for $x^2 = 2$.

> [!remark] Remark: When Newton's Method Fails
> For curves like the one in the figure above, the approximations converge to the root. But in some circumstances the sequence may not converge.
> - If $f'(x_1)$ is close to $0$, the tangent line is nearly horizontal, and $x_2$ may be a worse approximation than $x_1$, far from $r$.
> - An approximation may fall outside the domain of $f$, and the method stops.
> - The iteration may run away. For $f(x) = x^{1/3}$, whose only root is $0$, formula (2) gives $x_{n+1} = x_n - \dfrac{x_n^{1/3}}{\frac13 x_n^{-2/3}} = x_n - 3x_n = -2x_n$, so every starting value $x_1 \ne 0$ leads to $|x_n| = 2^{n-1}|x_1| \to \infty$.
>
> In the first two cases a better initial approximation $x_1$ should be chosen. (Stewart's Exercises 31–34 give such examples.)

^rem-32-1

> [!remark] Remark: Method — Newton's Method
> 1. Write the equation in the form $f(x) = 0$ and compute $f'(x)$. Write out formula (2) for this $f$, simplified.
> 2. Choose $x_1$ near the desired root: from a sketch (for $f(x) = g(x) - h(x)$, sketch $y = g(x)$ and $y = h(x)$ and look for the intersection), from a computer graph, or from a sign change of $f$ (Intermediate Value Theorem, [[§10 Continuity#^thm-10-10|Theorem §10.10]]).
> 3. Iterate (2), keeping more decimal places than required.
> 4. **Stopping rule (rule of thumb):** to get a root correct to $k$ decimal places, stop when two successive approximations $x_n$ and $x_{n+1}$ agree to $k$ decimal places. (A precise error estimate is Stewart's Exercise 11.11.39, [[§79 Applications of Taylor Polynomials|§79]].)
> 5. If the approximations wander off or leave the domain, start again with a better $x_1$.

^rem-32-2

## Examples

> [!example] Example §32.1: Newton's Own Example
> Starting with $x_1 = 2$, find the third approximation $x_3$ to the root of $x^3 - 2x - 5 = 0$.
>
> With $f(x) = x^3 - 2x - 5$ and $f'(x) = 3x^2 - 2$, formula (2) becomes
>
> $$
> x_{n+1} = x_n - \frac{x_n^3 - 2x_n - 5}{3x_n^2 - 2} .
> $$
>
> (Newton chose $x_1 = 2$ after some experimentation, because $f(1) = -6$, $f(2) = -1$, $f(3) = 16$.) With $n = 1$,
>
> $$
> x_2 = 2 - \frac{2^3 - 2(2) - 5}{3(2)^2 - 2} = 2 - \frac{-1}{10} = 2.1 .
> $$
>
> (Geometrically: the tangent line at $(2, -1)$ is $y = 10x - 21$, with $x$-intercept $2.1$.) With $n = 2$,
>
> $$
> x_3 = 2.1 - \frac{(2.1)^3 - 2(2.1) - 5}{3(2.1)^2 - 2} = 2.1 - \frac{9.261 - 4.2 - 5}{13.23 - 2} = 2.1 - \frac{0.061}{11.23} \approx 2.0946 .
> $$
>
> This third approximation is already correct to four decimal places (the root is $2.094551\ldots$).
>
> *Stewart: Example 4.8.1*

^ex-32-1

> [!example] Example §32.2: A Sixth Root
> Use Newton's method to find $\sqrt[6]{2}$ correct to eight decimal places.
>
> $\sqrt[6]{2}$ is the positive solution of $x^6 - 2 = 0$. With $f(x) = x^6 - 2$ and $f'(x) = 6x^5$, formula (2) becomes
>
> $$
> x_{n+1} = x_n - \frac{x_n^6 - 2}{6x_n^5} .
> $$
>
> Starting from $x_1 = 1$:
>
> $$
> x_2 \approx 1.16666667, \quad x_3 \approx 1.12644368, \quad x_4 \approx 1.12249707, \quad x_5 \approx 1.12246205, \quad x_6 \approx 1.12246205 .
> $$
>
> (For instance $x_2 = 1 - \frac{1 - 2}{6} = \frac76$.) Since $x_5$ and $x_6$ agree to eight decimal places, $\sqrt[6]{2} \approx 1.12246205$ to eight decimal places.
>
> *Stewart: Example 4.8.2*

^ex-32-2

> [!example] Example §32.3: A Transcendental Equation
> Find, correct to six decimal places, the solution of the equation $\cos x = x$.
>
> In standard form, $\cos x - x = 0$. With $f(x) = \cos x - x$, $f'(x) = -\sin x - 1$, formula (2) becomes
>
> $$
> x_{n+1} = x_n - \frac{\cos x_n - x_n}{-\sin x_n - 1} = x_n + \frac{\cos x_n - x_n}{\sin x_n + 1} .
> $$
>
> **First approximation.** Sketching $y = \cos x$ and $y = x$, they intersect at a point whose $x$-coordinate is somewhat less than $1$ (indeed $f(0) = 1 > 0$ and $f(1) = \cos 1 - 1 < 0$). Take $x_1 = 1$. In radian mode,
>
> $$
> x_2 \approx 0.75036387, \quad x_3 \approx 0.73911289, \quad x_4 \approx 0.73908513, \quad x_5 \approx 0.73908513 .
> $$
>
> Since $x_4$ and $x_5$ agree to six decimal places (eight, in fact), the solution correct to six decimal places is $0.739085$.
>
> A better first approximation saves steps: a computer graph suggests $x_1 = 0.75$, and then $x_2 \approx 0.73911114$, $x_3 \approx 0.73908513$, $x_4 \approx 0.73908513$, the same answer one step sooner.
>
> *Stewart: Example 4.8.3*

^ex-32-3
