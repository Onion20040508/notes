---
type: section
subject: "[[Calculus]]"
chapter: 3
section: 21
stewart: "3.8"
aliases: ["Stewart 3.8"]
tags: [calculus]
---
← [[§20 Rates of Change in the Natural and Social Sciences]] · ↑ [[· 3 Differentiation Rules]] · [[§22 Related Rates]] →

*Stewart, Section 3.8.*

Many quantities change at a rate proportional to their size: a population under ideal conditions (unlimited environment, adequate nutrition, immunity to disease), the mass of a radioactive substance, the concentration in a unimolecular first-order reaction, a savings account with continuously compounded interest. All are modeled by the differential equation $dy/dt = ky$, and its only solutions are the exponential functions $y(0)e^{kt}$. This section solves the standard problems: fitting $k$ to data, half-life, Newton's Law of Cooling (after a shift of variable), and continuous compounding, where the limit $e = \lim (1 + 1/n)^n$ of [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions|§19]] appears.

## The Law of Natural Growth

> [!definition] Definition §21.1: Law of Natural Growth and Decay
> If $y(t)$ is the value of a quantity at time $t$ and its rate of change with respect to $t$ is proportional to its size at every time, then
>
> $$
> \frac{dy}{dt} = ky \qquad (1)
> $$
>
> for a constant $k$. Equation 1 is the **law of natural growth** if $k > 0$ and the **law of natural decay** if $k < 0$. It is a *differential equation*: it involves an unknown function $y$ and its derivative $dy/dt$. The value $y(0)$ is the **initial value**.
>
> *Stewart: 3.8, Equation 1*

^def-21-1

> [!theorem] Theorem §21.1: Solutions of dy/dt = ky
> The only solutions of the differential equation $dy/dt = ky$ are the exponential functions
>
> $$
> y(t) = y(0)\,e^{kt} .
> $$
>
> *Stewart: 3.8, Theorem 2*

^thm-21-1

