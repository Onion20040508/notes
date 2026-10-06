---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 2
section: 7
bdp: "2.4"
aliases: ["BDP 2.4"]
tags: [ordinary-differential-equations, math331]
---
← [[§6 Modeling with First-Order Differential Equations]] · ↑ [[· 2 First-Order Differential Equations]] · [[§8 Autonomous Differential Equations and Population Dynamics]] →

*Boyce–DiPrima, Section 2.4 · MATH 331 Midterm (Fall 2021), Q2.*

So far every initial value problem had exactly one solution, given by a formula. This section asks whether that is always so, and finds that linear and nonlinear equations behave very differently. For a linear equation $y' + p(t)y = g(t)$ the solution exists and is unique on every interval where $p$ and $g$ are continuous, and the integrating factor gives it explicitly. For a nonlinear equation $y' = f(t, y)$, continuity of $f$ and $\partial f/\partial y$ still gives a unique solution, but only on some interval around the initial point whose size depends on the initial value, uniqueness can fail when $\partial f/\partial y$ is not continuous, and "the general solution" may miss solutions. The section ends with Bernoulli equations, nonlinear equations that a substitution turns into linear ones.

## Existence and Uniqueness of Solutions

> [!theorem] Theorem §7.1: Existence and Uniqueness for First-Order Linear Equations
> If the functions $p$ and $g$ are continuous on an open interval $I\colon \alpha < t < \beta$ containing the point $t = t_0$, then there exists a unique function $y = \phi(t)$ that satisfies the differential equation
>
> $$
> y' + p(t)\,y = g(t) \qquad (1)
> $$
>
> for each $t$ in $I$, and that also satisfies the initial condition
>
> $$
> y(t_0) = y_0 , \qquad (2)
> $$
>
> where $y_0$ is an arbitrary prescribed initial value.
>
> *BDP: Theorem 2.4.1*

^thm-7-1

