---
type: section
subject: "[[Calculus]]"
chapter: 5
section: 37
stewart: "5.4"
aliases: ["Stewart 5.4"]
tags: [calculus]
---
← [[§36 The Fundamental Theorem of Calculus]] · ↑ [[· 5 Integrals]] · [[§38 The Substitution Rule]] →

*Stewart, Section 5.4.*

FTC2 ([[§36 The Fundamental Theorem of Calculus#^thm-36-2|Theorem §36.2]]) evaluates a definite integral as soon as an antiderivative is known, so antiderivatives get a notation of their own, the indefinite integral $\int f(x)\,dx$, and a table. This section restates the antidifferentiation formulas of [[§33 Antiderivatives#^thm-33-2|Theorem §33.2]] in that notation and uses them to evaluate definite integrals. It then reads FTC2 as the **Net Change Theorem**: the integral of a rate of change is the net change. In particular the integral of velocity is displacement, and the integral of speed is distance traveled, which confirms the guess made in [[§34 The Area and Distance Problems#^ex-34-4|Example §34.4]].

## Indefinite Integrals

> [!definition] Definition §37.1: Indefinite Integral
> The notation $\int f(x)\,dx$ is used for an antiderivative of $f$ and is called an **indefinite integral**:
>
> $$
> \int f(x)\,dx = F(x) \qquad\text{means}\qquad F'(x) = f(x) .
> $$
>
> For example, $\displaystyle\int x^2\,dx = \frac{x^3}{3} + C$ because $\displaystyle\frac{d}{dx}\Big(\frac{x^3}{3} + C\Big) = x^2$. So an indefinite integral stands for a whole *family* of functions, one antiderivative for each value of the constant $C$.
>
> *Stewart: 5.4 (text)*

^def-37-1

> [!remark] Remark: Definite Versus Indefinite Integrals
> A definite integral $\int_a^b f(x)\,dx$ is a **number**; an indefinite integral $\int f(x)\,dx$ is a **function** (or a family of functions). They are connected by FTC2: if $f$ is continuous on $[a, b]$, then
>
> $$
> \int_a^b f(x)\,dx = \int f(x)\,dx \,\Big]_a^b .
> $$

^rem-37-1

> [!theorem] Theorem §37.1: Table of Indefinite Integrals
> $$
> \begin{aligned}
> &\int c f(x)\,dx = c \int f(x)\,dx && \int [f(x) + g(x)]\,dx = \int f(x)\,dx + \int g(x)\,dx \\
> &\int k\,dx = kx + C \\
> &\int x^n\,dx = \frac{x^{n+1}}{n + 1} + C \quad (n \ne -1) && \int \frac1x\,dx = \ln|x| + C \\
> &\int e^x\,dx = e^x + C && \int b^x\,dx = \frac{b^x}{\ln b} + C \\
> &\int \sin x\,dx = -\cos x + C && \int \cos x\,dx = \sin x + C \\
> &\int \sec^2 x\,dx = \tan x + C && \int \csc^2 x\,dx = -\cot x + C \\
> &\int \sec x \tan x\,dx = \sec x + C && \int \csc x \cot x\,dx = -\csc x + C \\
> &\int \frac{1}{x^2 + 1}\,dx = \tan^{-1} x + C && \int \frac{1}{\sqrt{1 - x^2}}\,dx = \sin^{-1} x + C \\
> &\int \sinh x\,dx = \cosh x + C && \int \cosh x\,dx = \sinh x + C
> \end{aligned}
> $$
>
> *Stewart: 5.4, Table 1*

^thm-37-1

> [!proof]+ Proof
> Every formula is checked by differentiating the right side and obtaining the integrand ([[§37 Indefinite Integrals and the Net Change Theorem#^def-37-1|Definition §37.1]]).
> - **The two rules.** If $F' = f$ and $G' = g$, then $(cF)' = cf$ and $(F + G)' = f + g$ (Constant Multiple and Sum Rules, [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-3|Theorems §14.3]] and [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-4|§14.4]]).
> - **Powers and exponentials.** $\frac{d}{dx}(kx) = k$; $\frac{d}{dx} \frac{x^{n+1}}{n + 1} = \frac{(n + 1)x^n}{n + 1} = x^n$ for $n \ne -1$ (Power Rule, [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-2|Theorem §14.2]], and its general version [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-6|Theorem §19.6]]); $\frac{d}{dx} e^x = e^x$ ([[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-6|Theorem §14.6]]); $\frac{d}{dx} \frac{b^x}{\ln b} = \frac{b^x \ln b}{\ln b} = b^x$ ([[§17 The Chain Rule#^thm-17-5|Theorem §17.5]]).
> - **The logarithm.** $\frac{d}{dx} \ln|x| = \frac1x$ for $x \ne 0$ ([[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-5|Theorem §19.5]]): for $x > 0$ it is $\frac{d}{dx}\ln x = \frac1x$, and for $x < 0$, $\frac{d}{dx}\ln(-x) = \frac{-1}{-x} = \frac1x$ by the Chain Rule.
> - **Trigonometric functions** ([[§16 Derivatives of Trigonometric Functions#^thm-16-4|Theorem §16.4]]): $(-\cos x)' = \sin x$, $(\sin x)' = \cos x$, $(\tan x)' = \sec^2 x$, $(-\cot x)' = \csc^2 x$, $(\sec x)' = \sec x \tan x$, $(-\csc x)' = \csc x \cot x$.
> - **Inverse trigonometric functions** ([[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-8|Theorem §19.8]]): $(\tan^{-1} x)' = \frac{1}{1 + x^2}$ and $(\sin^{-1} x)' = \frac{1}{\sqrt{1 - x^2}}$.
> - **Hyperbolic functions** ([[§24 Hyperbolic Functions#^thm-24-2|Theorem §24.2]]): $(\cosh x)' = \sinh x$ and $(\sinh x)' = \cosh x$.
>
> Adding the constant $C$ does not change the derivative. That $F(x) + C$ is the *most general* antiderivative on an interval is Theorem 4.9.1 ([[§33 Antiderivatives#^thm-33-1|Theorem §33.1]]).

^pf-37-1

*Uses:* [[§37 Indefinite Integrals and the Net Change Theorem#^def-37-1|Def. §37.1]], [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-2|§14.2]], [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-3|§14.3]], [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-4|§14.4]], [[§14 Derivatives of Polynomials and Exponential Functions#^thm-14-6|§14.6]], [[§16 Derivatives of Trigonometric Functions#^thm-16-4|§16.4]], [[§17 The Chain Rule#^thm-17-5|§17.5]], [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-5|§19.5]], [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-6|§19.6]], [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-8|§19.8]], [[§24 Hyperbolic Functions#^thm-24-2|§24.2]], [[§33 Antiderivatives#^thm-33-1|§33.1]]

> [!remark] Remark: Convention — Formulas Hold on an Interval
> The most general antiderivative *on a given interval* is a particular antiderivative plus a constant (Theorem 4.9.1). **A formula for a general indefinite integral is understood to be valid only on an interval.** Thus
>
> $$
> \int \frac{1}{x^2}\,dx = -\frac1x + C
> $$
>
> is meant on $(0, \infty)$ or on $(-\infty, 0)$. On the whole domain $x \ne 0$ the general antiderivative of $1/x^2$ is
>
> $$
> F(x) = \begin{cases} -\dfrac1x + C_1 & \text{if } x < 0 \\[6pt] -\dfrac1x + C_2 & \text{if } x > 0 \end{cases}
> $$
>
> with two independent constants, since the domain consists of two intervals.

^rem-37-2

> [!example] Example §37.1: General Indefinite Integrals
> **(a)** Find $\displaystyle\int (10x^4 - 2\sec^2 x)\,dx$.
>
> By the convention and Table 1,
>
> $$
> \int (10x^4 - 2\sec^2 x)\,dx = 10 \int x^4\,dx - 2 \int \sec^2 x\,dx = 10\,\frac{x^5}{5} - 2\tan x + C = 2x^5 - 2\tan x + C .
> $$
>
> Check: $\frac{d}{dx}(2x^5 - 2\tan x + C) = 10x^4 - 2\sec^2 x$. (Different values of $C$ shift the graph vertically; $C$ is its $y$-intercept.)
>
> **(b)** Evaluate $\displaystyle\int \frac{\cos\theta}{\sin^2\theta}\,d\theta$.
>
> This is not in Table 1 as written, so first rewrite it with trigonometric identities:
>
> $$
> \int \frac{\cos\theta}{\sin^2\theta}\,d\theta = \int \Big(\frac{1}{\sin\theta}\Big)\Big(\frac{\cos\theta}{\sin\theta}\Big)\,d\theta = \int \csc\theta \cot\theta\,d\theta = -\csc\theta + C .
> $$
>
> *Stewart: Examples 5.4.1 and 5.4.2*

^ex-37-1

> [!example] Example §37.2: Definite Integrals from the Table
> **(a)** Find $\displaystyle\int_0^2 \Big(2x^3 - 6x + \frac{3}{x^2 + 1}\Big)\,dx$ and interpret the result in terms of areas.
>
> By FTC2 and Table 1,
>
> $$
> \begin{aligned}
> \int_0^2 \Big(2x^3 - 6x + \frac{3}{x^2 + 1}\Big)\,dx
> &= 2\,\frac{x^4}{4} - 6\,\frac{x^2}{2} + 3\tan^{-1} x \,\Big]_0^2
> = \tfrac12 x^4 - 3x^2 + 3\tan^{-1} x \,\Big]_0^2 \\
> &= \tfrac12 (2^4) - 3(2^2) + 3\tan^{-1} 2 - 0 = -4 + 3\tan^{-1} 2 .
> \end{aligned}
> $$
>
> This is the exact value; numerically, $\tan^{-1} 2 \approx 1.107149$ gives $\approx -0.67855$. The integrand is positive near $x = 0$ and near $x = 2$ and negative in between, so the value is a net area ([[§35 The Definite Integral#^rem-35-1|Remark: The Integral as a Net Area]]): the two areas above the axis minus the one below.
>
> **(b)** Evaluate $\displaystyle\int_1^9 \frac{2t^2 + t^2\sqrt t - 1}{t^2}\,dt$.
>
> First simplify the integrand by carrying out the division:
>
> $$
> \begin{aligned}
> \int_1^9 \frac{2t^2 + t^2\sqrt t - 1}{t^2}\,dt &= \int_1^9 \big(2 + t^{1/2} - t^{-2}\big)\,dt
> = 2t + \frac{t^{3/2}}{\frac32} - \frac{t^{-1}}{-1} \,\Big]_1^9 = 2t + \tfrac23 t^{3/2} + \frac1t \,\Big]_1^9 \\
> &= \big(2 \cdot 9 + \tfrac23 \cdot 9^{3/2} + \tfrac19\big) - \big(2 \cdot 1 + \tfrac23 \cdot 1^{3/2} + \tfrac11\big)
> = 18 + 18 + \tfrac19 - 2 - \tfrac23 - 1 = 32\tfrac49 .
> \end{aligned}
> $$
>
> *Stewart: Examples 5.4.4 and 5.4.5*

^ex-37-2

## The Net Change Theorem

In FTC2, $F$ is an antiderivative of $f$, that is $F' = f$, so the theorem can be written $\int_a^b F'(x)\,dx = F(b) - F(a)$. Here $F'(x)$ is the rate of change of $y = F(x)$ with respect to $x$, and $F(b) - F(a)$ is the change in $y$ when $x$ changes from $a$ to $b$. Since $y$ may increase, then decrease, then increase again, $F(b) - F(a)$ is the *net* change in $y$.

> [!theorem] Theorem §37.2: The Net Change Theorem
> The integral of a rate of change is the net change:
>
> $$
> \int_a^b F'(x)\,dx = F(b) - F(a) .
> $$
>
> (Here $F'$ is continuous on $[a, b]$.)
>
> *Stewart: 5.4, Net Change Theorem*

^thm-37-2

> [!proof]+ Proof
> Apply FTC2 ([[§36 The Fundamental Theorem of Calculus#^thm-36-2|Theorem §36.2]]) to the continuous function $f = F'$, of which $F$ is an antiderivative.

^pf-37-2

*Uses:* [[§36 The Fundamental Theorem of Calculus#^thm-36-2|§36.2]]

> [!remark]- Connections
> - Rigorous treatment: [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]] proves exactly this form, assuming only that $F'$ exists and is integrable (not necessarily continuous).

> [!remark] Remark: Net Change in the Sciences
> The theorem applies to every rate of change of [[§20 Rates of Change in the Natural and Social Sciences|§20]]. A single abstract idea, the integral, has many interpretations:
> - **Water in a reservoir.** If $V(t)$ is the volume of water at time $t$, then $V'(t)$ is the rate of flow into the reservoir, and $\int_{t_1}^{t_2} V'(t)\,dt = V(t_2) - V(t_1)$ is the change in the amount of water between $t_1$ and $t_2$.
> - **Chemistry.** If $[\mathrm{C}](t)$ is the concentration of the product of a reaction, the rate of reaction is $d[\mathrm{C}]/dt$, and $\int_{t_1}^{t_2} \frac{d[\mathrm{C}]}{dt}\,dt = [\mathrm{C}](t_2) - [\mathrm{C}](t_1)$ is the change in concentration.
> - **Mass of a rod.** If $m(x)$ is the mass of a rod from its left end to the point $x$, the linear density is $\rho(x) = m'(x)$, and $\int_a^b \rho(x)\,dx = m(b) - m(a)$ is the mass of the segment $a \le x \le b$.
> - **Population.** $\int_{t_1}^{t_2} \frac{dn}{dt}\,dt = n(t_2) - n(t_1)$ is the net change in population, births minus deaths.
> - **Economics.** If $C(x)$ is the cost of producing $x$ units, then $\int_{x_1}^{x_2} C'(x)\,dx = C(x_2) - C(x_1)$ is the increase in cost when production rises from $x_1$ to $x_2$ units (marginal cost integrates to total cost).
> - **Acceleration.** If $a(t) = v'(t)$, then $\int_{t_1}^{t_2} a(t)\,dt = v(t_2) - v(t_1)$ is the change in velocity.

^rem-37-3

The most important instance concerns motion along a line, and it settles the guess made in [[§34 The Area and Distance Problems#^ex-34-4|Example §34.4]] (Equation 5 after it), now for objects that may also move backward.

> [!theorem] Corollary §37.3: Displacement and Distance Traveled
> Let an object move along a straight line with position function $s(t)$ and continuous velocity $v(t) = s'(t)$. Then:
> 1. its **displacement** (net change of position) from time $t_1$ to $t_2$ is
>
> $$
> \int_{t_1}^{t_2} v(t)\,dt = s(t_2) - s(t_1) ; \qquad (2)
> $$
>
> 2. the **total distance traveled** is the integral of the speed $|v(t)|$:
>
> $$
> \int_{t_1}^{t_2} |v(t)|\,dt = \text{total distance traveled} . \qquad (3)
> $$
>
> In terms of areas under the velocity curve: if $v \ge 0$ with area $A_1$, then $v \le 0$ with area $A_2$, then $v \ge 0$ with area $A_3$, the displacement is $A_1 - A_2 + A_3$ and the distance is $A_1 + A_2 + A_3$.
>
> *Stewart: 5.4, Equations 2 and 3*

^cor-37-3

> [!proof]+ Proof
> **(2)** is the Net Change Theorem with $F = s$.
>
> **(3)** Split $[t_1, t_2]$ by Property 5 of integrals ([[§35 The Definite Integral#^thm-35-5|Theorem §35.5]]) into intervals on each of which $v \ge 0$ or $v \le 0$. (Stewart takes this splitting for granted; it is possible whenever $v$ changes sign finitely often, as in all the examples.) On an interval $[c, d]$ where $v \ge 0$, the object moves only forward, so the distance it travels is $s(d) - s(c) = \int_c^d v(t)\,dt = \int_c^d |v(t)|\,dt$ by (2). On an interval where $v \le 0$, it moves only backward, so the distance is $s(c) - s(d) = \int_c^d [-v(t)]\,dt = \int_c^d |v(t)|\,dt$. Adding over the intervals gives the total distance $\int_{t_1}^{t_2} |v(t)|\,dt$.

^pf-37-3

*Uses:* [[§37 Indefinite Integrals and the Net Change Theorem#^thm-37-2|§37.2]], [[§35 The Definite Integral#^thm-35-5|§35.5]]

> [!example] Example §37.3: Displacement Versus Distance
> A particle moves along a line with velocity $v(t) = t^2 - t - 6$ (in meters per second).
>
> **(a)** Find the displacement during $1 \le t \le 4$.
>
> **(b)** Find the distance traveled during this time period.
>
> **(a)** By Equation (2),
>
> $$
> s(4) - s(1) = \int_1^4 (t^2 - t - 6)\,dt = \Big[\frac{t^3}{3} - \frac{t^2}{2} - 6t\Big]_1^4
> = \Big(\frac{64}{3} - 8 - 24\Big) - \Big(\frac13 - \frac12 - 6\Big) = -\frac{32}{3} + \frac{37}{6} = -\frac92 .
> $$
>
> The particle ends up $4.5$ m to the left of where it started.
>
> **(b)** $v(t) = (t - 3)(t + 2)$, so $v(t) \le 0$ on $[1, 3]$ and $v(t) \ge 0$ on $[3, 4]$. By Equation (3) and Property 5,
>
> $$
> \begin{aligned}
> \int_1^4 |v(t)|\,dt &= \int_1^3 [-v(t)]\,dt + \int_3^4 v(t)\,dt
> = \int_1^3 (-t^2 + t + 6)\,dt + \int_3^4 (t^2 - t - 6)\,dt \\
> &= \Big[-\frac{t^3}{3} + \frac{t^2}{2} + 6t\Big]_1^3 + \Big[\frac{t^3}{3} - \frac{t^2}{2} - 6t\Big]_3^4
> = \Big(\frac{27}{2} - \frac{37}{6}\Big) + \Big(-\frac{32}{3} + \frac{27}{2}\Big) = \frac{22}{3} + \frac{17}{6} = \frac{61}{6} \approx 10.17 \text{ m} .
> \end{aligned}
> $$
>
> (Check: displacement $= \frac{17}{6} - \frac{22}{3} = -\frac{27}{6} = -\frac92$.)
>
> *Stewart: Example 5.4.6*

^ex-37-3

![[m233-37-1.svg]]
*Example §37.3. On $[1, 3]$ the velocity is negative and the particle moves left a distance $\frac{22}{3}$ (orange area); on $[3, 4]$ it moves right $\frac{17}{6}$ (blue area). Displacement counts the orange area negatively, $\frac{17}{6} - \frac{22}{3} = -\frac92$; distance counts both, $\frac{17}{6} + \frac{22}{3} = \frac{61}{6}$.*

> [!example] Example §37.4: Energy from a Power Curve
> A graph shows the power consumption $P$ (in megawatts) in San Francisco on a day in September, with $t$ in hours starting at midnight. Estimate the energy used that day.
>
> Power is the rate of change of energy, $P(t) = E'(t)$. By the Net Change Theorem,
>
> $$
> \int_0^{24} P(t)\,dt = \int_0^{24} E'(t)\,dt = E(24) - E(0)
> $$
>
> is the total energy used that day. Only a graph of $P$ is available, so approximate the integral by the Midpoint Rule ([[§35 The Definite Integral#^def-35-3|Definition §35.3]]) with $12$ subintervals, $\Delta t = 2$, reading $P$ off the graph at the midpoints $t = 1, 3, \ldots, 23$:
>
> $$
> \begin{aligned}
> \int_0^{24} P(t)\,dt &\approx [P(1) + P(3) + P(5) + \cdots + P(21) + P(23)]\,\Delta t \\
> &\approx (440 + 400 + 420 + 620 + 790 + 840 + 850 + 840 + 810 + 690 + 670 + 550)(2) = 7920 \cdot 2 = 15{,}840 .
> \end{aligned}
> $$
>
> The energy used was approximately $15{,}840$ megawatt-hours.
>
> **Units.** $\int_0^{24} P(t)\,dt$ is a limit of sums of terms $P(t_i^{\ast})\,\Delta t$, megawatts times hours, so it is measured in megawatt-hours. In general, the unit of $\int_a^b f(x)\,dx$ is the unit of $f(x)$ times the unit of $x$.
>
> *Stewart: Example 5.4.7*

^ex-37-4
