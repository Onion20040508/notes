---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 2
section: 12
bdp: "2.9"
aliases: ["BDP 2.9"]
tags: [ordinary-differential-equations, math331, extension]
---
← [[§11 The Existence and Uniqueness Theorem]] · ↑ [[· 2 First-Order Differential Equations]] · [[§13 Homogeneous Differential Equations with Constant Coefficients]] →

*Boyce–DiPrima, Section 2.9.*
★ *Beyond MATH 331: the course skipped this section; it is included from Boyce–DiPrima as part of the chapter.*

Some processes are more naturally discrete than continuous: interest is compounded monthly, not continuously, and species whose generations do not overlap breed once a year. Then the state $y_{n+1}$ at step $n + 1$ is a function of $n$ and the previous state $y_n$, a first-order difference equation. Linear difference equations are solved by iteration, and their solutions converge, oscillate or blow up according to the size of the multiplier $\rho$. The nonlinear logistic difference equation $u_{n+1} = \rho u_n(1 - u_n)$ looks like a discrete version of the logistic differential equation of [[§8 Autonomous Differential Equations and Population Dynamics#^def-8-3|§8]], but it behaves very differently: as $\rho$ grows, its stable equilibrium gives way to oscillations of period 2, 4, 8, … and then to chaos. It was one of the first examples of mathematical chaos to be studied in detail.

> [!definition] Definition §12.1: First-Order Difference Equation
> An equation
>
> $$
> y_{n+1} = f(n, y_n), \qquad n = 0, 1, 2, \ldots \qquad (1)
> $$
>
> is a **first-order difference equation**: first-order because $y_{n+1}$ depends on $y_n$ but not on earlier values $y_{n-1}, y_{n-2}, \ldots$. It is **linear** if $f$ is a linear function of $y_n$, and **nonlinear** otherwise.
>
> *BDP: 2.9 (text)*

^def-12-1

> [!definition] Definition §12.1: Solution; Initial Condition
> A **solution** of the difference equation (1) is a sequence of numbers $y_0, y_1, y_2, \ldots$ that satisfies the equation for each $n$. An **initial condition**
>
> $$
> y_0 = \alpha \qquad (2)
> $$
>
> prescribes the first term of the solution sequence.
>
> *BDP: 2.9 (text)*

^def-12-new1

Unlike a differential equation, (1) with an initial condition always has exactly one solution: $y_1 = f(0, y_0)$, $y_2 = f(1, y_1)$, and so on, each term determined by the one before. The questions are about the behaviour of $y_n$ as $n \to \infty$.

> [!definition] Definition §12.2: Iterates
> Suppose $f$ depends only on $y_n$:
>
> $$
> y_{n+1} = f(y_n), \qquad n = 0, 1, 2, \ldots . \qquad (3)
> $$
>
> Then $y_1 = f(y_0)$, $y_2 = f(f(y_0))$, the **second iterate** of the difference equation, sometimes written $f^2(y_0)$, and in general the **$n$th iterate** is $y_n = f(y_{n-1}) = f^n(y_0)$; computing them is **iterating** the difference equation.
>
> *BDP: 2.9 (text)*

^def-12-2

> [!definition] Definition §12.2: Equilibrium Solutions
> Solutions of the difference equation (3) for which $y_n$ has the same value for all $n$ are **equilibrium solutions**. They are found by setting $y_{n+1}$ equal to $y_n$ in (3) and solving
>
> $$
> y_n = f(y_n) \qquad (4)
> $$
>
> for $y_n$.
>
> *BDP: 2.9 (text)*

^def-12-new2

> [!definition] Definition §12.2: Asymptotically Stable and Unstable Equilibria
> An equilibrium solution $y_n = y^{\ast}$ of (3) is **asymptotically stable** if solutions starting sufficiently near $y^{\ast}$ converge to $y^{\ast}$ as $n \to \infty$, and **unstable** if solutions starting arbitrarily near $y^{\ast}$ (other than $y^{\ast}$ itself) move away from it.
>
> *BDP: 2.9 (text)*

^def-12-new3

## Linear Equations

Suppose the population of a species in year $n + 1$ is a positive multiple $\rho_n$ of the population in year $n$, the reproduction rate $\rho_n$ possibly varying from year to year:

$$
y_{n+1} = \rho_n y_n, \qquad n = 0, 1, 2, \ldots . \qquad (5)
$$

> [!theorem] Proposition §12.1: Solution of yₙ₊₁ = ρₙyₙ
> The solution of (5) with initial value $y_0$ is
>
> $$
> y_n = \rho_{n-1}\cdots\rho_0\,y_0, \qquad n = 1, 2, \ldots . \qquad (6)
> $$
>
> If $\rho_n = \rho$ for every $n$, the equation is $y_{n+1} = \rho y_n$ (7), with solution
>
> $$
> y_n = \rho^n y_0 , \qquad (8)
> $$
>
> and for $y_0 \ne 0$
>
> $$
> \lim_{n\to\infty} y_n = \begin{cases} 0, & \text{if } |\rho| < 1; \\ y_0, & \text{if } \rho = 1; \\ \text{does not exist}, & \text{otherwise.} \end{cases} \qquad (9)
> $$
>
> So the equilibrium solution $y_n = 0$ of (7) is asymptotically stable for $|\rho| < 1$ and unstable for $|\rho| > 1$.
>
> *BDP: 2.9, equations (6)–(9)*

^prop-12-1

> [!proof]+ Proof
> By induction: $y_1 = \rho_0 y_0$, and if $y_n = \rho_{n-1}\cdots\rho_0 y_0$ then $y_{n+1} = \rho_n y_n = \rho_n\rho_{n-1}\cdots\rho_0 y_0$. With all $\rho_n = \rho$ this is (8). For (9): $\rho^n \to 0$ if $|\rho| < 1$ and $\rho^n = 1$ if $\rho = 1$; if $\rho = -1$, $y_n = (-1)^n y_0$ alternates between $\pm y_0$; if $|\rho| > 1$, $|y_n| = |\rho|^n|y_0| \to \infty$. In each of the last cases $y_n$ has no limit, since $y_0 \ne 0$. (If $y_0 = 0$, then $y_n = 0$ for all $n$, whatever $\rho$; this is the equilibrium solution.) The stability statement follows, since $|y_n - 0| = |\rho|^n|y_0|$ tends to $0$ or to $\infty$.

^pf-12-1

*Uses:* [[§12★ First-Order Difference Equations#^def-12-new2|Def. §12.2]], [[§12★ First-Order Difference Equations#^def-12-new3|Def. §12.2]], [[§69 Sequences#^thm-69-8|Calc Thm. §69.8]] (the sequence of powers)

Although $\rho_n$ is intrinsically positive for a population, (6) is valid for any $\rho_n$. If $\rho_n = 0$ for some $n$, then $y_{n+1}$ and all later values are zero: the species has become extinct.

Now include immigration or emigration: if $b_n$ is the net increase in year $n$ due to immigration, and the reproduction rate $\rho$ is constant,

$$
y_{n+1} = \rho y_n + b_n, \qquad n = 0, 1, 2, \ldots . \qquad (10)
$$

> [!theorem] Proposition §12.2: Solution of yₙ₊₁ = ρyₙ + bₙ
> The solution of (10) with initial value $y_0$ is
>
> $$
> y_n = \rho^n y_0 + \rho^{n-1}b_0 + \cdots + \rho b_{n-2} + b_{n-1} = \rho^n y_0 + \sum_{j=0}^{n-1} \rho^{n-1-j}b_j . \qquad (11)
> $$
>
> In the special case $b_n = b \ne 0$ for all $n$, that is, for
>
> $$
> y_{n+1} = \rho y_n + b , \qquad (12)
> $$
>
> the solution is $y_n = \rho^n y_0 + (1 + \rho + \rho^2 + \cdots + \rho^{n-1})b$ (13), which for $\rho \ne 1$ can be written
>
> $$
> y_n = \rho^n y_0 + \frac{1 - \rho^n}{1 - \rho}\,b = \rho^n\Big(y_0 - \frac{b}{1 - \rho}\Big) + \frac{b}{1 - \rho} , \qquad (14),\ (15)
> $$
>
> and for $\rho = 1$
>
> $$
> y_n = y_0 + nb . \qquad (16)
> $$
>
> For $\rho \ne 1$, $y_n = b/(1 - \rho)$ is the equilibrium solution of (12). If $|\rho| < 1$, $y_n \to b/(1 - \rho)$ for every $y_0$. If $|\rho| > 1$ or $\rho = -1$, $y_n$ has no limit unless $y_0 = b/(1 - \rho)$. If $\rho = 1$, $y_n$ becomes unbounded.
>
> *BDP: 2.9, equations (11)–(16)*

^prop-12-2

> [!proof]+ Proof
> Iterating, $y_1 = \rho y_0 + b_0$, $y_2 = \rho(\rho y_0 + b_0) + b_1 = \rho^2y_0 + \rho b_0 + b_1$, $y_3 = \rho^3y_0 + \rho^2b_0 + \rho b_1 + b_2$. In general (11) holds by induction: if it holds for $n$, then
>
> $$
> y_{n+1} = \rho\Big(\rho^n y_0 + \sum_{j=0}^{n-1}\rho^{n-1-j}b_j\Big) + b_n = \rho^{n+1}y_0 + \sum_{j=0}^{n-1}\rho^{n-j}b_j + b_n = \rho^{n+1}y_0 + \sum_{j=0}^{n}\rho^{n-j}b_j .
> $$
>
> With $b_j = b$, (11) is (13); for $\rho \ne 1$ the finite geometric sum is $1 + \rho + \cdots + \rho^{n-1} = (1 - \rho^n)/(1 - \rho)$, which gives (14), and rearranging gives (15); for $\rho = 1$ the sum is $n$, which gives (16). The constant $y^* = b/(1 - \rho)$ satisfies $\rho y^* + b = \big(\rho b + b(1 - \rho)\big)/(1 - \rho) = y^*$, so it is an equilibrium solution. The limits follow from (15) and [[§12★ First-Order Difference Equations#^prop-12-1|Proposition §12.1]] applied to $\rho^n\big(y_0 - b/(1 - \rho)\big)$, and from (16) with $b \ne 0$.

^pf-12-2

*Uses:* [[§12★ First-Order Difference Equations#^prop-12-1|§12.1]], [[§12★ First-Order Difference Equations#^def-12-new2|Def. §12.2]]

In (11) the first term represents the descendants of the original population, the others the population resulting from immigration in all preceding years; in (14) the two terms are the effects of the original population and of immigration.

> [!remark]- Connections
> - Linear difference equations of any order are treated in Applied Linear Algebra, [[§30 Applications to Difference Equations#^def-30-3|235 Def. §30.3]]: the existence and uniqueness of solutions by recursion is [[§30 Applications to Difference Equations#^thm-30-4|235 Thm. §30.4]], and the general solution of a nonhomogeneous equation is a particular solution plus the general homogeneous solution, [[§30 Applications to Difference Equations#^thm-30-7|235 Thm. §30.7]]. Formula (15) is exactly this for the first-order equation (12): the equilibrium $b/(1 - \rho)$ is a particular solution and $c\rho^n$ the general homogeneous solution.
> - The vector version $\mathbf{x}_{k+1} = A\mathbf{x}_k$, where the eigenvalues of $A$ play the role of $\rho$ and $|\lambda| < 1$ makes the origin an attractor: [[§37 Discrete Dynamical Systems#^prop-37-3|235 Prop. §37.3]].

The same model gives a framework for many problems of a financial character: $y_n$ is the account balance in the $n$th period, $\rho_n = 1 + r_n$ with $r_n$ the interest rate for that period, and $b_n$ the amount deposited or withdrawn. The continuous model of compound interest, [[§6 Modeling with First-Order Differential Equations#^prop-6-1|Proposition §6.1]], is only an approximation to this discrete process (compare [[§6 Modeling with First-Order Differential Equations#^prop-6-2|Proposition §6.2]], compounding $m$ times a year).

> [!example] Example §12.1: Paying Off a Car Loan
> A recent college graduate takes out a \$10,000 loan to purchase a car. If the interest rate is 12%, what monthly payment is required to pay off the loan in 4 years?
>
> **The model.** Let $y_n$ be the loan balance outstanding in the $n$th month. The difference equation is (12) with $\rho = 1 + r$, where $r = 0.12/12 = 0.01$ is the monthly interest rate, so $\rho = 1.01$; and $b$ is the effect of the monthly payment. Payments reduce the balance, so $b$ is negative and the actual payment is $|b|$.
>
> **The solution.** By (15) with $y_0 = 10{,}000$ and $b/(1 - \rho) = b/(-0.01) = -100b$,
>
> $$
> y_n = (1.01)^n(10{,}000 + 100b) - 100b . \qquad (17)
> $$
>
> **The payment.** Setting $y_{48} = 0$: $(1.01)^{48}(10{,}000 + 100b) = 100b$, so $100b\big((1.01)^{48} - 1\big) = -10{,}000\,(1.01)^{48}$ and
>
> $$
> b = -100\,\frac{(1.01)^{48}}{(1.01)^{48} - 1} = -100 \cdot \frac{1.612226}{0.612226} \cong -263.34 . \qquad (18)
> $$
>
> The monthly payment is \$263.34. The total amount paid is 48 times \$263.34, or \$12,640.32; of this, \$10,000 repays the principal and the remaining \$2,640.32 is interest.
>
> *BDP: Example 2.9.1*

^ex-12-1

## Nonlinear Equations: the Logistic Difference Equation

Nonlinear difference equations are much more complicated and have much more varied solutions than linear ones. BDP restricts attention to a single equation.

> [!definition] Definition §12.3: Logistic Difference Equation
> The **logistic difference equation** is
>
> $$
> y_{n+1} = \rho y_n\Big(1 - \frac{y_n}{k}\Big) , \qquad (19)
> $$
>
> the analogue of the logistic differential equation ([[§8 Autonomous Differential Equations and Population Dynamics#^def-8-3|Definition §8.3]])
>
> $$
> \frac{dy}{dt} = ry\Big(1 - \frac yK\Big) . \qquad (20)
> $$
>
> With the scaled variable $u_n = y_n/k$, (19) becomes
>
> $$
> u_{n+1} = \rho u_n(1 - u_n) , \qquad (21)
> $$
>
> where $\rho$ is a positive parameter.
>
> *BDP: 2.9, equations (19)–(21)*

^def-12-3

> [!theorem] Proposition §12.3: Euler's Method Turns the Logistic Equation into a Difference Equation
> If the derivative $dy/dt$ in (20) is replaced by the difference quotient $(y_{n+1} - y_n)/h$ (Euler's method with step $h$, [[§10 Numerical Approximations꞉ Euler's Method#^def-10-1|Definition §10.1]]), then (20) becomes (19) with
>
> $$
> \rho = 1 + hr, \qquad k = \frac{(1 + hr)K}{hr} .
> $$
>
> *BDP: 2.9 (text)*

^prop-12-3

> [!proof]+ Proof
> The replacement gives $y_{n+1} = y_n + hry_n(1 - y_n/K) = (1 + hr)y_n - \dfrac{hr}{K}y_n^2$. Factoring out $(1 + hr)y_n$,
>
> $$
> y_{n+1} = (1 + hr)\,y_n\Big(1 - \frac{hr}{(1 + hr)K}\,y_n\Big) = \rho y_n\Big(1 - \frac{y_n}{k}\Big)
> $$
>
> with $\rho$ and $k$ as stated.

^pf-12-3

*Uses:* [[§10 Numerical Approximations꞉ Euler's Method#^def-10-1|Def. §10.1]], [[§12★ First-Order Difference Equations#^def-12-3|Def. §12.3]]

> [!theorem] Proposition §12.4: Equilibria of the Logistic Difference Equation
> The equilibrium solutions of (21) are
>
> $$
> u_n = 0 \qquad\text{and}\qquad u_n = \frac{\rho - 1}{\rho} . \qquad (23)
> $$
>
> *BDP: 2.9, equations (22) and (23)*

^prop-12-4

> [!proof]+ Proof
> Setting $u_{n+1} = u_n = u$ in (21), the analogue of setting $dy/dt = 0$ in (20), gives
>
> $$
> u = \rho u - \rho u^2 , \qquad (22)
> $$
>
> that is, $u\big(\rho u - (\rho - 1)\big) = 0$, so $u = 0$ or $u = (\rho - 1)/\rho$.

^pf-12-4

*Uses:* [[§12★ First-Order Difference Equations#^def-12-new2|Def. §12.2]]

Are these equilibrium solutions asymptotically stable? BDP answers by linearizing; the following lemma, which BDP does not state, makes the linearization argument rigorous.

> [!theorem] Lemma §12.5: Stability of an Equilibrium of an Iteration
> Let $g$ have a continuous derivative near $u^*$, with $g(u^*) = u^*$, and consider $u_{n+1} = g(u_n)$.
> - If $|g'(u^*)| < 1$, then $u^*$ is asymptotically stable: there are $\delta > 0$ and $\lambda < 1$ such that $|u_n - u^*| \le \lambda^n|u_0 - u^*|$ whenever $|u_0 - u^*| \le \delta$.
> - If $|g'(u^*)| > 1$, then $u^*$ is unstable: there is $\delta > 0$ such that every solution with $0 < |u_0 - u^*| \le \delta$ eventually leaves the interval $|u - u^*| \le \delta$.
>
> *BDP: 2.9 (implicit in the linearizations (24)–(27))*

^lem-12-5

> [!proof]+ Proof
> **$|g'(u^{\ast})| < 1$.** Choose $\lambda$ with $|g'(u^{\ast})| < \lambda < 1$. By continuity of $g'$ there is $\delta > 0$ with $|g'(u)| \le \lambda$ for $|u - u^{\ast}| \le \delta$. If $|u - u^{\ast}| \le \delta$, the mean value theorem gives $\xi$ between $u$ and $u^{\ast}$ with
>
> $$
> |g(u) - u^*| = |g(u) - g(u^*)| = |g'(\xi)|\,|u - u^*| \le \lambda|u - u^*| \le \delta .
> $$
>
> So the iterates stay in the interval, and by induction $|u_n - u^*| \le \lambda^n|u_0 - u^*| \to 0$.
>
> **$|g'(u^{\ast})| > 1$.** Choose $\lambda$ with $1 < \lambda < |g'(u^{\ast})|$ and $\delta > 0$ with $|g'(u)| \ge \lambda$ for $|u - u^{\ast}| \le \delta$. As long as $u_n$ stays in $|u - u^{\ast}| \le \delta$, the mean value theorem gives $|u_{n+1} - u^{\ast}| \ge \lambda|u_n - u^{\ast}|$, so $|u_n - u^{\ast}| \ge \lambda^n|u_0 - u^{\ast}|$. Since $\lambda^n \to \infty$ and $u_0 \ne u^{\ast}$, this cannot continue forever: the solution leaves the interval.

^pf-12-5

*Uses:* [[§12★ First-Order Difference Equations#^def-12-new3|Def. §12.2]], [[§29 The Mean Value Theorem#^thm-29-3|451 Thm. §29.3]] (mean value theorem)

> [!remark] Remark: Why It Works
> This is BDP's argument. Near the equilibrium $u_n = 0$, $u_n^2$ is small compared with $u_n$, and neglecting the quadratic term in (21) leaves the linear equation
>
> $$
> u_{n+1} = \rho u_n , \qquad (24)
> $$
>
> presumably a good approximation for $u_n$ near zero. By (9), $u_n \to 0$ if and only if $|\rho| < 1$, that is $0 < \rho < 1$; so $0$ is asymptotically stable for these $\rho$. Near the other equilibrium write
>
> $$
> u_n = \frac{\rho - 1}{\rho} + v_n \qquad (25)
> $$
>
> with $v_n$ small. Substituting in (21): $1 - u_n = \frac1\rho - v_n$, so $\rho u_n(1 - u_n) = \big((\rho - 1) + \rho v_n\big)\big(\frac1\rho - v_n\big) = \frac{\rho - 1}{\rho} + (2 - \rho)v_n - \rho v_n^2$, that is,
>
> $$
> v_{n+1} = (2 - \rho)v_n - \rho v_n^2 . \qquad (26)
> $$
>
> Neglecting the quadratic term, $v_{n+1} = (2 - \rho)v_n$ (27), and by (9) $v_n \to 0$ for $|2 - \rho| < 1$, that is $1 < \rho < 3$. What this argument lacks is a theorem saying that the solutions of the nonlinear equation resemble those of the linear one near the equilibrium (for differential equations this is done in BDP's Section 9.3). [[§12★ First-Order Difference Equations#^lem-12-5|Lemma §12.5]] is that theorem for iterations: $2 - \rho$ and $\rho$ are exactly the values of $g'$ at the two equilibria.

^rem-12-1

> [!theorem] Proposition §12.6: Stability for the Logistic Difference Equation
> For $u_{n+1} = \rho u_n(1 - u_n)$ with $\rho > 0$:
> - the equilibrium solution $u_n = 0$ is asymptotically stable for $0 < \rho < 1$ and unstable for $\rho > 1$;
> - the equilibrium solution $u_n = (\rho - 1)/\rho$ is asymptotically stable for $1 < \rho < 3$, and unstable for $\rho < 1$ and for $\rho > 3$.
>
> *BDP: 2.9 (text, from the linearizations (24) and (27))*

^prop-12-6

> [!proof]+ Proof
> Here $g(u) = \rho u(1 - u)$ and $g'(u) = \rho(1 - 2u)$. At $u = 0$, $g'(0) = \rho$, which is less than $1$ in absolute value for $0 < \rho < 1$ and greater than $1$ for $\rho > 1$. At $u^* = (\rho - 1)/\rho$, $g'(u^*) = \rho\big(1 - 2(\rho - 1)/\rho\big) = \rho - 2(\rho - 1) = 2 - \rho$, and $|2 - \rho| < 1$ if and only if $1 < \rho < 3$, while $|2 - \rho| > 1$ for $\rho < 1$ and for $\rho > 3$. [[§12★ First-Order Difference Equations#^lem-12-5|Lemma §12.5]] gives the conclusions.

^pf-12-6

*Uses:* [[§12★ First-Order Difference Equations#^lem-12-5|§12.5]], [[§12★ First-Order Difference Equations#^prop-12-4|§12.4]]

At $\rho = 1$ the two equilibria coincide at $u = 0$ and $g'(0) = 1$, so [[§12★ First-Order Difference Equations#^lem-12-5|Lemma §12.5]] does not decide. For $0 < u_0 < 1$ the iterates $u_{n+1} = u_n - u_n^2$ decrease and stay positive, so they converge, and the limit $L$ satisfies $L = L - L^2$, so $L = 0$: the equilibrium attracts every population in $(0, 1)$, which is BDP's statement that it is asymptotically stable. (For $u_0 < 0$, outside the population range, $u_{n+1} = u_n - u_n^2 < u_n$ and the iterates decrease to $-\infty$, so the attraction is one-sided.)

> [!remark] Remark: Method — Stairstep (Cobweb) Diagrams
> To display the solution of $u_{n+1} = g(u_n)$ graphically:
> 1. Draw the graph of $y = g(x)$ (for (21), the parabola $y = \rho x(1 - x)$) and the line $y = x$. Their intersections are the equilibrium solutions.
> 2. Start at $u_0$ on the $x$-axis and draw a vertical segment up (or down) to the graph of $g$: its height is $g(u_0) = u_1$.
> 3. Draw a horizontal segment from there to the line $y = x$; this transfers the value $u_1$ from the $y$-axis to the $x$-axis.
> 4. Repeat: vertical to the graph, horizontal to the line. The resulting piecewise linear path, a **stairstep** or **cobweb diagram**, represents the solution sequence.
>
> A path that closes in on an intersection point shows convergence to that equilibrium: a staircase if $0 < g'(u^*) < 1$, a spiral if $-1 < g'(u^*) < 0$.

^rem-12-2

> [!example] Example §12.2: Three Regimes of the Logistic Difference Equation
> Compute solutions of (21) for $\rho = 0.8$, $1.5$ and $2.8$.
>
> **$\rho = 0.8$, $u_0 = 0.3$.** The iterates are $0.3,\ 0.168,\ 0.1118,\ 0.0795,\ 0.0585,\ 0.0441,\ \ldots$, decreasing to $0$: here $0$ is the asymptotically stable equilibrium, and $g'(0) = 0.8$, so the convergence is monotone, roughly by a factor $0.8$ per step.
>
> **$\rho = 1.5$, $u_0 = 0.85$.** The iterates are $0.85,\ 0.1913,\ 0.2320,\ 0.2673,\ 0.2938,\ 0.3112,\ 0.3215,\ \ldots \to \frac{0.5}{1.5} = \frac13$. After the first step the convergence is monotone, because $g'(\frac13) = 2 - 1.5 = 0.5 > 0$: the cobweb is a staircase.
>
> **$\rho = 2.8$, $u_0 = 0.3$.** The iterates are $0.3,\ 0.5880,\ 0.6783,\ 0.6110,\ 0.6655,\ 0.6233,\ 0.6574,\ \ldots \to \frac{1.8}{2.8} \cong 0.6429$, alternately above and below the limit, because $g'(0.6429) = 2 - 2.8 = -0.8 < 0$: the cobweb is a spiral (figure below), and the convergence is slow since $|g'| = 0.8$ is close to $1$.
>
> The graphs are similar for other initial conditions.
>
> *BDP: 2.9 (text), Figures 2.9.1 and 2.9.2*

^ex-12-2

![[m331-12-1.svg]]
*Cobweb diagrams for $u_{n+1} = \rho u_n(1 - u_n)$, starting at $u_0 = 0.3$. (a) $\rho = 2.8$: the path spirals into the equilibrium $(\rho - 1)/\rho \approx 0.643$, where the slope of the parabola is $2 - \rho = -0.8$. (b) $\rho = 3.2$: the slope at the equilibrium is $-1.2$, the equilibrium repels, and the path settles onto the rectangle (green) of the period-2 solution alternating between $0.513$ and $0.800$.*

In summary, (21) has two equilibrium solutions, $u_n = 0$, asymptotically stable for $0 \le \rho < 1$, and $u_n = (\rho - 1)/\rho$, asymptotically stable for $1 < \rho < 3$. Plotted against $\rho$, the stable branch passes from one curve to the other at $\rho = 1$.

## Bifurcations and Chaos

For $\rho > 3$ neither equilibrium is stable, and the solutions of (21) show increasing complexity as $\rho$ increases.

> [!definition] Definition §12.4: Exchange of Stability
> At $\rho = 1$ the equilibrium solutions $u = 0$ and $u = (\rho - 1)/\rho$ of the logistic difference equation (21) cross, and stability passes from one to the other: an **exchange of stability**.
>
> *BDP: 2.9 (text)*

^def-12-4

> [!definition] Definition §12.4: Bifurcation
> The transition from solutions of one period to solutions of a new period (for (21): from the stable equilibrium to a stable oscillation of period 2 at $\rho = 3$, from period 2 to period 4 at $\rho \cong 3.449$, then periods $8, 16, \ldots$) is called a **bifurcation**, and the value of the parameter at which it occurs is a **bifurcation value**.
>
> *BDP: 2.9 (text)*

^def-12-new4

> [!definition] Definition §12.4: Chaos
> Solutions that possess some regularity but no discernible detailed pattern, with an unpredictable fine structure and extreme sensitivity to the initial conditions, are called **chaotic**.
>
> *BDP: 2.9 (text)*

^def-12-new5

> [!example] Example §12.3: Period Doubling and Chaos
> **Period 2.** A solution of period 2 alternates between two values $u_1 \ne u_2$ with $g(u_1) = u_2$ and $g(u_2) = u_1$; these are fixed points of $g \circ g$ that are not fixed points of $g$. For $g(u) = \rho u(1 - u)$,
>
> $$
> g(g(u)) - u = -u\,(\rho u - \rho + 1)\,\big(\rho^2u^2 - \rho(\rho + 1)u + \rho + 1\big) .
> $$
>
> The first two factors give the equilibria $0$ and $(\rho - 1)/\rho$; the quadratic gives
>
> $$
> u_{1,2} = \frac{(\rho + 1) \pm \sqrt{(\rho + 1)(\rho - 3)}}{2\rho} ,
> $$
>
> real and distinct exactly when $\rho > 3$. For $\rho = 3.2$: $u_{1,2} = \dfrac{4.2 \pm \sqrt{0.84}}{6.4} \cong 0.7995$ and $0.5130$. Starting from $u_0 = 0.3$, the iterates $0.3,\ 0.672,\ 0.705,\ 0.665,\ 0.713,\ \ldots$ settle down, for $n$ greater than about 20, to the oscillation between $0.5130$ and $0.7995$, and the same happens for every initial value between $0$ and $1$. In the cobweb diagram the oscillation is a rectangle traversed repeatedly in the clockwise direction (figure above).
>
> **Why period 2 becomes unstable.** By the chain rule the slope of $g \circ g$ at $u_1$ is $g'(u_1)g'(u_2) = \rho^2(1 - 2u_1)(1 - 2u_2)$. With $u_1 + u_2 = (\rho + 1)/\rho$ and $u_1u_2 = (\rho + 1)/\rho^2$ (from the quadratic), this is $\rho^2 - 2\rho(\rho + 1) + 4(\rho + 1) = -\rho^2 + 2\rho + 4$. By [[§12★ First-Order Difference Equations#^lem-12-5|Lemma §12.5]] applied to $g \circ g$, the period-2 solution is stable when $|-\rho^2 + 2\rho + 4| < 1$, that is, when $\rho^2 - 2\rho - 3 > 0$ and $\rho^2 - 2\rho - 5 < 0$: for
>
> $$
> 3 < \rho < 1 + \sqrt6 \cong 3.449 .
> $$
>
> This is BDP's bifurcation value $\rho \cong 3.449$, at which each state of the period-2 oscillation separates into two and the solution becomes periodic with period 4. For $\rho = 3.5$ the solution from $u_0 = 0.3$ settles onto the four values $0.3828,\ 0.8269,\ 0.5009,\ 0.8750$.
>
> **Chaos.** As $\rho$ increases further, periodic solutions of period $8, 16, \ldots$ appear (period 8 at about $\rho_3 \cong 3.544$), and the period-doubling values approach a limit of approximately $3.57$. (The ratios $(\rho_n - \rho_{n-1})/(\rho_{n+1} - \rho_n)$ approach the Feigenbaum number $\delta \cong 4.6692$, BDP Problem 2.9.15.) For $\rho > 3.57$ the solutions show no discernible pattern for most values of $\rho$. For $\rho = 3.65$ the solution from $u_0 = 0.3$ wanders between about $0.3$ and $0.9$; the solution from $u_0 = 0.305$ stays close to it for about 15 iterations, after which the difference between them becomes as large as the values themselves (by $n = 18$ it is about $0.32$), although both keep wandering in about the same set of values. One solution cannot be used to estimate the other for $n$ larger than about 15.
>
> *BDP: 2.9 (text), Figures 2.9.4–2.9.7; the formulas for the period-2 solution and its stability are added*

^ex-12-3

![[m331-12-2.svg]]
*Equilibria and the period-2 solution of $u_{n+1} = \rho u_n(1 - u_n)$ against $\rho$ (solid: asymptotically stable; dashed: unstable). The equilibria $u = 0$ (blue) and $u = (\rho - 1)/\rho$ (red) exchange stability at $\rho = 1$. At $\rho = 3$ the red equilibrium loses stability and the period-2 solution (green) branches off; it is stable until $\rho = 1 + \sqrt6 \cong 3.449$, where the next period doubling occurs.*

The logistic difference equation was one of the first instances of mathematical chaos to be found and studied in detail, by Robert May in 1974. On the basis of his analysis of it as a model for certain insect populations, May suggested that if the growth rate $\rho$ is too large, effective long-range predictions of these populations are impossible. It is increasingly clear that chaotic solutions are much more common than was suspected at first, also for differential equations, and they may be part of the investigation of a wide range of phenomena. Note the contrast with the logistic *differential* equation (20), whose solutions with $y_0 > 0$ all approach $K$ monotonically ([[§8 Autonomous Differential Equations and Population Dynamics#^prop-8-3|Proposition §8.3]]): by [[§12★ First-Order Difference Equations#^prop-12-3|Proposition §12.3]], Euler's method with a step $h$ so large that $\rho = 1 + hr > 3$ does not reproduce this behaviour at all.