> [!proof]+ Proof
> The proof is contained in the derivation of the integrating factor, [[§4 Linear Differential Equations; Method of Integrating Factors#^thm-4-2|Theorem §4.2]] (BDP 2.1, equations (30) and (32)), looked at a little more closely. Let
>
> $$
> \mu(t) = \exp \int p(t)\,dt , \qquad (4)
> $$
>
> where $\int p(t)\,dt$ is any antiderivative of $p$ on $I$; one exists because $p$ is continuous on $I$ (for instance $\int_{t_0}^t p(s)\,ds$). Then $\mu$ is defined, differentiable and nonzero on $I$, with $\mu' = p\mu$.
>
> **Uniqueness.** Let $y$ be any solution of (1) on $I$. Multiplying (1) by $\mu(t)$ gives $\mu y' + \mu p y = \mu g$, that is,
>
> $$
> (\mu(t)\,y)' = \mu(t)\,g(t) . \qquad (5)
> $$
>
> The function $\mu g$ is continuous on $I$, so it has antiderivatives there, and any two of them differ by a constant. Hence
>
> $$
> \mu(t)\,y = \int \mu(t)\,g(t)\,dt + c \qquad (3)
> $$
>
> for some constant $c$: every solution of (1) is given by (3). The initial condition (2) determines $c$, since $\mu(t_0) \ne 0$. So there is at most one solution of the initial value problem.
>
> **Existence.** Conversely, define $y$ by (3), for an antiderivative of $\mu g$ and a constant $c$. Since $\mu g$ is continuous, its antiderivative is differentiable on $I$, and $\mu$ is differentiable and never zero, so $y$ is differentiable throughout $I$. Differentiating $\mu y$ gives (5), and expanding $(\mu y)' = \mu y' + \mu' y = \mu y' + p\mu y$ and dividing by $\mu \ne 0$ gives (1) at every point of $I$. Choosing $c$ so that $y(t_0) = y_0$ (possible because $\mu(t_0) \ne 0$) gives a solution of the initial value problem on all of $I$.

^pf-7-1

*Uses:* [[§4 Linear Differential Equations; Method of Integrating Factors#^thm-4-2|§4.2]] (the integrating factor), [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]] (a continuous function has a differentiable antiderivative), [[§29 The Mean Value Theorem#^cor-29-5|451 Cor. §29.5]] (antiderivatives differ by a constant)

> [!remark]- Connections
> - See also: [[§61 Linear Equations#^thm-61-1|Calc Thm. §61.1]] (Stewart's treatment of the integrating factor, without the interval of existence).
> - The two facts the proof needs from analysis: $\int_{t_0}^t f(s)\,ds$ is differentiable with derivative $f$ when $f$ is continuous, [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]]; and functions with equal derivatives on an interval differ by a constant, [[§29 The Mean Value Theorem#^cor-29-5|451 Cor. §29.5]], which is where uniqueness comes from.

The theorem asserts both the *existence* and the *uniqueness* of the solution, and it says where the solution lives: throughout any interval containing $t_0$ on which $p$ and $g$ are continuous. So a solution can be discontinuous, or fail to exist, only at points where $p$ or $g$ is discontinuous, and such points can usually be seen at a glance.

Choosing the lower limit of integration to be $t_0$ in both integrals makes the formula ready for the initial condition.

> [!theorem] Proposition §7.2: The Solution Formula for a Linear Initial Value Problem
> Let $p$ and $g$ be continuous on $I$, and let
>
> $$
> \mu(t) = \exp \int_{t_0}^{t} p(s)\,ds , \qquad (6)
> $$
>
> so that $\mu(t_0) = 1$. The general solution of (1) on $I$ is
>
> $$
> y = \frac{1}{\mu(t)} \left( \int_{t_0}^{t} \mu(s)\,g(s)\,ds + c \right), \qquad (7)
> $$
>
> and the solution of the initial value problem (1), (2) is
>
> $$
> y = \frac{1}{\mu(t)} \left( \int_{t_0}^{t} \mu(s)\,g(s)\,ds + y_0 \right). \qquad (8)
> $$
>
> *BDP: 2.4, equations (6)–(8)*

^prop-7-2

> [!proof]+ Proof
> Equation (6) defines an integrating factor as in (4), with the antiderivative $\int_{t_0}^t p(s)\,ds$ of $p$; and $\int_{t_0}^t \mu(s) g(s)\,ds$ is an antiderivative of $\mu g$. So (7) is (3) for these choices, and by the proof of [[§7 Differences Between Linear and Nonlinear Differential Equations#^thm-7-1|Theorem §7.1]] it gives all solutions of (1) on $I$. At $t = t_0$ both integrals vanish and $\mu(t_0) = e^0 = 1$, so (7) gives $y(t_0) = c$. The initial condition (2) therefore forces $c = y_0$, which is (8).

^pf-7-2

*Uses:* [[§7 Differences Between Linear and Nonlinear Differential Equations#^thm-7-1|§7.1]]

For a nonlinear equation there is no formula like (8), and [[§7 Differences Between Linear and Nonlinear Differential Equations#^thm-7-1|Theorem §7.1]] must be replaced by a more general theorem. BDP states it here as **Theorem 2.4.2**, the existence and uniqueness theorem for first-order nonlinear equations, and proves it in Section 2.8; it is boxed, with the proof by Picard iteration, as [[§11 The Existence and Uniqueness Theorem#^thm-11-8|Theorem §11.8]]:

$$
\left.\begin{array}{l} f \text{ and } \partial f/\partial y \text{ continuous on a rectangle} \\ \alpha < t < \beta,\ \ \gamma < y < \delta \text{ containing } (t_0, y_0) \end{array}\right\}
\ \Longrightarrow\
\begin{array}{l} \text{in some interval } t_0 - h < t < t_0 + h \text{ inside } (\alpha, \beta) \text{ there is} \\ \text{a unique solution } y = \phi(t) \text{ of } y' = f(t, y),\ y(t_0) = y_0 . \qquad (9) \end{array}
$$

> [!remark] Remark: Reading Theorem 2.4.2
> - **It contains Theorem §7.1.** If the equation is linear, $f(t, y) = -p(t)y + g(t)$ and $\partial f/\partial y = -p(t)$, so continuity of $f$ and $\partial f/\partial y$ is equivalent to continuity of $p$ and $g$. What Theorem 2.4.2 loses is the interval: for a linear equation the solution exists on all of $(\alpha, \beta)$, for a nonlinear one only on some interval $(t_0 - h, t_0 + h)$.
> - **Its hypotheses are sufficient, not necessary.** The conclusion survives under slightly weaker hypotheses on $f$. In fact the *existence* of a solution (but not its uniqueness) follows from the continuity of $f$ alone. (BDP omits the proof of this existence theorem, known as Peano's theorem. What the proof in [[§11 The Existence and Uniqueness Theorem|§11]] actually uses of $\partial f/\partial y$ is the Lipschitz bound of [[§11 The Existence and Uniqueness Theorem#^lem-11-5|Lemma §11.5]].)
> - **Why the proof is harder.** The proof of [[§7 Differences Between Linear and Nonlinear Differential Equations#^thm-7-1|Theorem §7.1]] is easy because the solution of every linear equation is given by the expression (3). There is no such expression for $y' = f(t, y)$, so the solution has to be constructed as a limit ([[§11 The Existence and Uniqueness Theorem|§11]]).

^rem-7-1

> [!theorem] Corollary §7.3: Solution Curves Do Not Cross
> If $f$ and $\partial f/\partial y$ are continuous on a rectangle $R$, then the graphs of two different solutions of $y' = f(t, y)$ in $R$ cannot intersect. The same holds for two different solutions of the linear equation (1) on an interval where $p$ and $g$ are continuous.
>
> *BDP: 2.4 (text)*

^cor-7-3

> [!proof]+ Proof
> Suppose the graphs of two solutions $\phi_1$ and $\phi_2$ meet at a point $(t_0, y_0)$ of $R$. Then both solve the initial value problem $y' = f(t, y)$, $y(t_0) = y_0$. By the uniqueness part of Theorem 2.4.2 ([[§11 The Existence and Uniqueness Theorem#^thm-11-8|Theorem §11.8]]) they agree on an interval around $t_0$; in the linear case [[§7 Differences Between Linear and Nonlinear Differential Equations#^thm-7-1|Theorem §7.1]] makes them agree on the whole interval. So two solutions whose graphs meet are not two different solutions near the meeting point.

^pf-7-3

*Uses:* [[§11 The Existence and Uniqueness Theorem#^thm-11-8|§11.8]], [[§7 Differences Between Linear and Nonlinear Differential Equations#^thm-7-1|§7.1]]

*Forward reference: [[§11 The Existence and Uniqueness Theorem#^thm-11-8|Theorem §11.8]] (BDP Theorem 2.4.2, stated above) is proved later, in [[§11 The Existence and Uniqueness Theorem|§11]] (BDP 2.8).*

> [!remark]- Connections
> - Stewart quotes this uniqueness theorem without proof and uses it the same way, to show that solution curves do not cross: [[§59 Separable Equations#^rem-59-2|Calc Remark: Solution Curves Do Not Cross]].

> [!example] Example §7.1: Where a Linear Problem Has a Solution
> Use [[§7 Differences Between Linear and Nonlinear Differential Equations#^thm-7-1|Theorem §7.1]] to find an interval in which the initial value problem
>
> $$
> t y' + 2y = 4t^2, \qquad y(1) = 2 \qquad (10),\ (11)
> $$
>
> has a unique solution. Then do the same when the initial condition is changed to $y(-1) = 2$.
>
> **Standard form.** Dividing by $t$,
>
> $$
> y' + \frac{2}{t}\,y = 4t ,
> $$
>
> so $p(t) = 2/t$ and $g(t) = 4t$. Here $g$ is continuous for all $t$, while $p$ is continuous only for $t < 0$ and for $t > 0$. The interval $t > 0$ contains the initial point $t_0 = 1$, so Theorem §7.1 guarantees a unique solution on $0 < t < \infty$.
>
> **The solution.** The integrating factor is $\mu(t) = \exp \int (2/t)\,dt = t^2$ (on either half-line), so $(t^2 y)' = 4t^3$, $t^2 y = t^4 + c$ and
>
> $$
> y = t^2 + \frac{c}{t^2} .
> $$
>
> The condition $y(1) = 2$ gives $1 + c = 2$, $c = 1$:
>
> $$
> y = t^2 + \frac{1}{t^2}, \qquad t > 0 . \qquad (12)
> $$
>
> **The other initial point.** With $y(-1) = 2$ the initial point lies in $t < 0$, and Theorem §7.1 gives a unique solution on $-\infty < t < 0$. Again $1 + c = 2$, so the solution is given by the same formula (12), now on the interval $t < 0$. Neither solution can be continued across $t = 0$, where $y \to \infty$.
>
> *BDP: Example 2.4.1*

^ex-7-1

> [!example] Example §7.2: A Nonlinear Problem With and Without a Unique Solution
> Apply Theorem 2.4.2 to the initial value problem
>
> $$
> \frac{dy}{dx} = \frac{3x^2 + 4x + 2}{2(y - 1)}, \qquad y(0) = -1 . \qquad (13)
> $$
>
> Repeat the analysis when the initial condition is changed to $y(0) = 1$.
>
> [[§7 Differences Between Linear and Nonlinear Differential Equations#^thm-7-1|Theorem §7.1]] does not apply, since the equation is nonlinear. For Theorem 2.4.2,
>
> $$
> f(x, y) = \frac{3x^2 + 4x + 2}{2(y - 1)}, \qquad \frac{\partial f}{\partial y}(x, y) = -\frac{3x^2 + 4x + 2}{2(y - 1)^2} .
> $$
>
> Both are continuous everywhere except on the line $y = 1$.
>
> **$y(0) = -1$.** A rectangle can be drawn about $(0, -1)$ that stays below $y = 1$, so on it $f$ and $\partial f/\partial y$ are continuous, and Theorem 2.4.2 gives a unique solution on some interval about $x = 0$. The rectangle can be stretched infinitely far in both $x$ directions, but that does not mean the solution exists for all $x$. Separating the variables ([[§5 Separable Differential Equations#^ex-5-1|Example §5.1]], BDP Example 2.2.2), $2(y - 1)\,dy = (3x^2 + 4x + 2)\,dx$ integrates to
>
> $$
> y^2 - 2y = x^3 + 2x^2 + 2x + c ,
> $$
>
> and $y(0) = -1$ gives $c = 3$. Completing the square, $(y - 1)^2 = x^3 + 2x^2 + 2x + 4 = (x + 2)(x^2 + 2)$, and the root with $y(0) = -1$ is
>
> $$
> y = 1 - \sqrt{(x + 2)(x^2 + 2)} .
> $$
>
> Since $x^2 + 2 > 0$, the radicand is positive exactly for $x > -2$. At $x = -2$ the solution reaches $y = 1$, where $f$ blows up (the tangent is vertical). So the solution exists only for $x > -2$.
>
> **$y(0) = 1$.** Now the initial point lies on the line $y = 1$, and no rectangle about it has $f$ and $\partial f/\partial y$ continuous: Theorem 2.4.2 says nothing. Separating the variables as before, $x = 0$, $y = 1$ give $c = -1$, so
>
> $$
> (y - 1)^2 = x^3 + 2x^2 + 2x = x(x^2 + 2x + 2), \qquad y = 1 \pm \sqrt{x^3 + 2x^2 + 2x} . \qquad (14)
> $$
>
> Since $x^2 + 2x + 2 = (x + 1)^2 + 1 > 0$, both functions are defined for $x \ge 0$; both satisfy the differential equation for $x > 0$ and the initial condition $y(0) = 1$. Two solutions of one initial value problem confirm that Theorem 2.4.2 does not apply.
>
> *BDP: Example 2.4.2*

^ex-7-2

> [!example] Example §7.3: Infinitely Many Solutions of One Initial Value Problem
> Consider
>
> $$
> y' = y^{1/3}, \qquad y(0) = 0 \qquad (15)
> $$
>
> for $t \ge 0$. Apply Theorem 2.4.2, and then solve the problem.
>
> **The theorem.** $f(t, y) = y^{1/3}$ is continuous everywhere, but $\partial f/\partial y = \frac13 y^{-2/3}$ does not exist when $y = 0$, so it is not continuous there. The initial point lies on the $t$-axis, so Theorem 2.4.2 does not apply and no conclusion can be drawn from it. By the second point of [[§7 Differences Between Linear and Nonlinear Differential Equations#^rem-7-1|Remark: Reading Theorem 2.4.2]], the continuity of $f$ does guarantee that solutions exist, though not that there is only one.
>
> **Solving.** The equation is separable: $y^{-1/3}\,dy = dt$ gives $\frac32 y^{2/3} = t + c$, so $y = \big(\frac23 (t + c)\big)^{3/2}$. The initial condition is satisfied if $c = 0$:
>
> $$
> y = \phi_1(t) = \Big(\frac23 t\Big)^{3/2}, \qquad t \ge 0 . \qquad (16)
> $$
>
> On the other hand,
>
> $$
> y = \phi_2(t) = -\Big(\frac23 t\Big)^{3/2}, \quad t \ge 0, \qquad\text{and}\qquad y = \psi(t) = 0, \quad t \ge 0 \qquad (17),\ (18)
> $$
>
> are also solutions. (Check for $\phi_2$: $\phi_2' = -\big(\frac23\big)^{3/2} \frac32 t^{1/2} = -\big(\frac23 t\big)^{1/2}$ and $\phi_2^{1/3} = -\big(\frac23 t\big)^{1/2}$.) More: for any $t_0 > 0$ the functions
>
> $$
> y = \chi(t) = \begin{cases} 0, & 0 \le t < t_0, \\ \pm\Big(\frac23 (t - t_0)\Big)^{3/2}, & t \ge t_0 \end{cases} \qquad (19)
> $$
>
> are continuous and differentiable, also at $t = t_0$, where both one-sided derivatives are $0$ (since $\frac{d}{dt}\big(\frac23(t - t_0)\big)^{3/2} = \big(\frac23(t - t_0)\big)^{1/2} \to 0$). They satisfy (15). So this initial value problem has an infinite family of solutions (figure below).
>
> The nonuniqueness does not contradict Theorem 2.4.2, which is not applicable when the initial point lies on the $t$-axis. If $(t_0, y_0)$ is any point *off* the $t$-axis, then a small rectangle about it avoids $y = 0$, and the theorem guarantees a unique solution of $y' = y^{1/3}$ through $(t_0, y_0)$.
>
> *BDP: Example 2.4.3*

^ex-7-3

![[m331-7-1.svg]]
*Some solutions of $y' = y^{1/3}$, $y(0) = 0$ ([[§7 Differences Between Linear and Nonlinear Differential Equations#^ex-7-3|Example §7.3]]): $\phi_1$ (blue), $\phi_2$ (green), $\psi = 0$ (black), and the functions $\chi$ that rest on the $t$-axis until a time $t_0$ and then leave it upward or downward (red; here $t_0 = 0.6, 1.2, 1.8$). Every point of the $t$-axis is a branching point, which is possible only because $\partial f/\partial y = \frac13 y^{-2/3}$ blows up there.*

## Interval of Existence

By [[§7 Differences Between Linear and Nonlinear Differential Equations#^thm-7-1|Theorem §7.1]], the solution of a linear problem (1), (2) exists throughout any interval about $t_0$ on which $p$ and $g$ are continuous; vertical asymptotes and other discontinuities of the solution can occur only at discontinuities of $p$ or $g$. In [[§7 Differences Between Linear and Nonlinear Differential Equations#^ex-7-1|Example §7.1]] the solutions $y = t^2 + c/t^2$ are asymptotic to the $y$-axis, matching the discontinuity of $p(t) = 2/t$ at $t = 0$, but have no other point where they fail to exist or to be differentiable. The one exception, $c = 0$, gives $y = t^2$, which is continuous even at $t = 0$: a solution may remain continuous at a discontinuity of the coefficients.

For a nonlinear problem satisfying the hypotheses of Theorem 2.4.2, the interval is much harder to find. The solution $y = \phi(t)$ exists as long as the point $(t, \phi(t))$ remains in a region where the hypotheses hold; this is what determines $h$ (in §11, $h = \min(a, b/M)$, [[§11 The Existence and Uniqueness Theorem#^lem-11-4|Lemma §11.4]]). But $\phi$ is usually not known, so it may be impossible to locate $(t, \phi(t))$ with respect to that region, and the interval may have no simple relation to $f$.

> [!example] Example §7.4: The Interval Depends on the Initial Value
> **(a)** Solve the initial value problem
>
> $$
> y' = y^2, \qquad y(0) = 1, \qquad (20)
> $$
>
> and determine the interval in which the solution exists.
>
> Theorem 2.4.2 guarantees a unique solution, since $f(t, y) = y^2$ and $\partial f/\partial y = 2y$ are continuous everywhere. Separating the variables,
>
> $$
> y^{-2}\,dy = dt, \qquad -y^{-1} = t + c, \qquad y = -\frac{1}{t + c} . \qquad (21),\ (22)
> $$
>
> The initial condition requires $c = -1$, so
>
> $$
> y = \frac{1}{1 - t} . \qquad (23)
> $$
>
> The solution becomes unbounded as $t \to 1$, so it exists only on $-\infty < t < 1$. Nothing in the differential equation itself marks the point $t = 1$. With the initial condition $y(0) = y_0 \ne 0$ instead (24), the constant is $c = -1/y_0$ and
>
> $$
> y = \frac{y_0}{1 - y_0 t} . \qquad (25)
> $$
>
> This becomes unbounded as $t \to 1/y_0$: the interval of existence is $-\infty < t < 1/y_0$ if $y_0 > 0$, and $1/y_0 < t < \infty$ if $y_0 < 0$ (for $y_0 = 0$ the solution is $y = 0$ for all $t$). The singularities of the solution of a nonlinear problem depend in an essential way on the initial condition, not only on the equation.
>
> **(b)** The exam problem $\dfrac{dy}{dx} = -6e^{3x}y^2$, $y(0) = 3$, solved in [[§5 Separable Differential Equations#^ex-5-4|Example §5.4]](a), behaves the same way. Theorem 2.4.2 applies everywhere ($f = -6e^{3x}y^2$ and $\partial f/\partial y = -12e^{3x}y$ are continuous in the whole plane), and the solution
>
> $$
> y = \frac{3}{6e^{3x} - 5}
> $$
>
> exists only for $\frac13 \ln \frac56 < x < \infty$, blowing up as $x$ decreases to $\frac13 \ln\frac56 \approx -0.061$. With $y(0) = y_0 > 0$ instead, separating gives $-1/y = -2e^{3x} + 2 - 1/y_0$, that is,
>
> $$
> y = \frac{1}{2e^{3x} - 2 + 1/y_0} ,
> $$
>
> whose denominator vanishes at $x = \frac13 \ln\big(1 - \frac{1}{2y_0}\big)$ when $y_0 > \frac12$, and never when $0 < y_0 \le \frac12$ (it decreases to $1/y_0 - 2 \ge 0$ as $x \to -\infty$ without reaching it). So the solution exists for all $x$ if $y_0 \le \frac12$, and only to the right of a point that moves toward $0$ as $y_0$ grows if $y_0 > \frac12$.
>
> *BDP: Example 2.4.4*
> *Source: 331 Midterm (Fall 2021), Q2*

^ex-7-4

![[m331-7-2.svg]]
*Solutions $y = y_0/(1 - y_0 t)$ of $y' = y^2$ for $y_0 = \pm\frac12, \pm1, \pm2$ (same colour for $\pm y_0$), with the vertical asymptotes $t = 1/y_0$ (dashed). Each solution exists only up to its own asymptote, $t < 1/y_0$ for $y_0 > 0$ and $t > 1/y_0$ for $y_0 < 0$, although $f(t, y) = y^2$ is as smooth as can be. The $t$-axis is the solution $y = 0$; by [[§7 Differences Between Linear and Nonlinear Differential Equations#^cor-7-3|Corollary §7.3]] no other solution touches it.*

## General Solution

For a first-order linear equation a solution containing one arbitrary constant contains all solutions ((7), by [[§7 Differences Between Linear and Nonlinear Differential Equations#^thm-7-1|Theorem §7.1]]). For nonlinear equations this may fail: a formula with an arbitrary constant may miss some solutions.

> [!definition] Definition §7.1: General Solution
> A **general solution** of a first-order differential equation is an expression containing one arbitrary constant from which *all* solutions follow by specifying the constant (as for $y' = ay - b$ in [[§2 Solutions of Some Differential Equations#^def-2-2|Definition §2.2]]). BDP uses the term only for linear equations, where (7) is a general solution.
>
> For nonlinear equations a one-parameter family of solutions need not be a general solution. For $y' = y^2$ ([[§7 Differences Between Linear and Nonlinear Differential Equations#^ex-7-4|Example §7.4]]), the expression (22), $y = -1/(t + c)$, contains an arbitrary constant, but $y = 0$ for all $t$ is also a solution and is not obtained from (22) for any value of $c$. This could be anticipated: rewriting the equation in the form (21) required $y \ne 0$. Such "additional" solutions are common for nonlinear equations.
>
> *BDP: 2.4 (text)*

^def-7-1

## Implicit Solutions

For a linear problem, (8) gives the solution $y = \phi(t)$ explicitly: the value at any $t$ is found by substituting $t$, as long as the antiderivatives can be found. For nonlinear equations the best one can usually hope for is an equation relating $t$ and $y$.

> [!definition] Definition §7.2: Integral; Implicit Solution
> An equation
>
> $$
> F(t, y) = 0 \qquad (26)
> $$
>
> that is satisfied by a solution $y = \phi(t)$ of a differential equation is called an **integral**, or **first integral**, of the differential equation. Its graph is an integral curve, or a family of integral curves. Equation (26) defines the solution **implicitly**: for each $t$, the value $y = \phi(t)$ is found by solving (26) for $y$.
>
> *BDP: 2.4 (text)*

^def-7-2

If (26) is simple enough, for instance quadratic in $y$ as in [[§7 Differences Between Linear and Nonlinear Differential Equations#^ex-7-2|Example §7.2]], it can be solved for $y$ analytically. More often it cannot, and the value of $y$ for a given $t$ must be computed numerically; plotting several such pairs $(t, y)$ sketches the integral curve. Examples §7.2–§7.4 are nonlinear problems whose explicit solution is easy to find; BDP's Examples 2.2.1 and 2.2.3 (in [[§5 Separable Differential Equations|§5]], the second as [[§5 Separable Differential Equations#^ex-5-2|Example §5.2]]) are better left in implicit form, which is the more typical situation. More often than not it is impossible even to find an implicit expression for the solution of a first-order nonlinear equation.

## Graphical or Numerical Construction of Integral Curves

Because exact solutions of nonlinear equations are so rarely available, methods that give approximate solutions or qualitative information are correspondingly important. A direction field ([[§1 Some Basic Mathematical Models; Direction Fields#^def-1-2|Definition §1.2]]) shows the qualitative form of the solutions and the regions of the $ty$-plane where they do something interesting. Graphical methods for autonomous equations follow in [[§8 Autonomous Differential Equations and Population Dynamics|§8]], and the simplest numerical method, Euler's, in [[§10 Numerical Approximations꞉ Euler's Method|§10]]. It is not necessary to study numerical algorithms in order to use the many software packages that plot approximate solutions of initial value problems.

## Summary

> [!remark] Remark: Linear Versus Nonlinear
> The linear equation $y' + p(t)y = g(t)$ has three properties:
> 1. Assuming the coefficients are continuous, there is a general solution ([[§7 Differences Between Linear and Nonlinear Differential Equations#^def-7-1|Definition §7.1]]), containing an arbitrary constant, that includes all solutions of the equation. The solution of an initial value problem is picked out by choosing the constant.
> 2. There is an expression for the solution, (7) or (8). Although it involves two integrations, it gives $y = \phi(t)$ explicitly rather than implicitly.
> 3. The possible points of discontinuity, or singularities, of the solution can be found without solving the problem, as the points of discontinuity of the coefficients. If the coefficients are continuous for all $t$, the solution exists and is differentiable for all $t$.
>
> None of these is true, in general, of nonlinear equations. A nonlinear equation may have a solution involving an arbitrary constant and still have other solutions ([[§7 Differences Between Linear and Nonlinear Differential Equations#^ex-7-4|Example §7.4]]); there is no general formula for its solutions, and integrating it usually gives an equation that defines the solutions only implicitly ([[§7 Differences Between Linear and Nonlinear Differential Equations#^def-7-2|Definition §7.2]]); and its singularities can usually be found only by solving it, and they are likely to depend on the initial condition as well as on the equation (Example §7.4).

^rem-7-2

## Bernoulli Equations

Sometimes a change of the dependent variable converts a nonlinear equation into a linear one. The most important case is the following.

> [!definition] Definition §7.3: Bernoulli Equation
> An equation of the form
>
> $$
> y' + p(t)\,y = q(t)\,y^n
> $$
>
> is called a **Bernoulli equation**, after Jakob Bernoulli. For $n = 0$ it is the linear equation $y' + py = q$, and for $n = 1$ it is the linear equation $y' + (p - q)y = 0$; for other $n$ it is nonlinear.
>
> *BDP: 2.4 (Problems, "Bernoulli Equations"); Problem 2.4.23(a)*

^def-7-3

> [!theorem] Proposition §7.4: The Bernoulli Substitution
> If $n \ne 0, 1$, the substitution $v = y^{1 - n}$ reduces the Bernoulli equation $y' + p(t)y = q(t)y^n$, on any interval where $y \ne 0$, to the linear equation
>
> $$
> v' + (1 - n)\,p(t)\,v = (1 - n)\,q(t) .
> $$
>
> *BDP: Problem 2.4.23(b) (the method goes back to Leibniz, 1696)*

^prop-7-4

> [!proof]+ Proof
> Where $y \ne 0$, the function $v = y^{1-n}$ is differentiable with $v' = (1 - n)y^{-n}y'$ by the chain rule. Multiply the Bernoulli equation by $(1 - n)y^{-n}$:
>
> $$
> (1 - n)y^{-n}y' + (1 - n)p(t)\,y^{1-n} = (1 - n)q(t) ,
> $$
>
> that is, $v' + (1 - n)p(t)v = (1 - n)q(t)$. Conversely, if $v > 0$ solves this linear equation then $y = v^{1/(1-n)}$ solves the Bernoulli equation, by the same computation read backwards.

^pf-7-4

*Uses:* [[§7 Differences Between Linear and Nonlinear Differential Equations#^def-7-3|Def. §7.3]]

> [!remark] Remark: Method — Bernoulli Equations
> 1. Write the equation as $y' + p(t)y = q(t)y^n$ and read off $n$.
> 2. Substitute $v = y^{1-n}$ to get the linear equation $v' + (1 - n)p(t)v = (1 - n)q(t)$ ([[§7 Differences Between Linear and Nonlinear Differential Equations#^prop-7-4|Proposition §7.4]]).
> 3. Solve it with an integrating factor ([[§7 Differences Between Linear and Nonlinear Differential Equations#^prop-7-2|Proposition §7.2]]).
> 4. Return to $y = v^{1/(1-n)}$, and apply the initial condition.
> 5. Check whether $y = 0$ is a solution (it is when $n > 0$); the substitution divides by $y^n$ and loses it.

^rem-7-3

> [!example] Example §7.5: The Logistic Equation as a Bernoulli Equation
> Solve $y' = ry - ky^2$, where $r > 0$ and $k > 0$, with $y(0) = y_0 > 0$. This equation is the logistic equation of population dynamics ([[§8 Autonomous Differential Equations and Population Dynamics#^def-8-3|Definition §8.3]]).
>
> In the form $y' - ry = -ky^2$ it is a Bernoulli equation with $p = -r$, $q = -k$ and $n = 2$. Substitute $v = y^{1-2} = 1/y$:
>
> $$
> v' + (1 - 2)(-r)v = (1 - 2)(-k), \qquad\text{that is,}\qquad v' + rv = k .
> $$
>
> With the integrating factor $e^{rt}$, $(e^{rt}v)' = ke^{rt}$, so $e^{rt}v = \frac{k}{r}e^{rt} + c$ and
>
> $$
> v = \frac{k}{r} + c\,e^{-rt}, \qquad y = \frac{1}{k/r + c\,e^{-rt}} .
> $$
>
> At $t = 0$, $1/y_0 = k/r + c$. Writing $K = r/k$, so that $k/r = 1/K$ and $c = 1/y_0 - 1/K$,
>
> $$
> y = \frac{1}{\dfrac1K + \Big(\dfrac{1}{y_0} - \dfrac1K\Big)e^{-rt}} = \frac{y_0 K}{y_0 + (K - y_0)e^{-rt}} .
> $$
>
> This is the solution of the logistic equation found by partial fractions in [[§8 Autonomous Differential Equations and Population Dynamics#^prop-8-3|Proposition §8.3]]. The substitution assumed $y \ne 0$ and so lost the solution $y = 0$, as in [[§7 Differences Between Linear and Nonlinear Differential Equations#^def-7-1|Definition §7.1]].
>
> *BDP: Problem 2.4.24*

^ex-7-5
