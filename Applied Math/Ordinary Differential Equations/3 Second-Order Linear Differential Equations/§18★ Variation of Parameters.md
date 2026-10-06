---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 3
section: 18
bdp: "3.6"
aliases: ["BDP 3.6"]
tags: [ordinary-differential-equations, math331, extension]
---
← [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients]] · ↑ [[· 3 Second-Order Linear Differential Equations]] · [[§19 Mechanical and Electrical Vibrations]] →

*Boyce–DiPrima, Section 3.6 · MATH 331 Written HW 4.*
★ *Beyond MATH 331: the course skipped this section; it is included from Boyce–DiPrima as part of the chapter. [[§18★ Variation of Parameters#^ex-18-2|Example §18.2]] re-solves a Written HW 4 problem that was set for undetermined coefficients.*

Variation of parameters is the second way, after undetermined coefficients, to find a particular solution of $y'' + p(t)y' + q(t)y = g(t)$. Its idea, due to Lagrange, is to replace the constants $c_1, c_2$ in the homogeneous solution $c_1 y_1 + c_2 y_2$ by functions $u_1(t), u_2(t)$ and to impose one extra condition that turns the problem into two linear *algebraic* equations for $u_1'$ and $u_2'$. Unlike undetermined coefficients, it works for any continuous forcing $g$ and for variable coefficients, once a fundamental set $y_1, y_2$ is known. The price is a pair of integrals, which may be hard to evaluate; in exchange the particular solution comes as an explicit integral formula in $g$, the starting point for the convolution and impulse-response picture of Chapter 6.

## A First Example

> [!example] Example §18.1: A Forcing Term Undetermined Coefficients Cannot Handle
> Find the general solution of
>
> $$
> y'' + 4y = 8\tan t, \qquad -\pi/2 < t < \pi/2 . \qquad (1)
> $$
>
> **Why a new method.** $g(t) = 8\tan t = 8\sin t/\cos t$ is a quotient of $\sin t$ and $\cos t$, not a sum or product of exponentials, polynomials, sines and cosines, so the table of trial forms of undetermined coefficients ([[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-4|Theorem §17.4]]) does not apply.
>
> **Homogeneous solution.** $y'' + 4y = 0$ has $r^2 + 4 = 0$, $r = \pm 2i$, so $y_c(t) = c_1\cos(2t) + c_2\sin(2t)$.
>
> **Vary the parameters.** Look for a solution
>
> $$
> y = u_1(t)\cos(2t) + u_2(t)\sin(2t) . \qquad (4)
> $$
>
> Differentiating,
>
> $$
> y' = -2u_1\sin(2t) + 2u_2\cos(2t) + u_1'\cos(2t) + u_2'\sin(2t) .
> $$
>
> One equation (the ODE) cannot determine two functions, so we may impose a second condition of our own. Require the last two terms to vanish:
>
> $$
> u_1'\cos(2t) + u_2'\sin(2t) = 0 . \qquad (6)
> $$
>
> Then $y' = -2u_1\sin(2t) + 2u_2\cos(2t)$ contains no derivatives of $u_1, u_2$, and
>
> $$
> y'' = -4u_1\cos(2t) - 4u_2\sin(2t) - 2u_1'\sin(2t) + 2u_2'\cos(2t) .
> $$
>
> Substituting into (1), the terms $\mp 4u_1\cos(2t)$, $\mp 4u_2\sin(2t)$ cancel and
>
> $$
> -2u_1'\sin(2t) + 2u_2'\cos(2t) = 8\tan t . \qquad (9)
> $$
>
> **Solve the algebraic system (6), (9) for $u_1', u_2'$.** From (6), $u_2' = -u_1'\cos(2t)/\sin(2t)$. Put this into (9) and multiply by $\sin(2t)$: $-2u_1'(\sin^2 2t + \cos^2 2t) = 8\tan t\sin(2t)$, so, with $\sin 2t = 2\sin t\cos t$,
>
> $$
> u_1' = -4\tan t\sin(2t) = -8\sin^2 t, \qquad
> u_2' = 8\sin^2 t\,\frac{\cos(2t)}{\sin(2t)} = \frac{4\sin t\,(2\cos^2 t - 1)}{\cos t} = 4\sin t\Big(2\cos t - \frac{1}{\cos t}\Big) .
> $$
>
> **Integrate.** With $\sin^2 t = \frac12(1 - \cos 2t)$,
>
> $$
> u_1 = -4t + 2\sin(2t) + c_1 = 4\sin t\cos t - 4t + c_1, \qquad
> u_2 = -4\cos^2 t + 4\ln(\cos t) + c_2 ,
> $$
>
> since $\frac{d}{dt}(-4\cos^2 t) = 8\sin t\cos t$ and $\frac{d}{dt}\,4\ln(\cos t) = -4\tan t$ ($\cos t > 0$ on the interval).
>
> **Assemble.** Substituting into (4) and using $2\sin t\cos t = \sin 2t$, $2\cos^2 t = 1 + \cos 2t$:
>
> $$
> y = (2\sin 2t - 4t)\cos 2t + \big(4\ln(\cos t) - 2 - 2\cos 2t\big)\sin 2t + c_1\cos 2t + c_2\sin 2t ,
> $$
>
> that is,
>
> $$
> y = -2\sin(2t) - 4t\cos(2t) + 4\ln(\cos t)\sin(2t) + c_1\cos(2t) + c_2\sin(2t) . \qquad (15)
> $$
>
> The $c_1, c_2$ terms are $y_c$; the other three terms are a particular solution. Since $-2\sin 2t$ is itself a homogeneous solution, it can be absorbed into $c_2$: the shorter $Y(t) = -4t\cos(2t) + 4\ln(\cos t)\sin(2t)$ is also a particular solution (substitution confirms $Y'' + 4Y = 8\tan t$). Its $\ln(\cos t)$ term is one no trial form would have guessed.
>
> *BDP: Example 3.6.1*

^ex-18-1

## The General Method

Consider
$$
y'' + p(t)y' + q(t)y = g(t) \qquad (16)
$$
with $p, q, g$ continuous, and suppose a fundamental set $y_1, y_2$ of the homogeneous equation $y'' + p(t)y' + q(t)y = 0$ is known, so that $y_c = c_1y_1 + c_2y_2$. This is a major assumption: so far only constant-coefficient equations can be solved ([[§13 Homogeneous Differential Equations with Constant Coefficients|§13]]–[[§16 Repeated Roots; Reduction of Order|§16]]). As in [[§18★ Variation of Parameters#^ex-18-1|Example §18.1]], set
$$
y = u_1(t)y_1(t) + u_2(t)y_2(t) , \qquad (19)
$$
impose $u_1'y_1 + u_2'y_2 = 0$ (21), so that $y' = u_1y_1' + u_2y_2'$ (22), and substitute $y''$ (23) into (16). After grouping,
$$
u_1\big(y_1'' + py_1' + qy_1\big) + u_2\big(y_2'' + py_2' + qy_2\big) + u_1'y_1' + u_2'y_2' = g ,
$$
and both parentheses vanish because $y_1, y_2$ solve the homogeneous equation. What is left are two linear algebraic equations for $u_1', u_2'$:
$$
u_1'y_1 + u_2'y_2 = 0, \qquad u_1'y_1' + u_2'y_2' = g . \qquad (21),\ (25)
$$
Their determinant is the Wronskian $W[y_1, y_2] = y_1y_2' - y_1'y_2$, which is nonzero because $y_1, y_2$ is a fundamental set, and Cramer's rule gives
$$
u_1'(t) = -\frac{y_2(t)g(t)}{W[y_1, y_2](t)}, \qquad u_2'(t) = \frac{y_1(t)g(t)}{W[y_1, y_2](t)} . \qquad (26)
$$
Integrating these gives $u_1, u_2$, and (19) is the general solution of (16) when the integrals can be evaluated. In general the answer is a formula with integrals:

> [!theorem] Theorem §18.1: Variation of Parameters
> Consider the nonhomogeneous equation
>
> $$
> y'' + p(t)y' + q(t)y = g(t) . \qquad (28)
> $$
>
> If $p$, $q$ and $g$ are continuous on an open interval $I$, and $y_1$, $y_2$ form a fundamental set of solutions of the homogeneous equation $y'' + p(t)y' + q(t)y = 0$, then a particular solution of (28) is
>
> $$
> Y(t) = -y_1(t)\int_{t_0}^{t} \frac{y_2(s)g(s)}{W[y_1, y_2](s)}\,ds + y_2(t)\int_{t_0}^{t} \frac{y_1(s)g(s)}{W[y_1, y_2](s)}\,ds , \qquad (30)
> $$
>
> where $t_0$ is any conveniently chosen point of $I$. The general solution is
>
> $$
> y = c_1y_1(t) + c_2y_2(t) + Y(t) , \qquad (31)
> $$
>
> as prescribed by Theorem 3.5.2 ([[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-2|Theorem §17.2]]).
>
> *BDP: Theorem 3.6.1*

^thm-18-1

> [!proof]+ Proof
> The derivation above shows how (30) was found; here we check directly that it works.
>
> **The integrands are continuous.** $W = W[y_1, y_2]$ is continuous on $I$, and it is never zero there: since $y_1, y_2$ is a fundamental set, $W$ is not identically zero, and by Abel's theorem ([[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-8|Theorem §14.8]], Theorem 3.2.7) a Wronskian of two solutions is either identically zero or never zero on $I$. So $y_2g/W$ and $y_1g/W$ are continuous on $I$.
>
> **The functions $u_1, u_2$.** Put
>
> $$
> u_1(t) = -\int_{t_0}^{t} \frac{y_2(s)g(s)}{W(s)}\,ds, \qquad u_2(t) = \int_{t_0}^{t} \frac{y_1(s)g(s)}{W(s)}\,ds ,
> $$
>
> so that $Y = u_1y_1 + u_2y_2$. By the Fundamental Theorem of Calculus, $u_1$ and $u_2$ are differentiable with $u_1' = -y_2g/W$ and $u_2' = y_1g/W$. Then
>
> $$
> u_1'y_1 + u_2'y_2 = \frac{-y_2y_1 + y_1y_2}{W}\,g = 0, \qquad
> u_1'y_1' + u_2'y_2' = \frac{-y_2y_1' + y_1y_2'}{W}\,g = \frac{W}{W}\,g = g .
> $$
>
> **Substitute.** By the product rule and the first identity, $Y' = u_1y_1' + u_2y_2' + (u_1'y_1 + u_2'y_2) = u_1y_1' + u_2y_2'$. This is again differentiable, with $Y'' = u_1y_1'' + u_2y_2'' + u_1'y_1' + u_2'y_2'$. Hence
>
> $$
> Y'' + pY' + qY = u_1\big(y_1'' + py_1' + qy_1\big) + u_2\big(y_2'' + py_2' + qy_2\big) + \big(u_1'y_1' + u_2'y_2'\big) = 0 + 0 + g .
> $$
>
> So $Y$ solves (28) on $I$. By Theorem 3.5.2 ([[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-2|Theorem §17.2]]), every solution of (28) is $c_1y_1 + c_2y_2 + Y$, which is (31).

^pf-18-1

*Uses:* [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-8|§14.8]] (Abel's theorem), [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^def-14-3|Def. §14.3]] (fundamental set), [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-2|§17.2]] (Theorem 3.5.2), [[§36 The Fundamental Theorem of Calculus#^thm-36-1|Calc Thm. §36.1]] (FTC, Part 1)

> [!remark]- Connections
> - The derivative of $\int_{t_0}^t h(s)\,ds$ for continuous $h$: [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]] (FTC II).
> - The same method for systems $\mathbf{x}' = \mathbf{P}(t)\mathbf{x} + \mathbf{g}(t)$, with a fundamental matrix in place of $y_1, y_2$: [[§35★ Nonhomogeneous Linear Systems#^thm-35-3|Theorem §35.3]] (BDP 7.9). BDP's footnote points there (Problems 7.9.17–19) for a more natural derivation of the extra condition (21): it is the first row of the system form.
> - See also: [[§2★ Nonhomogeneous Linear Equations#^thm-2-6|341 Thm. §2.6]] (the same method in Powers' review); it solves the radial equations of Poisson's equation in a disk in [[§39 Potential in a Disk#^ex-39-3|341 Ex. §39.3]].

> [!remark] Remark: Method — Variation of Parameters
> To find a particular solution of $y'' + p(t)y' + q(t)y = g(t)$:
> 1. **Standard form.** Divide by the coefficient of $y''$, so that the equation is exactly in the form (28). Otherwise $g$ is misidentified, a common error.
> 2. **Fundamental set.** Find $y_1, y_2$ solving the homogeneous equation and compute $W = y_1y_2' - y_1'y_2$.
> 3. **Solve for $u_1', u_2'$** from $u_1'y_1 + u_2'y_2 = 0$, $u_1'y_1' + u_2'y_2' = g$, that is, (26): $u_1' = -y_2g/W$, $u_2' = y_1g/W$.
> 4. **Integrate** to get $u_1, u_2$. Constants of integration may be dropped (they only add a homogeneous solution), or kept to get the general solution at once. If the integrals cannot be done in closed form, use the definite-integral form (30).
> 5. **Assemble** $Y = u_1y_1 + u_2y_2$ and simplify; terms that are homogeneous solutions may be absorbed into $c_1y_1 + c_2y_2$.
>
> The two possible difficulties are step 2 (finding $y_1, y_2$ when the coefficients are not constant) and step 4 (the integrals). The advantage is that (30) expresses $Y$ for an *arbitrary* forcing $g$, which makes it the natural tool for studying how the response depends on the input.

^rem-18-1

> [!example] Example §18.2: Checking Undetermined Coefficients
> Compute the general solution of
>
> $$
> \frac{d^2y}{dt^2} - 5\frac{dy}{dt} - 14y = e^{4t} .
> $$
>
> **Steps 1–2.** The equation is in standard form with $g(t) = e^{4t}$. $r^2 - 5r - 14 = (r - 7)(r + 2) = 0$ gives $y_1 = e^{7t}$, $y_2 = e^{-2t}$, and
>
> $$
> W = y_1y_2' - y_1'y_2 = e^{7t}(-2e^{-2t}) - 7e^{7t}e^{-2t} = -9e^{5t} .
> $$
>
> **Steps 3–4.**
>
> $$
> u_1' = -\frac{y_2g}{W} = -\frac{e^{-2t}e^{4t}}{-9e^{5t}} = \frac{e^{-3t}}{9}, \quad u_1 = -\frac{e^{-3t}}{27}; \qquad
> u_2' = \frac{y_1g}{W} = \frac{e^{7t}e^{4t}}{-9e^{5t}} = -\frac{e^{6t}}{9}, \quad u_2 = -\frac{e^{6t}}{54} .
> $$
>
> **Step 5.**
>
> $$
> Y = u_1y_1 + u_2y_2 = -\frac{e^{4t}}{27} - \frac{e^{4t}}{54} = -\frac{e^{4t}}{18}, \qquad
> y = c_1e^{7t} + c_2e^{-2t} - \frac{1}{18}e^{4t} .
> $$
>
> This agrees with undetermined coefficients: $Y = Ae^{4t}$ gives $(16 - 20 - 14)A = -18A = 1$, $A = -\frac{1}{18}$. Here undetermined coefficients is quicker; variation of parameters earns its keep when $g$ is not of the tabulated forms, as in Example §18.1.
>
> *Source: 331 Written HW 4, Problem 3 (set for undetermined coefficients)*

^ex-18-2

## Zero Initial Data and the Response to a Forcing

> [!theorem] Corollary §18.2: The Particular Solution with Zero Initial Data
> Let $L[y] = y'' + p(t)y' + q(t)y$ with $p, q, g$ continuous on $I \ni t_0$, and $y_1, y_2$ a fundamental set of $L[y] = 0$. Then the particular solution (30), written as a single integral,
>
> $$
> Y(t) = \int_{t_0}^{t} \frac{y_1(s)y_2(t) - y_1(t)y_2(s)}{y_1(s)y_2'(s) - y_1'(s)y_2(s)}\,g(s)\,ds ,
> $$
>
> is the solution of the initial value problem
>
> $$
> L[y] = g(t), \qquad y(t_0) = 0, \quad y'(t_0) = 0 .
> $$
>
> Consequently the solution of $L[y] = g(t)$, $y(t_0) = y_0$, $y'(t_0) = y_0'$ is $y = u + Y$, where $u$ solves $L[u] = 0$, $u(t_0) = y_0$, $u'(t_0) = y_0'$: the nonhomogeneity in the equation and the one in the initial conditions can be dealt with separately.
>
> *BDP: Problems 3.6.16 and 3.6.17*

^cor-18-2

> [!proof]+ Proof
> In (30), $y_1(t)$ and $y_2(t)$ do not depend on the integration variable $s$, so they can be moved inside the integrals, which then combine into the single integral shown; its denominator is $W[y_1, y_2](s)$.
>
> By [[§18★ Variation of Parameters#^thm-18-1|Theorem §18.1]], $L[Y] = g$. With $u_1, u_2$ as in its proof, $u_1(t_0) = u_2(t_0) = 0$ (integrals over $[t_0, t_0]$), so
>
> $$
> Y(t_0) = u_1(t_0)y_1(t_0) + u_2(t_0)y_2(t_0) = 0, \qquad Y'(t_0) = u_1(t_0)y_1'(t_0) + u_2(t_0)y_2'(t_0) = 0 ,
> $$
>
> using $Y' = u_1y_1' + u_2y_2'$ from the proof of Theorem §18.1.
>
> For the second statement, $u$ exists by the existence and uniqueness theorem ([[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-1|Theorem §14.1]], Theorem 3.2.1). Then $L[u + Y] = L[u] + L[Y] = 0 + g$ by linearity of $L$, and $(u + Y)(t_0) = y_0 + 0$, $(u + Y)'(t_0) = y_0' + 0$. By the uniqueness part of Theorem 3.2.1, $u + Y$ is the solution.

^pf-18-2

*Uses:* [[§18★ Variation of Parameters#^thm-18-1|§18.1]], [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-1|§14.1]] (Theorem 3.2.1)

> [!remark]- Connections
> - See also: [[§2★ Nonhomogeneous Linear Equations#^thm-2-7|341 Thm. §2.7]] (the same integral, with its kernel called the Green's function) and its boundary value version, [[§5★ Green's Functions#^thm-5-1|341 Thm. §5.1]], where the Green's function is built to satisfy conditions at both ends of an interval.

> [!example] Example §18.3: The Forced Equation y″ + y = g(t)
> Show that the solution of $y'' + y = g(t)$, $y(t_0) = 0$, $y'(t_0) = 0$ is
>
> $$
> y = \int_{t_0}^{t} \sin(t - s)\,g(s)\,ds ,
> $$
>
> and solve $y'' + y = g(t)$, $y(0) = y_0$, $y'(0) = y_0'$.
>
> **Zero data.** Take $y_1 = \cos t$, $y_2 = \sin t$, with $W = \cos t\cos t - (-\sin t)\sin t = 1$. The numerator in [[§18★ Variation of Parameters#^cor-18-2|Corollary §18.2]] is
>
> $$
> y_1(s)y_2(t) - y_1(t)y_2(s) = \sin t\cos s - \cos t\sin s = \sin(t - s) ,
> $$
>
> which gives the formula.
>
> **General data.** The homogeneous problem $u'' + u = 0$, $u(0) = y_0$, $u'(0) = y_0'$ has $u = y_0\cos t + y_0'\sin t$. By the second part of Corollary §18.2,
>
> $$
> y = y_0\cos t + y_0'\sin t + \int_0^{t} \sin(t - s)\,g(s)\,ds .
> $$
>
> **The kernel.** The integrand is $K(t - s)\,g(s)$ with $K(t) = \sin t$: the kernel depends only on $t - s$, not on $t$ and $s$ separately. BDP's Problem 3.6.22 shows that this holds for every constant-coefficient operator $L[y] = y'' + by' + cy$: the solution with zero data is $\int_{t_0}^t K(t - s)g(s)\,ds$, where $K$ depends only on $y_1, y_2$. Such an integral is the **convolution** of $K$ and $g$, and once $K$ is known, every forcing reduces to one integral. Chapter 6 recovers this formula with the Laplace transform, where $K$ appears as the impulse response ([[§26★ The Convolution Integral#^thm-26-3|Theorem §26.3]], BDP 6.6).
>
> *BDP: Problems 3.6.18 and 3.6.22*

^ex-18-3