> [!proof]+ Proof
> **These are solutions.** For any constant $C$, the function $y(t) = Ce^{kt}$ satisfies, by the Chain Rule ([[§17 The Chain Rule#^cor-17-4|Corollary §17.4]]),
>
> $$
> \frac{dy}{dt} = C(ke^{kt}) = k(Ce^{kt}) = ky ,
> $$
>
> and $y(0) = Ce^{k \cdot 0} = C$. So the constant $C$ is the initial value, and $y(t) = y(0)e^{kt}$.
>
> **There are no others.** Stewart defers this half to Section 9.4 ([[§60 Models for Population Growth#^thm-60-1|Theorem §60.1]]), where the equation is solved by separation of variables. That computation divides by $y$, so it finds only the zero solution and the solutions that never vanish. A direct argument that covers every solution, using a consequence of the Mean Value Theorem from Chapter 4: let $y$ be any solution on an interval containing $0$ and put $g(t) = y(t)e^{-kt}$. By the Product Rule,
>
> $$
> g'(t) = y'(t)e^{-kt} - k\,y(t)e^{-kt} = \big(ky(t) - ky(t)\big)e^{-kt} = 0 .
> $$
>
> A function with derivative $0$ on an interval is constant ([[§26 The Mean Value Theorem|§26]], Stewart 4.2 Theorem 5), so $g(t) = g(0) = y(0)$ for all $t$, that is, $y(t) = y(0)e^{kt}$.

^pf-21-1

*Uses:* [[§17 The Chain Rule#^cor-17-4|§17.4]], [[§15 The Product and Quotient Rules#^thm-15-1|§15.1]], [[§26 The Mean Value Theorem|§26]] (a function with zero derivative is constant)

> [!remark]- Connections
> - The step "zero derivative implies constant" is [[§29 The Mean Value Theorem#^cor-29-4|451 Cor. §29.4]].
> - In Chapter 9 the same equation is the first example of a separable equation and of a population model: [[§59 Separable Equations|§59]], [[§60 Models for Population Growth|§60]].

## Population Growth

> [!definition] Definition §21.2: Relative Growth Rate
> If $P(t)$ is the size of a population at time $t$, the **relative growth rate** is the growth rate divided by the population size:
>
> $$
> \frac{dP/dt}{P} .
> $$
>
> So the law of natural growth $\dfrac{dP}{dt} = kP$ can also be written $\dfrac{dP/dt}{P} = k$ (Equation 3): instead of "the growth rate is proportional to population size" one can say "the relative growth rate is constant".
>
> *Stewart: 3.8, Equation 3 (text)*

^def-21-2

By Theorem §21.1, a population with constant relative growth rate $k$ grows exponentially, $P(t) = P_0 e^{kt}$, and $k$ is the coefficient of $t$ in the exponent. For instance, $dP/dt = 0.02P$ ($t$ in years) means a relative growth rate of $2\%$ per year, and $P(t) = P_0 e^{0.02t}$.

> [!remark] Remark: Method — Exponential Models
> 1. Recognize the model: the rate of change of $y$ is proportional to $y$ (or, after a shift $y = T - T_s$, to the difference from a constant).
> 2. Write $y(t) = y(0)e^{kt}$ by Theorem §21.1, with the initial value from the data.
> 3. Determine $k$ from one more data point $y(t_1) = y_1$: $e^{kt_1} = y_1/y(0)$, so $k = \dfrac{1}{t_1}\ln\dfrac{y_1}{y(0)}$. For a half-life $h$: $e^{kh} = \frac12$, so $k = -\dfrac{\ln 2}{h}$.
> 4. To evaluate, substitute $t$. To find *when* $y$ reaches a value $Y$, solve $e^{kt} = Y/y(0)$ by taking natural logarithms: $t = \dfrac1k \ln\dfrac{Y}{y(0)}$.

^rem-21-1

> [!example] Example §21.1: World Population
> The world population was $2560$ million in 1950 and $3040$ million in 1960. Model the population in the second half of the 20th century, assuming that the growth rate is proportional to the population size. What is the relative growth rate? Estimate the population in 1993 and predict it for 2025.
>
> Let $t$ be the time in years with $t = 0$ in 1950, and $P(t)$ the population in millions. Then $P(0) = 2560$ and $P(10) = 3040$. Since $dP/dt = kP$, Theorem §21.1 gives
>
> $$
> P(t) = P(0)e^{kt} = 2560e^{kt}, \qquad P(10) = 2560e^{10k} = 3040, \qquad k = \frac{1}{10}\ln\frac{3040}{2560} \approx 0.017185 .
> $$
>
> The relative growth rate is about $1.7\%$ per year, and the model is $P(t) = 2560e^{0.017185t}$. It estimates the 1993 population as
>
> $$
> P(43) = 2560e^{0.017185(43)} \approx 5360 \text{ million}
> $$
>
> and predicts for 2025
>
> $$
> P(75) = 2560e^{0.017185(75)} \approx 9289 \text{ million} .
> $$
>
> The model fits the actual population fairly well to the end of the 20th century, so the 1993 estimate is quite reliable. The 2025 prediction, an extrapolation far beyond the data, may not be.
>
> *Stewart: Example 3.8.1*

^ex-21-1

## Radioactive Decay

If $m(t)$ is the mass remaining from an initial mass $m_0$ of a radioactive substance after time $t$, the relative decay rate $-\dfrac{dm/dt}{m}$ has been found experimentally to be constant (it is positive, since $dm/dt < 0$). So $dm/dt = km$ with $k < 0$: radioactive substances decay at a rate proportional to the remaining mass, and by Theorem §21.1 the mass decays exponentially, $m(t) = m_0 e^{kt}$.

> [!definition] Definition §21.3: Half-Life
> The **half-life** of a radioactive substance is the time required for half of any given quantity of it to decay.
>
> *Stewart: 3.8 (text)*

^def-21-3

> [!example] Example §21.2: Radium-226
> The half-life of radium-226 is $1590$ years. (a) A sample has mass $100$ mg. Find a formula for the mass remaining after $t$ years. (b) Find the mass remaining after $1000$ years, to the nearest milligram. (c) When will the mass be reduced to $30$ mg?
>
> **(a)** Let $m(t)$ be the mass in mg after $t$ years. Then $dm/dt = km$ and $m(0) = 100$, so $m(t) = 100e^{kt}$ by Theorem §21.1. Use $m(1590) = \frac12 (100)$:
>
> $$
> 100e^{1590k} = 50, \qquad e^{1590k} = \tfrac12, \qquad 1590k = \ln\tfrac12 = -\ln 2, \qquad k = -\frac{\ln 2}{1590} .
> $$
>
> Therefore $m(t) = 100e^{-(\ln 2)t/1590}$. Since $e^{\ln 2} = 2$, this can also be written $m(t) = 100 \times 2^{-t/1590}$.
>
> **(b)** $m(1000) = 100e^{-(\ln 2)1000/1590} \approx 100e^{-0.43594} \approx 65$ mg.
>
> **(c)** Solve $m(t) = 30$, that is, $100e^{-(\ln 2)t/1590} = 30$, or $e^{-(\ln 2)t/1590} = 0.3$. Take natural logarithms:
>
> $$
> -\frac{\ln 2}{1590}\,t = \ln 0.3, \qquad t = -1590\,\frac{\ln 0.3}{\ln 2} \approx 2762 \text{ years} .
> $$
>
> (A graph of $m(t)$ with the line $m = 30$ shows the intersection near $t \approx 2800$, in agreement.)
>
> *Stewart: Example 3.8.2*

^ex-21-2

## Newton's Law of Cooling

> [!definition] Definition §21.4: Newton's Law of Cooling
> **Newton's Law of Cooling** states that the rate of cooling of an object is proportional to the temperature difference between the object and its surroundings, provided this difference is not too large (it applies to warming too). If $T(t)$ is the temperature of the object at time $t$ and $T_s$ the (constant) temperature of the surroundings, then
>
> $$
> \frac{dT}{dt} = k(T - T_s)
> $$
>
> for a constant $k$.
>
> *Stewart: 3.8 (text)*

^def-21-4

> [!theorem] Corollary §21.2: Solution of Newton's Law of Cooling
> The solutions of $\dfrac{dT}{dt} = k(T - T_s)$ are
>
> $$
> T(t) = T_s + \big(T(0) - T_s\big)e^{kt} .
> $$
>
> *Stewart: 3.8 (text)*

^cor-21-2

> [!proof]+ Proof
> The equation is not quite Equation 1, so change variable: $y(t) = T(t) - T_s$. Because $T_s$ is constant, $y'(t) = T'(t)$, and the equation becomes $dy/dt = ky$. By Theorem §21.1, $y(t) = y(0)e^{kt}$, that is, $T(t) - T_s = (T(0) - T_s)e^{kt}$.

^pf-21-2

*Uses:* [[§21 Exponential Growth and Decay#^thm-21-1|§21.1]]

> [!example] Example §21.3: Cooling Iced Tea
> A bottle of iced tea at room temperature ($72^\circ$F) is placed in a refrigerator where the temperature is $44^\circ$F. After half an hour the tea has cooled to $61^\circ$F. (a) What is its temperature after another half hour? (b) How long does it take to cool to $50^\circ$F?
>
> **(a)** Let $T(t)$ be the temperature after $t$ minutes. With $T_s = 44$, Newton's Law of Cooling says $dT/dt = k(T - 44)$. Let $y = T - 44$. Then $y(0) = 72 - 44 = 28$ and $dy/dt = ky$, so $y(t) = 28e^{kt}$. From $T(30) = 61$, $y(30) = 17$:
>
> $$
> 28e^{30k} = 17, \qquad e^{30k} = \tfrac{17}{28}, \qquad k = \frac{\ln\big(\frac{17}{28}\big)}{30} \approx -0.01663 .
> $$
>
> Thus $y(t) = 28e^{-0.01663t}$, $T(t) = 44 + 28e^{-0.01663t}$, and
>
> $$
> T(60) = 44 + 28e^{-0.01663(60)} \approx 54.3 .
> $$
>
> After another half hour the tea is at about $54^\circ$F. (Exactly: $e^{60k} = (e^{30k})^2 = (17/28)^2$, so $T(60) = 44 + 28 \cdot \frac{289}{784} = 44 + \frac{289}{28} \approx 54.3$.)
>
> **(b)** $T(t) = 50$ when
>
> $$
> 44 + 28e^{-0.01663t} = 50, \qquad e^{-0.01663t} = \tfrac{6}{28}, \qquad t = \frac{\ln\big(\frac{6}{28}\big)}{-0.01663} \approx 92.6 .
> $$
>
> The tea cools to $50^\circ$F after about $1$ hour $33$ minutes. As expected, $\lim_{t \to \infty} T(t) = 44 + 28 \cdot 0 = 44$: the tea approaches the temperature of the refrigerator.
>
> *Stewart: Example 3.8.3*

^ex-21-3

## Continuously Compounded Interest

If an amount $A_0$ is invested at interest rate $r$ (e.g. $r = 0.02$), compounded annually, it is worth $A_0(1 + r)^t$ after $t$ years. Compounded $n$ times per year, the rate per period is $r/n$ and there are $nt$ periods in $t$ years, so the value is

$$
A = A_0 \left( 1 + \frac{r}{n} \right)^{nt} .
$$

Letting $n \to \infty$ means compounding the interest **continuously**.

> [!theorem] Corollary §21.3: Continuous Compounding
> With continuous compounding of interest at rate $r$, an amount $A_0$ is worth
>
> $$
> A(t) = \lim_{n \to \infty} A_0 \left( 1 + \frac{r}{n} \right)^{nt} = A_0 e^{rt}
> $$
>
> after $t$ years. Equivalently, $\dfrac{dA}{dt} = rA_0 e^{rt} = rA(t)$: the investment grows at a rate proportional to its size.
>
> *Stewart: 3.8 (Example 3.8.4)*

^cor-21-3

> [!proof]+ Proof
> Let $r > 0$ and put $m = n/r$, so $m \to \infty$ as $n \to \infty$. Then
>
> $$
> \lim_{n \to \infty} A_0 \left( 1 + \frac{r}{n} \right)^{nt} = \lim_{n \to \infty} A_0 \left[ \left( 1 + \frac{r}{n} \right)^{n/r} \right]^{rt} = A_0 \left[ \lim_{m \to \infty} \left( 1 + \frac1m \right)^m \right]^{rt} = A_0 e^{rt} ,
> $$
>
> by Formula 6 of [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-7|Theorem §19.7]]. The limit passes inside the power $u \mapsto u^{rt}$ because this function is continuous at $u = e$ ([[§10 Continuity#^thm-10-7|Theorem §10.7]]); and $m = n/r$ need not be an integer, which is fine since Formula 6 holds with $m$ a real variable (it comes from $\lim_{x \to 0^+} (1 + x)^{1/x} = e$). Differentiating $A(t) = A_0 e^{rt}$ by the Chain Rule gives $dA/dt = rA_0 e^{rt} = rA(t)$.

^pf-21-3

*Uses:* [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^thm-19-7|§19.7]], [[§10 Continuity#^thm-10-7|§10.7]], [[§17 The Chain Rule#^cor-17-4|§17.4]]

> [!example] Example §21.4: Compounding More and More Often
> $\$5000$ is invested at $2\%$ interest for $3$ years. With annual compounding it is worth $\$5000(1.02) = \$5100.00$ after one year, $[\$5000(1.02)](1.02) = \$5202.00$ after two, and after three years:
>
> | compounding | value after 3 years |
> |---|---|
> | annual | $\$5000(1.02)^3 = \$5306.04$ |
> | semiannual | $\$5000(1.01)^6 = \$5307.60$ |
> | quarterly | $\$5000(1.005)^{12} = \$5308.39$ |
> | monthly | $\$5000\big(1 + \frac{0.02}{12}\big)^{36} = \$5308.92$ |
> | daily | $\$5000\big(1 + \frac{0.02}{365}\big)^{365 \cdot 3} = \$5309.17$ |
> | continuous | $\$5000e^{(0.02)3} = \$5309.18$ |
>
> The interest paid increases with the number $n$ of compounding periods, toward the continuous value of Corollary §21.3. That value is very close to the daily one and easier to compute.
>
> *Stewart: Example 3.8.4*

^ex-21-4
