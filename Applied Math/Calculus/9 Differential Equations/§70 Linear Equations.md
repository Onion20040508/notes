---
type: section
subject: "[[Calculus]]"
chapter: 9
section: 70
stewart: "9.5"
aliases: ["Stewart 9.5"]
tags: [calculus]
---
← [[§69 Models for Population Growth]] · ↑ [[· 9 Differential Equations]] · [[§71 Predator-Prey Systems]] →

*Stewart, Section 9.5.*

A first-order linear equation $y' + P(x)y = Q(x)$ is usually not separable, but it can always be solved. Multiplying by the integrating factor $I(x) = e^{\int P(x)\,dx}$ turns the left side into the derivative of the single product $I(x)y$, and then both sides can be integrated. The method gives every solution in one formula, with one constant fixed by an initial condition. Even when $\int I(x)Q(x)\,dx$ is not elementary, the answer can still be written with a definite integral. The main application here is the current in an electric circuit with a resistor and an inductor, driven by a battery or by a generator.

## Linear Differential Equations

> [!definition] Definition §70.1: First-Order Linear Equation
> A first-order **linear** differential equation is one that can be put into the form
>
> $$
> \frac{dy}{dx} + P(x)\,y = Q(x) \qquad (1)
> $$
>
> where $P$ and $Q$ are continuous functions on a given interval. This is the **standard form**: the coefficient of $y'$ is $1$, and $y$ and $y'$ appear only to the first power, multiplied by functions of $x$ alone.
>
> *Stewart: 9.5, Equation 1*

^def-70-1

> [!remark] Remark: A Linear Equation That Is Not Separable
> The equation $xy' + y = 2x$ is linear, since for $x \ne 0$ it can be written as
>
> $$
> y' + \frac1x\,y = 2 . \qquad (2)
> $$
>
> It is not separable: $y' = 2 - y/x$ cannot be factored as a function of $x$ times a function of $y$, so the method of [[§68 Separable Equations#^thm-68-1|Theorem §68.1]] does not apply. But by the Product Rule the left side of $xy' + y = 2x$ is a derivative, $xy' + y = (xy)'$, so the equation says
>
> $$
> (xy)' = 2x .
> $$
>
> Integrating both sides gives $xy = x^2 + C$, or $y = x + \dfrac{C}{x}$. Had the equation been given in the form (2), the first step would have been to multiply both sides by $x$. The method below finds such a multiplier for every linear equation.

^rem-70-1

> [!definition] Definition §70.2: Integrating Factor
> An **integrating factor** for the linear equation (1) is a function $I(x)$ such that multiplying the left side of (1) by $I(x)$ turns it into the derivative of the product $I(x)y$:
>
> $$
> I(x)\big(y' + P(x)y\big) = \big(I(x)y\big)' . \qquad (3)
> $$
>
> For $xy' + y = 2x$ in the form (2), $I(x) = x$ is an integrating factor.
>
> *Stewart: 9.5, Equation 3*

^def-70-2

> [!theorem] Theorem §70.1: Solving a Linear Equation
> Let $P$ and $Q$ be continuous on an interval. Then
>
> $$
> I(x) = e^{\int P(x)\,dx} \qquad (5)
> $$
>
> (any one antiderivative of $P$ in the exponent) is an integrating factor for (1), and the solutions of (1) on the interval are exactly the functions
>
> $$
> y(x) = \frac{1}{I(x)} \left[ \int I(x)\,Q(x)\,dx + C \right], \qquad C \text{ a constant} . \qquad (4)
> $$
>
> In practice one does not memorize (4) but only the form of the integrating factor: **to solve $y' + P(x)y = Q(x)$, multiply both sides by the integrating factor $I(x) = e^{\int P(x)\,dx}$ and then integrate both sides.**
>
> *Stewart: 9.5, Equations 4 and 5 and the boxed rule*

^thm-70-1

> [!proof]+ Proof
> **Finding $I$.** Suppose $I$ satisfies (3). Expanding both sides of (3) with the Product Rule,
>
> $$
> I(x)y' + I(x)P(x)y = \big(I(x)y\big)' = I'(x)y + I(x)y' ,
> $$
>
> and cancelling $I(x)y'$ leaves $I(x)P(x)y = I'(x)y$. For this to hold for the solutions $y$, it is enough that
>
> $$
> I'(x) = I(x)P(x) .
> $$
>
> This is a separable differential equation for $I$. Separating variables,
>
> $$
> \int \frac{dI}{I} = \int P(x)\,dx, \qquad \ln|I| = \int P(x)\,dx, \qquad I = A e^{\int P(x)\,dx} ,
> $$
>
> where $A = \pm e^C$. We want a particular integrating factor, not the most general one, so we take $A = 1$, which is (5).
>
> **Checking (5).** The argument above shows where (5) comes from; here is why it works. Since $P$ is continuous, it has an antiderivative $p(x) = \int P(x)\,dx$ (for instance $\int_a^x P(t)\,dt$, by Part 1 of the Fundamental Theorem of Calculus). By the Chain Rule, $I = e^{p}$ satisfies $I' = e^{p}\,p' = I P$. Hence for every differentiable $y$,
>
> $$
> \big(I y\big)' = I' y + I y' = I\big(y' + P y\big) ,
> $$
>
> which is (3).
>
> **All solutions.** Since $I(x) = e^{p(x)} > 0$, multiplying by $I$ and dividing by $I$ are both allowed, so $y$ solves (1) if and only if
>
> $$
> \big(I(x)y\big)' = I(x)Q(x) .
> $$
>
> The function $IQ$ is continuous, so it has an antiderivative $G$. Then $(Iy)' = G'$, and two functions with the same derivative on an interval differ by a constant (Stewart asserts "integrating both sides"; this is the fact that makes it exact): $I(x)y = G(x) + C$. Dividing by $I(x)$ gives (4). Conversely, every function (4) satisfies $(Iy)' = G' = IQ$, so it is a solution.

