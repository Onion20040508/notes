---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 2
section: 9
bdp: "2.6"
aliases: ["BDP 2.6"]
tags: [ordinary-differential-equations, math331]
---
← [[§8 Autonomous Differential Equations and Population Dynamics]] · ↑ [[· 2 First-Order Differential Equations]] · [[§10 Numerical Approximations꞉ Euler's Method]] →

*Boyce–DiPrima, Section 2.6 · MATH 331 Written HW 2 (Problem 4), Midterm (Fall 2021) Q1.*

An equation $M(x, y) + N(x, y)\,y' = 0$ is exact when its left side is the $x$-derivative of a single function $\psi(x, y)$ along solutions; then the solutions are the level curves $\psi(x, y) = c$. This section gives the test $M_y = N_x$ for exactness on a rectangle, whose proof is also the method for finding $\psi$, and shows how an equation that is not exact can sometimes be made exact by an integrating factor, as linear equations were in [[§4 Linear Differential Equations; Method of Integrating Factors#^thm-4-2|Theorem §4.2]]. In the language of multivariable analysis, $M\,dx + N\,dy$ is a 1-form, exact equations are exact forms, and the test says that on a rectangle closed forms are exact. Equations solvable by elementary methods remain special: most first-order equations are not linear, separable or exact.

## Exact Equations

> [!example] Example §9.1: Recognizing a Derivative
> Solve the differential equation
>
> $$
> 2x + y^2 + 2xyy' = 0 . \qquad (1)
> $$
>
> The equation is neither linear nor separable. But the function $\psi(x, y) = x^2 + xy^2$ has
>
> $$
> 2x + y^2 = \frac{\partial \psi}{\partial x}, \qquad 2xy = \frac{\partial \psi}{\partial y} , \qquad (2)
> $$
>
> so (1) reads
>
> $$
> \frac{\partial \psi}{\partial x} + \frac{\partial \psi}{\partial y}\frac{dy}{dx} = 0 . \qquad (3)
> $$
>
> If $y$ is a function of $x$, the chain rule turns the left side into $d\psi(x, y)/dx$, so (1) becomes
>
> $$
> \frac{d}{dx}\psi(x, y) = \frac{d}{dx}(x^2 + xy^2) = 0 , \qquad (4)
> $$
>
> and integrating,
>
> $$
> \psi(x, y) = x^2 + xy^2 = c , \qquad (5)
> $$
>
> with $c$ an arbitrary constant. The level curves of $\psi$ are the integral curves of (1), and (5) defines its solutions implicitly.
>
> *BDP: Example 2.6.1*

^ex-9-1

> [!definition] Definition §9.1: Exact Differential Equation
> The differential equation
>
> $$
> M(x, y) + N(x, y)\,y' = 0 \qquad (6)
> $$
>
> is **exact** (in a region) if there is a function $\psi(x, y)$ such that
>
> $$
> \frac{\partial \psi}{\partial x}(x, y) = M(x, y), \qquad \frac{\partial \psi}{\partial y}(x, y) = N(x, y) \qquad (7)
> $$
>
> there. The name says that the left side of (6) can be expressed exactly as the derivative of a specific function, $\frac{d}{dx}\psi(x, \phi(x))$, along any solution $y = \phi(x)$.
>
> *BDP: 2.6 (text)*

^def-9-1

> [!theorem] Proposition §9.1: Solutions of an Exact Equation
> If (6) is exact, with $\psi$ as in (7) and $\psi$ continuously differentiable, then (6) is equivalent to
>
> $$
> \frac{d}{dx}\psi(x, \phi(x)) = 0 , \qquad (8)
> $$
>
> and its solutions are given implicitly by
>
> $$
> \psi(x, y) = c , \qquad (9)
> $$
>
> where $c$ is an arbitrary constant: a differentiable function $y = \phi(x)$ on an interval solves (6) if and only if $\psi(x, \phi(x))$ is constant.
>
> *BDP: 2.6, equations (8) and (9)*

^prop-9-1

> [!proof]+ Proof
> Let $y = \phi(x)$ be differentiable on an interval, with its graph in the region. By the chain rule and (7),
>
> $$
> M(x, \phi(x)) + N(x, \phi(x))\,\phi'(x) = \frac{\partial \psi}{\partial x} + \frac{\partial \psi}{\partial y}\frac{d\phi}{dx} = \frac{d}{dx}\psi(x, \phi(x)) .
> $$
>
> So $\phi$ solves (6) exactly when the derivative of $x \mapsto \psi(x, \phi(x))$ vanishes on the interval, that is, (8); and a function with zero derivative on an interval is constant, so (8) says $\psi(x, \phi(x)) = c$.

^pf-9-1

*Uses:* [[§9 Exact Differential Equations and Integrating Factors#^def-9-1|Def. §9.1]], [[§10 Composition of Functions and the Chain Rule#^thm-10-2|452 Thm. §10.2]] (chain rule), [[§29 The Mean Value Theorem#^cor-29-4|451 Cor. §29.4]] (zero derivative means constant)

Whether the relation $\psi(x, y) = c$ really defines $y$ as a differentiable function of $x$ is a separate question; in general terms it does, locally, at points where $\partial\psi/\partial y \ne 0$ (the implicit function theorem, [[§12 The Implicit Function Theorem#^thm-12-1|452 Thm. §12.1]]).

In Example §9.1 it was easy to see that the equation is exact and to find $\psi$. In general one needs a test for exactness and a way to construct $\psi$; the following theorem gives the first, and its proof the second.

> [!theorem] Theorem §9.2: Test for Exactness
> Let the functions $M$, $N$, $M_y$ and $N_x$, where subscripts denote partial derivatives, be continuous in the rectangular region $R\colon \alpha < x < \beta$, $\gamma < y < \delta$. Then equation (6),
>
> $$
> M(x, y) + N(x, y)\,y' = 0 ,
> $$
>
> is an exact differential equation in $R$ if and only if
>
> $$
> M_y(x, y) = N_x(x, y) \qquad (10)
> $$
>
> at each point of $R$. That is, there exists a function $\psi$ satisfying (7), $\psi_x = M$ and $\psi_y = N$, if and only if $M$ and $N$ satisfy (10).
>
> *BDP: Theorem 2.6.1*

^thm-9-2

> [!proof]+ Proof
> **Exact $\Rightarrow$ (10).** Suppose $\psi$ satisfies (7). Computing $M_y$ and $N_x$ from (7),
>
> $$
> M_y(x, y) = \psi_{xy}(x, y), \qquad N_x(x, y) = \psi_{yx}(x, y) . \qquad (11)
> $$
>
> Since $M_y$ and $N_x$ are continuous, so are $\psi_{xy}$ and $\psi_{yx}$. This guarantees their equality (the Schwarz–Clairaut theorem on the open rectangle $R$), and (10) follows.
>
> **(10) $\Rightarrow$ exact.** We construct $\psi$. Integrate the first equation of (7) with respect to $x$, holding $y$ constant:
>
> $$
> \psi(x, y) = Q(x, y) + h(y) , \qquad (12)
> $$
>
> where $Q$ is any differentiable function with $Q_x = M$, for example
>
> $$
> Q(x, y) = \int_{x_0}^{x} M(s, y)\,ds , \qquad (13)
> $$
>
> with $x_0$ a fixed number in $(\alpha, \beta)$. (The segment from $(x_0, y)$ to $(x, y)$ lies in $R$ because $R$ is a rectangle, and $Q_x = M$ by the fundamental theorem of calculus, $M$ being continuous.) The function $h$ of $y$ plays the role of the constant of integration. It remains to choose $h$ so that $\psi_y = N$. Differentiating (12) with respect to $y$ and setting the result equal to $N$,
>
> $$
> \psi_y(x, y) = \frac{\partial Q}{\partial y}(x, y) + h'(y) = N(x, y), \qquad\text{so}\qquad h'(y) = N(x, y) - \frac{\partial Q}{\partial y}(x, y) . \qquad (14)
> $$
>
> To determine $h$ from (14), the right side, despite its appearance, must be a function of $y$ only. Its derivative with respect to $x$ is
>
> $$
> \frac{\partial N}{\partial x}(x, y) - \frac{\partial}{\partial x}\frac{\partial Q}{\partial y}(x, y) . \qquad (15)
> $$
>
> Interchanging the order of differentiation in the second term, this is $\dfrac{\partial N}{\partial x} - \dfrac{\partial}{\partial y}\dfrac{\partial Q}{\partial x} = \dfrac{\partial N}{\partial x} - \dfrac{\partial M}{\partial y}$, which is zero by (10).
>
> (BDP asserts the interchange; here is why it is allowed. It is enough to show that $Q_y$ exists and $Q_y(x, y) = \int_{x_0}^x M_y(s, y)\,ds$, because then $\frac{\partial}{\partial x} Q_y = M_y$ by the fundamental theorem of calculus. Fix $(x, y)$ in $R$ and a closed rectangle $R' \subset R$ containing the segment from $(x_0, y)$ to $(x, y)$ in its interior. For small $k \ne 0$, by the mean value theorem in the second variable, for each $s$ between $x_0$ and $x$
>
> $$
> \frac{M(s, y + k) - M(s, y)}{k} = M_y(s, y + \theta k) \quad\text{for some } \theta = \theta(s) \in (0, 1) .
> $$
>
> $M_y$ is continuous on the closed bounded set $R'$, hence uniformly continuous there: given $\varepsilon > 0$ there is $\eta > 0$ with $|M_y(s, y') - M_y(s, y)| < \varepsilon$ whenever $|y' - y| < \eta$ and the points lie in $R'$. So for $|k| < \eta$ the continuous integrand $(M(s, y + k) - M(s, y))/k$ is within $\varepsilon$ of $M_y(s, y)$ for every $s$, and
>
> $$
> \left| \frac{Q(x, y + k) - Q(x, y)}{k} - \int_{x_0}^{x} M_y(s, y)\,ds \right| \le \varepsilon\,|x - x_0| .
> $$
>
> Letting $\varepsilon \to 0$ gives the formula for $Q_y$.)
>
> So the right side $g(x, y) = N(x, y) - Q_y(x, y)$ of (14) has $g_x = 0$ in $R$. For fixed $y$, $x \mapsto g(x, y)$ has zero derivative on the interval $(\alpha, \beta)$, so it is constant: $g(x, y) = g(x_0, y)$. Since $Q(x_0, y) = 0$ for all $y$, $Q_y(x_0, y) = 0$, and $g(x, y) = N(x_0, y)$, which is a continuous function of $y$ only. Hence (14) is solved by
>
> $$
> h(y) = \int_{y_0}^{y} N(x_0, t)\,dt \qquad (y_0 \in (\gamma, \delta)) ,
> $$
>
> and substituting into (12) gives the required function
>
> $$
> \psi(x, y) = \int_{x_0}^{x} M(s, y)\,ds + \int_{y_0}^{y} N(x_0, t)\,dt ,
> $$
>
> with $\psi_x = Q_x = M$ and $\psi_y = Q_y + h' = (N - g) + g = N$. (This explicit formula is BDP's Problem 13, there with the roles of $x$ and $y$ interchanged: integrate $M$ along $y = y_0$ and $N$ along a vertical segment.)

^pf-9-2

*Uses:* [[§9 Exact Differential Equations and Integrating Factors#^def-9-1|Def. §9.1]], [[§5 Equality of Mixed Partials#^thm-5-1|452 Thm. §5.1]] (Schwarz–Clairaut), [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]] (FTC), [[§29 The Mean Value Theorem#^thm-29-3|451 Thm. §29.3]] (mean value theorem), [[§29 The Mean Value Theorem#^cor-29-4|451 Cor. §29.4]], [[§19 Uniform Continuity#^thm-19-1|451 Thm. §19.1]] (uniform continuity on a closed bounded set; the proof carries over to a closed rectangle with [[§13 Some Topological Concepts in Metric Spaces#^thm-13-3|451 Thm. §13.3]])

> [!remark]- Connections
> - Rigorous treatment in the language of forms: (6) is exact exactly when the 1-form $\omega = M\,dx + N\,dy$ is exact, $\omega = d\psi$, and (10) says $\omega$ is closed, $d\omega = (N_x - M_y)\,dx \wedge dy = 0$ ([[§22 The Algebra of Differential Forms#^def-22-8|452 Def. §22.8]]). The first half of the proof is exact $\Rightarrow$ closed, [[§22 The Algebra of Differential Forms#^prop-22-10|452 Prop. §22.10]] (Clairaut in forms language, [[§22 The Algebra of Differential Forms#^prop-22-9|452 Prop. §22.9]]); the second half is the Poincaré lemma, [[§22 The Algebra of Differential Forms#^prop-22-12|452 Prop. §22.12]], for a rectangle, proved here in full. BDP notes that the region need not be rectangular, only simply connected; the angle form on the punctured plane ([[§22 The Algebra of Differential Forms#^prop-22-11|452 Prop. §22.11]], [[Angle form on the punctured plane]]) is closed but not exact, so some condition on the region is needed.
> - See also: the same test and construction for vector fields in Calculus, where $\psi$ is a potential function of $\mathbf{F} = M\,\mathbf{i} + N\,\mathbf{j}$: [[§109 The Fundamental Theorem for Line Integrals#^thm-109-4|Calc Thm. §109.4]] (necessity), [[§110 Green's Theorem#^thm-110-5|Calc Thm. §110.5]] (sufficiency on simply-connected regions) and [[§109 The Fundamental Theorem for Line Integrals#^rem-109-1|Calc Remark: Method — Finding a Potential Function]].

It is possible to write $\psi$ explicitly as integrals, as at the end of the proof, but in solving specific exact equations it is usually simpler and easier to repeat the steps of the proof.

> [!remark] Remark: Method — Solving an Exact Equation
> For $M(x, y) + N(x, y)\,y' = 0$:
> 1. **Test.** Compute $M_y$ and $N_x$. If $M_y = N_x$ (on a rectangle where $M$, $N$, $M_y$, $N_x$ are continuous), the equation is exact (Theorem §9.2); if not, it is not exact (look for an integrating factor below).
> 2. **Integrate $M$ in $x$.** $\psi(x, y) = \int M(x, y)\,dx + h(y)$, holding $y$ fixed, with an arbitrary function $h(y)$ in place of the constant of integration.
> 3. **Match $N$.** Differentiate in $y$ and set $\psi_y = N$. This determines $h'(y)$; if the equation is exact, every $x$ cancels.
> 4. **Find $h$.** Integrate $h'(y)$. The constant of integration can be omitted: any one $\psi$ will do.
> 5. **Solution.** $\psi(x, y) = c$ gives the solutions implicitly (Proposition §9.1). Apply an initial condition to find $c$, and solve for $y$ if possible.
>
> Steps 2–4 may equally be done the other way round: integrate $N$ in $y$, with an arbitrary function $g(x)$, and match $\psi_x = M$.

^rem-9-1

> [!example] Example §9.2: An Exact Equation
> Solve the differential equation
>
> $$
> (y\cos x + 2xe^y) + (\sin x + x^2e^y - 1)\,y' = 0 . \qquad (16)
> $$
>
> **Test.** With $M = y\cos x + 2xe^y$ and $N = \sin x + x^2e^y - 1$,
>
> $$
> M_y(x, y) = \cos x + 2xe^y = N_x(x, y) ,
> $$
>
> so the equation is exact (all four functions are continuous in the whole plane). So there is a $\psi$ with
>
> $$
> \psi_x(x, y) = y\cos x + 2xe^y, \qquad \psi_y(x, y) = \sin x + x^2e^y - 1 .
> $$
>
> **Integrate the first in $x$:**
>
> $$
> \psi(x, y) = y\sin x + x^2e^y + h(y) . \qquad (17)
> $$
>
> **Match $N$:** $\psi_y(x, y) = \sin x + x^2e^y + h'(y) = \sin x + x^2e^y - 1$, so $h'(y) = -1$ and $h(y) = -y$ (the constant of integration can be omitted, since any $\psi$ will do). Thus $\psi(x, y) = y\sin x + x^2e^y - y$, and the solutions of (16) are given implicitly by
>
> $$
> y\sin x + x^2e^y - y = c . \qquad (18)
> $$
>
> *BDP: Example 2.6.2*

^ex-9-2

> [!example] Example §9.3: Choosing a Parameter to Make an Equation Exact
> Consider the differential equation
>
> $$
> 4xy - 2x + (ax^2 + 1)\frac{dy}{dx} = 0 .
> $$
>
> **(a)** For what value of $a$ is it exact? **(b)** For that $a$, find the general solution (an implicit solution is enough).
>
> **(a)** $M = 4xy - 2x$ and $N = ax^2 + 1$ give $M_y = 4x$ and $N_x = 2ax$. They agree for all $x$ if and only if $a = 2$.
>
> **(b)** With $a = 2$, find $\psi$ with $\psi_x = 4xy - 2x$ and $\psi_y = 2x^2 + 1$. Integrating the first in $x$: $\psi = 2x^2y - x^2 + h(y)$. Then $\psi_y = 2x^2 + h'(y) = 2x^2 + 1$, so $h'(y) = 1$ and $h(y) = y$. The solutions are given by
>
> $$
> 2x^2y - x^2 + y = c ,
> $$
>
> and since this is linear in $y$ it can be solved: $y(2x^2 + 1) = x^2 + c$,
>
> $$
> y = \frac{x^2 + c}{2x^2 + 1} .
> $$
>
> Integrating the second equation first gives the same result: $\psi = \int (2x^2 + 1)\,dy = 2x^2y + y + g(x)$, then $\psi_x = 4xy + g'(x) = 4xy - 2x$, so $g(x) = -x^2$. (Check: with $y = (x^2 + c)/(2x^2 + 1)$, $y' = \dfrac{2x(2x^2 + 1) - 4x(x^2 + c)}{(2x^2 + 1)^2} = \dfrac{2x(1 - 2c)}{(2x^2 + 1)^2}$, and $(4xy - 2x) = \dfrac{4x(x^2 + c) - 2x(2x^2 + 1)}{2x^2 + 1} = \dfrac{2x(2c - 1)}{2x^2 + 1}$, so $M + Ny' = 0$.)
>
> *Source: 331 Midterm (Fall 2021), Q1*

^ex-9-3

> [!example] Example §9.4: All Exact Equations with a Given N
> Find all functions $M(x, y)$ such that the equation
>
> $$
> M(x, y)\,dx + 8xy^3\,dy = 0
> $$
>
> is exact.
>
> Here $N(x, y) = 8xy^3$, so $N_x = 8y^3$. By Theorem §9.2 (in the whole plane, for $M$ with continuous $M_y$), the equation is exact exactly when
>
> $$
> M_y(x, y) = 8y^3 .
> $$
>
> Integrating with respect to $y$, holding $x$ fixed, the "constant" of integration is an arbitrary function of $x$:
>
> $$
> M(x, y) = 2y^4 + h(x) ,
> $$
>
> with $h$ any continuous function of $x$. Every such $M$ works: if $H$ is an antiderivative of $h$, then $\psi(x, y) = 2xy^4 + H(x)$ has $\psi_x = 2y^4 + h(x) = M$ and $\psi_y = 8xy^3 = N$, and the solutions are $2xy^4 + H(x) = c$. Conversely, if the equation is exact then $M_y = N_x = 8y^3$, so $M - 2y^4$ has zero $y$-derivative and depends on $x$ alone.
>
> *Source: 331 Written HW 2, Problem 4*

^ex-9-4

> [!remark]- Remark: Separable Equations Are Exact
> A separable equation $M(x) + N(y)\,y' = 0$ ([[§5 Separable Differential Equations#^def-5-1|Definition §5.1]]) is exact: $M_y = 0 = N_x$. Here $\psi(x, y) = \int M(x)\,dx + \int N(y)\,dy$, and $\psi = c$ is exactly the implicit solution found by separating the variables. (BDP Problem 2.6.14.)

^rem-9-2

## Integrating Factors

An equation that is not exact can sometimes be made exact by multiplying it by a suitable **integrating factor**, which is how linear equations were solved in [[§4 Linear Differential Equations; Method of Integrating Factors#^def-4-2|Definition §4.2]] and [[§4 Linear Differential Equations; Method of Integrating Factors#^thm-4-2|Theorem §4.2]].

> [!definition] Definition §9.2: Integrating Factor
> A function $\mu(x, y)$ is an **integrating factor** for the equation
>
> $$
> M(x, y) + N(x, y)\,y' = 0 \qquad (23)
> $$
>
> if the equation
>
> $$
> \mu(x, y)M(x, y) + \mu(x, y)N(x, y)\,y' = 0 \qquad (24)
> $$
>
> is exact.
>
> *BDP: 2.6 (text)*

^def-9-2

> [!theorem] Proposition §9.3: The Equation for an Integrating Factor
> Let $M$, $N$, $\mu$ and their first partial derivatives be continuous on a rectangle $R$. Then $\mu$ is an integrating factor for (23) on $R$ if and only if
>
> $$
> (\mu M)_y = (\mu N)_x , \qquad (25)
> $$
>
> that is, if and only if $\mu$ satisfies the first-order partial differential equation
>
> $$
> M\mu_y - N\mu_x + (M_y - N_x)\,\mu = 0 . \qquad (26)
> $$
>
> Where $\mu \ne 0$, the solutions of (24), found by Theorem §9.2, are solutions of (23).
>
> *BDP: 2.6, equations (25) and (26)*

^prop-9-3

> [!proof]+ Proof
> By Theorem §9.2 applied to $\mu M$ and $\mu N$ (whose partial derivatives $(\mu M)_y$ and $(\mu N)_x$ are continuous), (24) is exact on $R$ if and only if (25) holds. By the product rule, (25) reads $\mu_y M + \mu M_y = \mu_x N + \mu N_x$, which rearranges to (26). Finally, if $y = \phi(x)$ solves (24) and $\mu(x, \phi(x)) \ne 0$, dividing (24) by $\mu$ shows that $\phi$ solves (23): the integrating factor can be cancelled.

^pf-9-3

*Uses:* [[§9 Exact Differential Equations and Integrating Factors#^thm-9-2|§9.2]], [[§9 Exact Differential Equations and Integrating Factors#^def-9-2|Def. §9.2]]

A partial differential equation such as (26) may have more than one solution, and any of them may be used as an integrating factor (Example §9.5). But (26) is ordinarily at least as hard to solve as the original equation (23), so integrating factors can be found in practice only in special cases. The most important are those where $\mu$ depends on only one of the variables.

> [!theorem] Proposition §9.4: Integrating Factors Depending on One Variable
> (a) If $(M_y - N_x)/N$ is a function of $x$ only, then (23) has an integrating factor $\mu(x)$ that depends on $x$ only, found by solving
>
> $$
> \frac{d\mu}{dx} = \frac{M_y - N_x}{N}\,\mu , \qquad\text{for instance}\qquad \mu(x) = \exp \int \frac{M_y - N_x}{N}\,dx . \qquad (27)
> $$
>
> (b) If $(N_x - M_y)/M = Q$ is a function of $y$ only, then (23) has the integrating factor
>
> $$
> \mu(y) = \exp \int Q(y)\,dy .
> $$
>
> *BDP: 2.6, equation (27); Problem 2.6.17*

^prop-9-4

> [!proof]+ Proof
> **(a)** If $\mu$ depends on $x$ only, then $\mu_x = d\mu/dx$ and $\mu_y = 0$, and (26) becomes $-N\,\mu' + (M_y - N_x)\mu = 0$, which is (27). If $(M_y - N_x)/N = P(x)$ depends on $x$ only, (27) is the equation $\mu' = P(x)\mu$, linear and separable in $\mu$ alone, and $\mu(x) = \exp \int P(x)\,dx$ solves it: $\mu' = P(x)\mu$. By Proposition §9.3 this $\mu$ is an integrating factor.
>
> **(b)** If $\mu$ depends on $y$ only, then $\mu_x = 0$ and $\mu_y = d\mu/dy$, and (26) becomes $M\mu' + (M_y - N_x)\mu = 0$, that is, $\mu' = \dfrac{N_x - M_y}{M}\,\mu = Q(y)\,\mu$. The function $\mu(y) = \exp \int Q(y)\,dy$ satisfies $\mu' = Q(y)\mu$, so it is an integrating factor by Proposition §9.3.

^pf-9-4

*Uses:* [[§9 Exact Differential Equations and Integrating Factors#^prop-9-3|§9.3]]

> [!remark] Remark: Method — Integrating Factors
> If $M + Ny' = 0$ is not exact ($M_y \ne N_x$):
> 1. Compute $(M_y - N_x)/N$. If it depends on $x$ only, take $\mu(x) = \exp \int \frac{M_y - N_x}{N}\,dx$.
> 2. Otherwise compute $(N_x - M_y)/M$. If it depends on $y$ only, take $\mu(y) = \exp \int \frac{N_x - M_y}{M}\,dy$.
> 3. Multiply the equation by $\mu$, check that $(\mu M)_y = (\mu N)_x$, and solve it by the method for exact equations (Remark: Method — Solving an Exact Equation).
> 4. Check whether the curves where $\mu = 0$ or $\mu$ is undefined carry solutions of the original equation that were lost or introduced.
>
> If neither quotient depends on a single variable, an integrating factor may still exist (any solution of (26)), but there is no general way to find one.

^rem-9-3

> [!example] Example §9.5: An Integrating Factor Depending on x
> Show that the equation
>
> $$
> (3xy + y^2) + (x^2 + xy)\,y' = 0 \qquad (19)
> $$
>
> is not exact, then find an integrating factor and solve it.
>
> **Not exact.** $M_y = 3x + 2y$ and $N_x = 2x + y$, which differ. To see that the method for exact equations really fails, seek $\psi$ with
>
> $$
> \psi_x = 3xy + y^2, \qquad \psi_y = x^2 + xy . \qquad (20)
> $$
>
> Integrating the first in $x$, $\psi = \frac32 x^2y + xy^2 + h(y)$ (21); then $\psi_y = \frac32 x^2 + 2xy + h'(y) = x^2 + xy$ requires
>
> $$
> h'(y) = -\tfrac12 x^2 - xy , \qquad (22)
> $$
>
> whose right side depends on $x$ as well as $y$. So no $\psi$ satisfies both equations (20).
>
> **Integrating factor.**
>
> $$
> \frac{M_y - N_x}{N} = \frac{3x + 2y - (2x + y)}{x^2 + xy} = \frac{x + y}{x(x + y)} = \frac1x \qquad (28)
> $$
>
> depends on $x$ only, so by Proposition §9.4 there is an integrating factor $\mu(x)$ with $d\mu/dx = \mu/x$ (29); for instance
>
> $$
> \mu(x) = x . \qquad (30)
> $$
>
> Multiplying (19) by $x$:
>
> $$
> (3x^2y + xy^2) + (x^3 + x^2y)\,y' = 0 , \qquad (31)
> $$
>
> which is exact, since $\frac{\partial}{\partial y}(3x^2y + xy^2) = 3x^2 + 2xy = \frac{\partial}{\partial x}(x^3 + x^2y)$.
>
> **Solve.** Find $\psi$ with $\psi_x = 3x^2y + xy^2$, $\psi_y = x^3 + x^2y$ (32). Integrating the first in $x$, $\psi = x^3y + \frac12 x^2y^2 + h(y)$; then $\psi_y = x^3 + x^2y + h'(y) = x^3 + x^2y$, so $h'(y) = 0$ and $h$ is a constant. The solutions of (31), and hence of (19), are given implicitly by
>
> $$
> x^3y + \tfrac12 x^2y^2 = c . \qquad (33)
> $$
>
> Since (33) is quadratic in $y$, the solutions can also be written explicitly: for $x \ne 0$, $\frac12 x^2 y^2 + x^3 y - c = 0$ gives $y = \dfrac{-x^3 \pm \sqrt{x^6 + 2cx^2}}{x^2}$.
>
> **Another integrating factor.** $\mu(x, y) = \dfrac{1}{xy(2x + y)}$ is also an integrating factor of (19), and it leads to the same solutions, though with much greater difficulty (BDP Problem 2.6.22): integrating factors are not unique.
>
> *BDP: Examples 2.6.3 and 2.6.4*

^ex-9-5
