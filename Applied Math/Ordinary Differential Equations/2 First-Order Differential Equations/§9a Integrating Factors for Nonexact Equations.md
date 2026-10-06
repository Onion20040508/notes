---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 2
section: 9
bdp: "2.6"
aliases: ["BDP 2.6 (cont.)"]
tags: [ordinary-differential-equations, math331]
---
← [[§9 Exact Differential Equations and Integrating Factors]] · ↑ [[· 2 First-Order Differential Equations]] · [[§10 Numerical Approximations꞉ Euler's Method]] →

*Boyce–DiPrima, Section 2.6 · MATH 331 Written HW 2 (Problem 4), Midterm (Fall 2021) Q1.*

The second half of BDP 2.6, continuing [[§9 Exact Differential Equations and Integrating Factors|§9]]: an equation that is not exact can sometimes be made exact by an integrating factor, and the test for exactness then decides whether a given factor works. Equation numbers continue those of [[§9 Exact Differential Equations and Integrating Factors|§9]].

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
> Where $\mu \ne 0$, the solutions of (24), found by [[§9 Exact Differential Equations and Integrating Factors#^thm-9-2|Theorem §9.2]], are solutions of (23).
>
> *BDP: 2.6, equations (25) and (26)*

^prop-9-3

> [!proof]+ Proof
> By [[§9 Exact Differential Equations and Integrating Factors#^thm-9-2|Theorem §9.2]] applied to $\mu M$ and $\mu N$ (whose partial derivatives $(\mu M)_y$ and $(\mu N)_x$ are continuous), (24) is exact on $R$ if and only if (25) holds. By the product rule, (25) reads $\mu_y M + \mu M_y = \mu_x N + \mu N_x$, which rearranges to (26). Finally, if $y = \phi(x)$ solves (24) and $\mu(x, \phi(x)) \ne 0$, dividing (24) by $\mu$ shows that $\phi$ solves (23): the integrating factor can be cancelled.

^pf-9-3

*Uses:* [[§9 Exact Differential Equations and Integrating Factors#^thm-9-2|§9.2]], [[§9a Integrating Factors for Nonexact Equations#^def-9-2|Def. §9.2]]

A partial differential equation such as (26) may have more than one solution, and any of them may be used as an integrating factor ([[§9a Integrating Factors for Nonexact Equations#^ex-9-5|Example §9.5]]). But (26) is ordinarily at least as hard to solve as the original equation (23), so integrating factors can be found in practice only in special cases. The most important are those where $\mu$ depends on only one of the variables.

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
> **(a)** If $\mu$ depends on $x$ only, then $\mu_x = d\mu/dx$ and $\mu_y = 0$, and (26) becomes $-N\,\mu' + (M_y - N_x)\mu = 0$, which is (27). If $(M_y - N_x)/N = P(x)$ depends on $x$ only, (27) is the equation $\mu' = P(x)\mu$, linear and separable in $\mu$ alone, and $\mu(x) = \exp \int P(x)\,dx$ solves it: $\mu' = P(x)\mu$. By [[§9a Integrating Factors for Nonexact Equations#^prop-9-3|Proposition §9.3]] this $\mu$ is an integrating factor.
>
> **(b)** If $\mu$ depends on $y$ only, then $\mu_x = 0$ and $\mu_y = d\mu/dy$, and (26) becomes $M\mu' + (M_y - N_x)\mu = 0$, that is, $\mu' = \dfrac{N_x - M_y}{M}\,\mu = Q(y)\,\mu$. The function $\mu(y) = \exp \int Q(y)\,dy$ satisfies $\mu' = Q(y)\mu$, so it is an integrating factor by [[§9a Integrating Factors for Nonexact Equations#^prop-9-3|Proposition §9.3]].

^pf-9-4

*Uses:* [[§9a Integrating Factors for Nonexact Equations#^prop-9-3|§9.3]]

> [!remark] Remark: Method — Integrating Factors
> If $M + Ny' = 0$ is not exact ($M_y \ne N_x$):
> 1. Compute $(M_y - N_x)/N$. If it depends on $x$ only, take $\mu(x) = \exp \int \frac{M_y - N_x}{N}\,dx$.
> 2. Otherwise compute $(N_x - M_y)/M$. If it depends on $y$ only, take $\mu(y) = \exp \int \frac{N_x - M_y}{M}\,dy$.
> 3. Multiply the equation by $\mu$, check that $(\mu M)_y = (\mu N)_x$, and solve it by the method for exact equations ([[§9 Exact Differential Equations and Integrating Factors#^rem-9-1|Remark: Method — Solving an Exact Equation]]).
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
> depends on $x$ only, so by [[§9a Integrating Factors for Nonexact Equations#^prop-9-4|Proposition §9.4]] there is an integrating factor $\mu(x)$ with $d\mu/dx = \mu/x$ (29); for instance
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