^pf-70-1

*Uses:* [[§70 Linear Equations#^def-70-1|Def. §70.1]], [[§70 Linear Equations#^def-70-2|Def. §70.2]], [[§18 The Product and Quotient Rules#^thm-18-1|§18.1]] (Product Rule), [[§20 The Chain Rule#^thm-20-2|§20.2]] (Chain Rule), [[§68 Separable Equations#^thm-68-1|§68.1]] (separable equations), [[§41 The Fundamental Theorem of Calculus#^thm-41-1|§41.1]] (FTC Part 1: a continuous function has an antiderivative), [[§29 Rolle's Theorem and the Mean Value Theorem#^cor-29-4|§29.4]] (equal derivatives differ by a constant)

> [!remark]- Connections
> - The integrating factor appears in 451 in a Rolle's-theorem argument, where $(y e^{g})' = e^{g}(y' + y g')$ is used exactly as in (3): [[§29 The Mean Value Theorem#^ex-29-4|451 Ex. §29.4]] and [[§29 The Mean Value Theorem#^rem-29-2|451 Remark after Ex. §29.4]].
> - The step "all solutions differ by a constant" is [[§29 The Mean Value Theorem#^cor-29-5|451 Cor. §29.5]], and the existence of an antiderivative of a continuous function is [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 Thm. §34.4]] (FTC II).
> - ODE version: [[§5 Linear Differential Equations; Method of Integrating Factors#^thm-5-2|331 Thm. §5.2]] (the same integrating factor for $y' + p(t)y = g(t)$, [[§5 Linear Differential Equations; Method of Integrating Factors#^def-5-1|331 Def. §5.1]], [[§5 Linear Differential Equations; Method of Integrating Factors#^def-5-2|331 Def. §5.2]]), and [[§8 Differences Between Linear and Nonlinear Differential Equations#^thm-8-1|331 Thm. §8.1]] (an initial-value problem has exactly one solution on the whole interval where $p$ and $g$ are continuous).

> [!remark] Remark: Method — Solving a Linear Equation
> 1. **Standard form.** Divide by the coefficient of $y'$ to get $y' + P(x)y = Q(x)$. Note the interval on which that coefficient is not $0$; the solution lives there ([[§70 Linear Equations#^ex-70-2|Example §70.2]]).
> 2. **Integrating factor.** Compute $I(x) = e^{\int P(x)\,dx}$. No constant of integration is needed here, and $e^{\ln x} = x$ type simplifications usually apply.
> 3. **Multiply** both sides by $I(x)$. The left side is now $\big(I(x)y\big)'$. (Checking this is a good test of the arithmetic.)
> 4. **Integrate** both sides: $I(x)y = \int I(x)Q(x)\,dx + C$. Do not forget $C$. If $\int IQ\,dx$ is not elementary, write it as a definite integral $\int_a^x$ ([[§70 Linear Equations#^ex-70-3|Example §70.3]]).
> 5. **Divide** by $I(x)$ to get $y$.
> 6. **Initial condition.** If $y(x_0) = y_0$ is given, substitute to find $C$.

^rem-70-2

> [!example] Example §70.1: A First Linear Equation
> Solve the differential equation $\dfrac{dy}{dx} + 3x^2 y = 6x^2$.
>
> The equation has the form (1) with $P(x) = 3x^2$ and $Q(x) = 6x^2$. An integrating factor is
>
> $$
> I(x) = e^{\int 3x^2\,dx} = e^{x^3} .
> $$
>
> Multiplying both sides by $e^{x^3}$ gives
>
> $$
> e^{x^3}\frac{dy}{dx} + 3x^2 e^{x^3} y = 6x^2 e^{x^3}, \qquad\text{that is,}\qquad \frac{d}{dx}\big(e^{x^3} y\big) = 6x^2 e^{x^3}
> $$
>
> by the Product Rule. Integrating both sides (substitute $u = x^3$, $du = 3x^2\,dx$, [[§43 The Substitution Rule#^thm-43-1|Theorem §43.1]]),
>
> $$
> e^{x^3} y = \int 6x^2 e^{x^3}\,dx = 2e^{x^3} + C, \qquad y = 2 + Ce^{-x^3} .
> $$
>
> **Check.** $y' = -3x^2 C e^{-x^3}$, so $y' + 3x^2 y = -3x^2Ce^{-x^3} + 6x^2 + 3x^2Ce^{-x^3} = 6x^2$.
>
> Since $Ce^{-x^3} \to 0$ as $x \to \infty$, every solution approaches $2$. The solution with $C = 0$ is the constant $y = 2$.
>
> *Stewart: Example 9.5.1*

^ex-70-1

![[m233-61-1.svg]]
*Solutions $y = 2 + Ce^{-x^3}$ of [[§70 Linear Equations#^ex-70-1|Example §70.1]] for $C = \pm 2, \pm 1, \pm 0.4$ and $0$. Each is the constant solution $y = 2$ (blue) plus $C$ times the decaying factor $e^{-x^3}$. For $x > 0$ they all merge into $y = 2$; for $x < 0$, $e^{-x^3}$ blows up and the curves separate fast.*

> [!example] Example §70.2: An Initial-Value Problem
> Find the solution of the initial-value problem
>
> $$
> x^2 y' + xy = 1, \qquad x > 0, \qquad y(1) = 2 .
> $$
>
> **Standard form.** Divide by the coefficient $x^2$ of $y'$ (allowed, since $x > 0$):
>
> $$
> y' + \frac1x\,y = \frac{1}{x^2}, \qquad x > 0 . \qquad (6)
> $$
>
> **Integrating factor.** $I(x) = e^{\int (1/x)\,dx} = e^{\ln x} = x$. (In general $\int dx/x = \ln|x|$; here $x > 0$.)
>
> **Multiply and integrate.** Multiplying (6) by $x$,
>
> $$
> xy' + y = \frac1x, \qquad\text{or}\qquad (xy)' = \frac1x .
> $$
>
> Then $xy = \displaystyle\int \frac1x\,dx = \ln x + C$, and so
>
> $$
> y = \frac{\ln x + C}{x} .
> $$
>
> **Initial condition.** $2 = y(1) = \dfrac{\ln 1 + C}{1} = C$. Therefore the solution of the initial-value problem is
>
> $$
> y = \frac{\ln x + 2}{x} .
> $$
>
> It rises to a maximum and then decays to $0$ as $x \to \infty$, and $y \to -\infty$ as $x \to 0^+$.
>
> *Stewart: Example 9.5.2*

^ex-70-2

> [!example] Example §70.3: When the Integral Is Not Elementary
> Solve $y' + 2xy = 1$.
>
> The equation is in standard form with $P(x) = 2x$, $Q(x) = 1$. Multiplying by the integrating factor $e^{\int 2x\,dx} = e^{x^2}$ gives
>
> $$
> e^{x^2} y' + 2xe^{x^2} y = e^{x^2}, \qquad\text{or}\qquad \big(e^{x^2} y\big)' = e^{x^2} .
> $$
>
> Therefore
>
> $$
> e^{x^2} y = \int e^{x^2}\,dx + C, \qquad y = e^{-x^2} \int e^{x^2}\,dx + Ce^{-x^2} .
> $$
>
> The integral $\int e^{x^2}\,dx$ cannot be expressed in terms of elementary functions ([[§55 Strategy for Integration#^thm-55-2|Theorem §55.2]]). It is still a perfectly good function. To name one antiderivative explicitly, use Part 1 of the Fundamental Theorem of Calculus ([[§41 The Fundamental Theorem of Calculus#^thm-41-1|Theorem §41.1]]):
>
> $$
> y = e^{-x^2} \int_0^x e^{t^2}\,dt + Ce^{-x^2} .
> $$
>
> Any number can be chosen for the lower limit of integration; changing it changes $\int_a^x e^{t^2}\,dt$ by a constant, which is absorbed into $C$.
>
> **Check.** With $F(x) = \int_0^x e^{t^2}\,dt$ we have $F'(x) = e^{x^2}$, so $y' = -2xe^{-x^2}F(x) + e^{-x^2}e^{x^2} - 2xCe^{-x^2} = -2xy + 1$.
>
> Solutions written with an integral can still be graphed by computer, evaluating the integral numerically ([[§57 Approximate Integration|§57]]).
>
> *Stewart: Example 9.5.3*

^ex-70-3

> [!remark]- Connections
> - ODE version: [[§5 Linear Differential Equations; Method of Integrating Factors#^ex-5-4|331 Ex. §5.4]] ($2y' + ty = 2$, $y(0) = 1$, whose solution keeps the non-elementary integral of $e^{s^2/4}$ with lower limit at the initial point).

## Application to Electric Circuits

> [!definition] Definition §70.3: The RL Circuit Equation
> A simple circuit contains an electromotive force (a battery or generator) producing a voltage of $E(t)$ volts (V), a resistor with resistance $R$ ohms ($\Omega$), an inductor with inductance $L$ henries (H), and a switch. Let $I(t)$ be the current in amperes (A) at time $t$. By Ohm's Law the voltage drop across the resistor is $RI$, and the drop across the inductor is $L\,(dI/dt)$. One of Kirchhoff's laws says that the sum of the voltage drops equals the supplied voltage $E(t)$, so
>
> $$
> L\,\frac{dI}{dt} + RI = E(t) . \qquad (7)
> $$
>
> This is a first-order linear equation for $I$ ([[§70 Linear Equations#^def-70-1|Definition §70.1]], after dividing by $L$). The circuit was first met in [[§67 Direction Fields and Euler's Method#^def-67-2|Definition §67.2]].
>
> *Stewart: 9.5, Equation 7*

^def-70-3

> [!example] Example §70.4: A Circuit with a Battery
> In the circuit of [[§70 Linear Equations#^def-70-3|Definition §70.3]] the resistance is $12\ \Omega$ and the inductance is $4$ H. A battery gives a constant voltage of $60$ V, and the switch is closed at $t = 0$, so $I(0) = 0$. Find (a) $I(t)$, (b) the current after $1$ second, and (c) the limiting value of the current.
>
> **(a)** With $L = 4$, $R = 12$ and $E(t) = 60$, Equation (7) gives the initial-value problem
>
> $$
> 4\frac{dI}{dt} + 12I = 60, \quad I(0) = 0, \qquad\text{or}\qquad \frac{dI}{dt} + 3I = 15, \quad I(0) = 0 .
> $$
>
> Multiplying by the integrating factor $e^{\int 3\,dt} = e^{3t}$,
>
> $$
> e^{3t}\frac{dI}{dt} + 3e^{3t} I = 15e^{3t}, \qquad \frac{d}{dt}\big(e^{3t} I\big) = 15e^{3t}, \qquad e^{3t} I = \int 15e^{3t}\,dt = 5e^{3t} + C ,
> $$
>
> so $I(t) = 5 + Ce^{-3t}$. Since $I(0) = 0$, $5 + C = 0$, so $C = -5$ and
>
> $$
> I(t) = 5\big(1 - e^{-3t}\big) .
> $$
>
> **(b)** $I(1) = 5(1 - e^{-3}) \approx 5(1 - 0.0498) \approx 4.75$ A.
>
> **(c)**
>
> $$
> \lim_{t \to \infty} I(t) = \lim_{t \to \infty} 5\big(1 - e^{-3t}\big) = 5 - 5\lim_{t \to \infty} e^{-3t} = 5 - 0 = 5 .
> $$
>
> The limit is the current $E/R = 60/12$ that Ohm's Law gives when the inductor plays no role. This equation is also separable, $dI/dt = 15 - 3I$, so it can be solved as in [[§68 Separable Equations|§68]] (Stewart's Example 9.3.4). With a generator instead of a battery it is linear but no longer separable ([[§70 Linear Equations#^ex-70-5|Example §70.5]]).
>
> *Stewart: Example 9.5.4*

^ex-70-4

> [!example] Example §70.5: A Circuit with a Generator
> Keep the resistance and inductance of [[§70 Linear Equations#^ex-70-4|Example §70.4]], but replace the battery by a generator producing the variable voltage $E(t) = 60\sin 30t$ volts, with $I(0) = 0$. Find $I(t)$.
>
> Now (7) becomes
>
> $$
> 4\frac{dI}{dt} + 12I = 60\sin 30t \qquad\text{or}\qquad \frac{dI}{dt} + 3I = 15\sin 30t .
> $$
>
> The same integrating factor $e^{3t}$ gives
>
> $$
> \frac{d}{dt}\big(e^{3t} I\big) = e^{3t}\frac{dI}{dt} + 3e^{3t} I = 15e^{3t}\sin 30t .
> $$
>
> **The integral.** By Formula 98 of the Table of Integrals, $\displaystyle\int e^{au}\sin bu\,du = \frac{e^{au}}{a^2 + b^2}(a\sin bu - b\cos bu) + C$ ([[§56 Integration Using Tables and Technology|§56]]; it also follows by integrating by parts twice, [[§51 Integration by Parts#^thm-51-1|Theorem §51.1]]). With $a = 3$, $b = 30$, $a^2 + b^2 = 909$:
>
> $$
> e^{3t} I = \int 15e^{3t}\sin 30t\,dt = 15\,\frac{e^{3t}}{909}\,(3\sin 30t - 30\cos 30t) + C .
> $$
>
> (Check: $\frac{d}{dt}\big[e^{3t}(3\sin 30t - 30\cos 30t)\big] = e^{3t}(9\sin 30t - 90\cos 30t + 90\cos 30t + 900\sin 30t) = 909\,e^{3t}\sin 30t$.) Since $\frac{15 \cdot 3}{909} = \frac{45}{909} = \frac{5}{101}$, dividing by $e^{3t}$ gives
>
> $$
> I = \frac{5}{101}(\sin 30t - 10\cos 30t) + Ce^{-3t} .
> $$
>
> **Initial condition.** $I(0) = \frac{5}{101}(0 - 10) + C = -\frac{50}{101} + C = 0$, so $C = \frac{50}{101}$ and
>
> $$
> I(t) = \frac{5}{101}(\sin 30t - 10\cos 30t) + \frac{50}{101}e^{-3t} .
> $$
>
> The term $\frac{50}{101}e^{-3t}$ dies out (the transient). What remains is an oscillation with the generator's frequency and amplitude $\frac{5}{101}\sqrt{1^2 + 10^2} = \frac{5}{\sqrt{101}} \approx 0.50$ A.
>
> *Stewart: Example 9.5.5*

^ex-70-5

![[m233-61-2.svg]]
*The current in the circuit of [[§70 Linear Equations#^ex-70-4|Examples §70.4]] and [[§70 Linear Equations#^ex-70-5|§70.5]]. (a) With a battery, $I(t) = 5(1 - e^{-3t})$ rises to its limiting value $5$ A and is already within $5\%$ of it at $t = 1$. (b) With a generator, the same decaying term $\frac{50}{101}e^{-3t}$ (orange) pushes the first oscillations upward; after about one second only the steady oscillation of amplitude $5/\sqrt{101} \approx 0.50$ A (between the blue lines) is left.*
