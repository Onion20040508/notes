---
type: section
subject: "[[Calculus]]"
chapter: 8
section: 55
stewart: "8.4"
aliases: ["Stewart 8.4"]
tags: [calculus]
---
← [[§54 Applications to Physics and Engineering]] · ↑ [[· 8 Further Applications of Integration]] · [[§56 Probability]] →

*Stewart, Section 8.4.*

Three more quantities come out of the slice-and-add strategy of [[§54 Applications to Physics and Engineering|§54]]. In economics, the consumer surplus measures how much buyers save because they pay the market price rather than the most they would have paid. It is an area between the demand curve and the price line. In biology, Poiseuille's Law gives the rate at which blood flows through a vessel, obtained by cutting the cross-section into thin rings; the flux turns out to grow like the fourth power of the radius. Finally, the dye dilution method measures how much blood the heart pumps, by integrating dye concentrations read off at a few instants (in practice with Simpson's Rule).

## Consumer Surplus

> [!definition] Definition §55.1: Demand Function
> The **demand function** $p(x)$ is the price that a company can charge in order to sell $x$ units of a commodity ([[§31 Optimization Problems#^def-31-1|Definition §31.1]]). Selling larger quantities usually requires lowering prices, so the demand function is usually decreasing. Its graph is the **demand curve**. If $X$ is the amount of the commodity that can currently be sold, then $P = p(X)$ is the current selling price.
>
> *Stewart: 8.4 (text)*

^def-55-1

> [!definition] Definition §55.2: Consumer Surplus
> The **consumer surplus** for a good is the difference between what consumers are willing to pay and what they actually pay. For a demand function $p$, at sales level $X$ and current price $P = p(X)$, the total consumer surplus is
>
> $$
> \int_0^X \big[ p(x) - P \big]\,dx .
> $$
>
> It is the area under the demand curve and above the line $p = P$, $0 \le x \le X$. By finding it, economists assess the overall benefit of a market to society.
>
> *Stewart: 8.4, Equation 1*

^def-55-2

> [!remark] Remark: Why It Works
> Divide $[0, X]$ into $n$ subintervals of length $\Delta x = X/n$ and let $x_i^* = x_i$ be the right endpoint of the $i$th one. According to the demand curve, $x_{i-1}$ units would be bought at a price of $p(x_{i-1})$ dollars per unit; to sell $x_i$ units the price must drop to $p(x_i)$, and then an additional $\Delta x$ units are sold (but no more). The consumers who buy these $\Delta x$ units would have paid $p(x_i)$ dollars, the value of the product to them. Paying only $P$, they save
>
> $$
> (\text{savings per unit})(\text{number of units}) = \big[ p(x_i) - P \big]\,\Delta x .
> $$
>
> Adding over all such groups of consumers, the total savings are $\sum_{i=1}^n [p(x_i) - P]\,\Delta x$, the area of the rectangles in the figure below. This is a Riemann sum of $p(x) - P$ on $[0, X]$, so as $n \to \infty$ it tends to the integral of Definition §55.2: the amount of money saved by consumers who buy the commodity at price $P$, corresponding to the amount demanded $X$.

^rem-55-1

![[m233-55-1.svg]]
*Consumer surplus. The group of consumers buying between $x_{i-1}$ and $x_i$ units would pay $p(x_i)$ but pays only $P$, saving $[p(x_i) - P]\,\Delta x$: one rectangle above the red price line. The rectangles fill out the area between the demand curve and $p = P$ (light blue) as $\Delta x \to 0$.*

> [!example] Example §55.1: Consumer Surplus for a Quadratic Demand Curve
> The demand for a product, in dollars, is
>
> $$
> p = 1200 - 0.2x - 0.0001x^2 .
> $$
>
> Find the consumer surplus when the sales level is $500$.
>
> The number of products sold is $X = 500$, so the price is
>
> $$
> P = 1200 - (0.2)(500) - (0.0001)(500)^2 = 1200 - 100 - 25 = 1075 .
> $$
>
> By Definition §55.2, the consumer surplus is
>
> $$
> \begin{aligned}
> \int_0^{500} \big[ p(x) - P \big]\,dx &= \int_0^{500} \big( 1200 - 0.2x - 0.0001x^2 - 1075 \big)\,dx = \int_0^{500} \big( 125 - 0.2x - 0.0001x^2 \big)\,dx \\
> &= \Big[ 125x - 0.1x^2 - (0.0001)\frac{x^3}{3} \Big]_0^{500} = (125)(500) - (0.1)(500)^2 - \frac{(0.0001)(500)^3}{3} \\
> &= 62{,}500 - 25{,}000 - 4166.67 = \$33{,}333.33 .
> \end{aligned}
> $$
>
> *Stewart: Example 8.4.1*

^ex-55-1

> [!definition] Definition §55.3: Supply Function
> The **supply function** $p_S(x)$ of a commodity gives the selling price at which manufacturers will produce $x$ units. For a higher price more is produced, so $p_S$ is increasing.
>
> *Stewart: 8.4, Exercises 9–11 (producer surplus), Exercise 12 (equilibrium), Exercises 13–14 (total surplus)*

^def-55-3

> [!definition] Definition §55.3: Producer Surplus
> If $X$ units are currently produced, at price $P = p_S(X)$, some producers would have sold for less; the excess is the **producer surplus**,
>
> $$
> \int_0^X \big[ P - p_S(x) \big]\,dx ,
> $$
>
> the area between the line $p = P$ and the supply curve (the same argument as in Remark: Why It Works, with producers in place of consumers).
>
> *Stewart: 8.4, Exercises 9–11 (producer surplus), Exercise 12 (equilibrium), Exercises 13–14 (total surplus)*

^def-55-new1

> [!definition] Definition §55.3: Market Equilibrium
> A market is in **equilibrium** when the quantity demanded equals the quantity supplied: the equilibrium quantity and price are the coordinates of the point where the demand and supply curves cross.
>
> *Stewart: 8.4, Exercises 9–11 (producer surplus), Exercise 12 (equilibrium), Exercises 13–14 (total surplus)*

^def-55-new2

> [!definition] Definition §55.3: Total Surplus
> Consumer surplus plus producer surplus is the **total surplus**; for a good in equilibrium it is maximized.
>
> *Stewart: 8.4, Exercises 9–11 (producer surplus), Exercise 12 (equilibrium), Exercises 13–14 (total surplus)*

^def-55-new3

> [!example] Example §55.2: Market Equilibrium
> Given the demand curve $p = 50 - \frac{1}{20}x$ and the supply curve $p = 20 + \frac{1}{10}x$, find the quantity and price at which the market is in equilibrium, and the consumer and producer surplus there.
>
> **Equilibrium.** Set the prices equal:
>
> $$
> 50 - \frac{x}{20} = 20 + \frac{x}{10} \iff 30 = \frac{3x}{20} \iff x = 200, \qquad P = 50 - \frac{200}{20} = 40 .
> $$
>
> So $200$ units are sold at $\$40$.
>
> **Consumer surplus** (Definition §55.2):
>
> $$
> \int_0^{200} \Big[ \Big(50 - \frac{x}{20}\Big) - 40 \Big]\,dx = \int_0^{200} \Big( 10 - \frac{x}{20} \Big)\,dx = \Big[ 10x - \frac{x^2}{40} \Big]_0^{200} = 2000 - 1000 = \$1000 .
> $$
>
> **Producer surplus** ([[§55 Applications to Economics and Biology#^def-55-new1|Definition §55.3]]):
>
> $$
> \int_0^{200} \Big[ 40 - \Big(20 + \frac{x}{10}\Big) \Big]\,dx = \int_0^{200} \Big( 20 - \frac{x}{10} \Big)\,dx = \Big[ 20x - \frac{x^2}{20} \Big]_0^{200} = 4000 - 2000 = \$2000 .
> $$
>
> Both regions are triangles with base $200$ and heights $50 - 40 = 10$ and $40 - 20 = 20$, which confirms $\frac12 \cdot 200 \cdot 10 = 1000$ and $\frac12 \cdot 200 \cdot 20 = 2000$. The total surplus is $\$3000$.
>
> *Stewart: Exercise 8.4.12*

^ex-55-2

![[m233-55-2.svg]]
*Example §55.2. At the equilibrium $(200, 40)$ the consumer surplus (blue) lies between the demand curve and the price line, and the producer surplus (green) between the price line and the supply curve.*

## Blood Flow

> [!definition] Definition §55.4: Flux
> The **flux** (or **discharge**) of a fluid through a tube is the volume of fluid that passes a cross-section per unit time.
>
> *Stewart: 8.4 (text)*

^def-55-4

> [!theorem] Theorem §55.1: Poiseuille's Law
> Blood flows along a blood vessel of radius $R$ and length $l$; $P$ is the pressure difference between the ends of the vessel and $\eta$ the viscosity of the blood. Suppose the velocity of the blood at distance $r$ from the central axis is given by the law of laminar flow ([[§20 Rates of Change in the Natural and Social Sciences#^ex-20-4|Example §20.4]], Stewart's Example 3.7.7),
>
> $$
> v(r) = \frac{P}{4\eta l}\,(R^2 - r^2), \qquad 0 \le r \le R .
> $$
>
> Then the flux is
>
> $$
> F = \int_0^R 2\pi r\,v(r)\,dr = \frac{\pi P R^4}{8\eta l} .
> $$
>
> The flux is proportional to the fourth power of the radius of the vessel: halving the radius divides the flux by $16$.
>
> *Stewart: 8.4, Equation 2*

^thm-55-1

> [!proof]+ Proof
> **The integral (Stewart's argument).** Take equally spaced radii $0 = r_0 < r_1 < \cdots < r_n = R$ with $\Delta r = r_i - r_{i-1}$. The ring (washer) with inner radius $r_{i-1}$ and outer radius $r_i$ has area approximately $2\pi r_i\,\Delta r$. If $\Delta r$ is small, the velocity is almost constant on the ring, about $v(r_i)$, so the volume of blood crossing the ring per unit time is about $(2\pi r_i\,\Delta r)\,v(r_i)$. The total flux is about $\sum_{i=1}^n 2\pi r_i v(r_i)\,\Delta r$, a Riemann sum with limit $\int_0^R 2\pi r\,v(r)\,dr$. The velocity, and hence the volume per unit time, increases toward the center of the vessel.
>
> (To make "about" precise: the exact area of the ring is $a_i = \pi(r_i^2 - r_{i-1}^2) = \int_{r_{i-1}}^{r_i} 2\pi r\,dr$. Since $v$ is decreasing, the velocity on the ring lies between $v(r_i)$ and $v(r_{i-1})$, so both the flux $F_i$ through the ring and the integral $\int_{r_{i-1}}^{r_i} 2\pi r\,v(r)\,dr$ lie between $v(r_i)\,a_i$ and $v(r_{i-1})\,a_i$. Adding, $F$ and $\int_0^R 2\pi r\,v(r)\,dr$ differ by at most
>
> $$
> \sum_{i=1}^n \big[ v(r_{i-1}) - v(r_i) \big]\,a_i \le 2\pi R\,\Delta r \sum_{i=1}^n \big[ v(r_{i-1}) - v(r_i) \big] = 2\pi R\,\Delta r\,\big[ v(0) - v(R) \big] ,
> $$
>
> using $a_i = \pi(r_i + r_{i-1})\,\Delta r \le 2\pi R\,\Delta r$ and a telescoping sum. This tends to $0$ as $\Delta r \to 0$, so they are equal.)
>
> **The computation.**
>
> $$
> \begin{aligned}
> F &= \int_0^R 2\pi r \cdot \frac{P}{4\eta l}\,(R^2 - r^2)\,dr = \frac{\pi P}{2\eta l} \int_0^R (R^2 r - r^3)\,dr = \frac{\pi P}{2\eta l} \Big[ R^2 \frac{r^2}{2} - \frac{r^4}{4} \Big]_{r=0}^{r=R} \\
> &= \frac{\pi P}{2\eta l} \Big[ \frac{R^4}{2} - \frac{R^4}{4} \Big] = \frac{\pi P}{2\eta l} \cdot \frac{R^4}{4} = \frac{\pi P R^4}{8\eta l} .
> \end{aligned}
> $$

^pf-55-1

*Uses:* [[§55 Applications to Economics and Biology#^def-55-4|Def. §55.4]], [[§20 Rates of Change in the Natural and Social Sciences#^ex-20-4|Ex. §20.4]] (law of laminar flow), [[§35 The Definite Integral#^def-35-1|Def. §35.1]] (Riemann sums), [[§35 The Definite Integral#^thm-35-5|§35.5]] (additivity over adjacent intervals), [[§35 The Definite Integral#^thm-35-6|§35.6]] (comparison properties)

> [!remark]- Connections
> - The flux is the double integral of the velocity over the disk $D$ of radius $R$, and $\int_0^R 2\pi r\,v(r)\,dr$ is that integral in polar coordinates for a velocity depending only on $r$: $\iint_D v\,dA = \int_0^{2\pi}\!\int_0^R v(r)\,r\,dr\,d\theta$ ([[§100 Double Integrals in Polar Coordinates#^thm-100-1|Theorem §100.1]]; rigorously [[§15 Multivariable Integration#^thm-15-7|452 Thm. §15.7]]). The rings are the polar rectangles with $\theta$ running all the way around.

## Cardiac Output

Blood returns from the body through the veins, enters the right atrium of the heart, and is pumped through the pulmonary arteries to the lungs for oxygenation. It then flows back into the left atrium through the pulmonary veins and out to the rest of the body through the aorta.

> [!definition] Definition §55.5: Cardiac Output
> The **cardiac output** of the heart is the volume of blood pumped by the heart per unit time, that is, the rate of flow into the aorta.
>
> *Stewart: 8.4 (text)*

^def-55-5

> [!theorem] Theorem §55.2: Dye Dilution Formula
> In the **dye dilution method**, an amount $A$ of dye is injected into the right atrium and flows through the heart into the aorta, where a probe measures the concentration $c(t)$ of dye leaving the heart over a time interval $[0, T]$ until the dye has cleared. If the rate of flow $F$ is constant and $c$ is continuous, the cardiac output is
>
> $$
> F = \frac{A}{\displaystyle\int_0^T c(t)\,dt} .
> $$
>
> In practice $c$ is known only at equally spaced times, and the integral is approximated numerically.
>
> *Stewart: 8.4, Equation 3*

^thm-55-2

> [!proof]+ Proof
> Divide $[0, T]$ into subintervals of equal length $\Delta t$. During the time from $t_{i-1}$ to $t_i$, a volume $F\,\Delta t$ of blood flows past the measuring point, with concentration about $c(t_i)$, so the amount of dye carried past is about
>
> $$
> (\text{concentration})(\text{volume}) = c(t_i)\,(F\,\Delta t) .
> $$
>
> The total amount of dye is about $\sum_{i=1}^n c(t_i) F\,\Delta t = F \sum_{i=1}^n c(t_i)\,\Delta t$, and letting $n \to \infty$, all of the dye having passed by time $T$,
>
> $$
> A = F \int_0^T c(t)\,dt .
> $$
>
> Solving for $F$ gives the formula.
>
> (Precisely: if $m_i$ and $M_i$ are the minimum and maximum of $c$ on $[t_{i-1}, t_i]$, the dye carried past in that time is between $m_i F\,\Delta t$ and $M_i F\,\Delta t$. So $A$ lies between $F$ times the lower and upper sums $\sum m_i\,\Delta t$ and $\sum M_i\,\Delta t$ of $c$, and both of these tend to $\int_0^T c(t)\,dt$ for continuous $c$.)

^pf-55-2

*Uses:* [[§55 Applications to Economics and Biology#^def-55-5|Def. §55.5]], [[§35 The Definite Integral#^def-35-1|Def. §35.1]] (Riemann sums), [[§35 The Definite Integral#^thm-35-1|§35.1]] (continuous functions are integrable)

> [!example] Example §55.3: Estimating Cardiac Output
> A $5$-mg dose (a bolus) of dye is injected into a patient's right atrium. The concentration of the dye (in milligrams per liter) is measured in the aorta at one-second intervals:
>
> | $t$ (s) | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> | $c(t)$ (mg/L) | $0$ | $0.4$ | $2.8$ | $6.5$ | $9.8$ | $8.9$ | $6.1$ | $4.0$ | $2.3$ | $1.1$ | $0$ |
>
> Estimate the cardiac output.
>
> Here $A = 5$, $\Delta t = 1$ and $T = 10$. Approximate the integral by Simpson's Rule with $n = 10$ ([[§50 Approximate Integration#^def-50-5|Definition §50.5]]):
>
> $$
> \begin{aligned}
> \int_0^{10} c(t)\,dt &\approx \frac13 \big[ 0 + 4(0.4) + 2(2.8) + 4(6.5) + 2(9.8) + 4(8.9) + 2(6.1) + 4(4.0) + 2(2.3) + 4(1.1) + 0 \big] \\
> &= \frac13 \big[ 1.6 + 5.6 + 26 + 19.6 + 35.6 + 12.2 + 16 + 4.6 + 4.4 \big] = \frac{125.6}{3} \approx 41.87 .
> \end{aligned}
> $$
>
> By Theorem §55.2,
>
> $$
> F = \frac{A}{\int_0^{10} c(t)\,dt} \approx \frac{5}{41.87} \approx 0.12\ \text{L/s} = 7.2\ \text{L/min} .
> $$
>
> (Units: $c$ in mg/L and $t$ in s give $\int c\,dt$ in mg$\cdot$s/L, so $A / \int c\,dt$ is in L/s; $0.1194 \times 60 \approx 7.2$.)
>
> *Stewart: Example 8.4.2*

^ex-55-3
