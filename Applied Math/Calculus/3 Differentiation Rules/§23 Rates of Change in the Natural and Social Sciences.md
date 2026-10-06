---
type: section
subject: "[[Calculus]]"
chapter: 3
section: 23
stewart: "3.7"
aliases: ["Stewart 3.7"]
tags: [calculus]
---
← [[§22 Derivatives of Logarithmic and Inverse Trigonometric Functions]] · ↑ [[· 3 Differentiation Rules]] · [[§24 Exponential Growth and Decay]] →

*Stewart, Section 3.7.*

The derivative $dy/dx$ is the rate of change of $y$ with respect to $x$ ([[§14 Derivatives and Rates of Change#^def-14-4|Definition §14.4]]). Whenever $y = f(x)$ has a specific meaning in a science, its derivative has one too, measured in units of $y$ per unit of $x$. This section collects such interpretations: velocity and acceleration, linear density and current in physics, rates of reaction and compressibility in chemistry, growth rates and velocity gradients in biology, and marginal cost in economics. With the differentiation rules of [[§17 Derivatives of Polynomials and Exponential Functions|§17]]–[[§22 Derivatives of Logarithmic and Inverse Trigonometric Functions|§22]], each becomes a routine computation.

## Rates of Change

> [!definition] Definition §23.1: Average and Instantaneous Rate of Change
> Let $y = f(x)$. If $x$ changes from $x_1$ to $x_2$, the changes in $x$ and $y$ are
>
> $$
> \Delta x = x_2 - x_1, \qquad \Delta y = f(x_2) - f(x_1) .
> $$
>
> The difference quotient
>
> $$
> \frac{\Delta y}{\Delta x} = \frac{f(x_2) - f(x_1)}{x_2 - x_1}
> $$
>
> is the **average rate of change of $y$ with respect to $x$** over $[x_1, x_2]$: the slope of the secant line through $P(x_1, f(x_1))$ and $Q(x_2, f(x_2))$. Its limit as $\Delta x \to 0$ is the derivative $f'(x_1)$, the **instantaneous rate of change of $y$ with respect to $x$** at $x = x_1$: the slope of the tangent line at $P$. In Leibniz notation,
>
> $$
> \frac{dy}{dx} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} .
> $$
>
> The units of $dy/dx$ are the units of $y$ divided by the units of $x$.
>
> *Stewart: 3.7 (text)*

^def-23-1

## Physics

> [!definition] Definition §23.2: Velocity
> Let $s = f(t)$ be the position function of a particle moving in a straight line. Then $\Delta s / \Delta t$ is its average velocity over a time period $\Delta t$, and
>
> $$
> v = \frac{ds}{dt}
> $$
>
> is its (instantaneous) **velocity**, the rate of change of displacement with respect to time.
>
> The **speed** is $|v|$.
>
> *Stewart: 3.7 (text and Example 3.7.1)*

^def-23-2

> [!definition] Definition §23.3: Acceleration
> The **acceleration** is the rate of change of velocity with respect to time:
>
> $$
> a(t) = v'(t) = s''(t) .
> $$
>
> The particle **speeds up** when $v$ and $a$ have the same sign (it is pushed in the direction in which it moves) and **slows down** when they have opposite signs.
>
> *Stewart: 3.7 (text and Example 3.7.1)*

^def-23-3

> [!example] Example §23.1: Analyzing the Motion of a Particle
> The position of a particle is $s = f(t) = t^3 - 6t^2 + 9t$ ($t$ in seconds, $s$ in meters).
>
> **(a) Velocity.** $v(t) = \dfrac{ds}{dt} = 3t^2 - 12t + 9$.
>
> **(b)** After $2$ s: $v(2) = 3(2)^2 - 12(2) + 9 = -3$ m/s. After $4$ s: $v(4) = 3(4)^2 - 12(4) + 9 = 9$ m/s.
>
> **(c) At rest** when $v(t) = 0$: $3t^2 - 12t + 9 = 3(t^2 - 4t + 3) = 3(t - 1)(t - 3) = 0$, that is, after $1$ s and after $3$ s.
>
> **(d) Direction.** The particle moves in the positive direction when $v(t) = 3(t - 1)(t - 3) > 0$: both factors positive ($t > 3$) or both negative ($t < 1$). It moves backward when $1 < t < 3$. So it goes forward from $s = 0$ to $s = f(1) = 4$, back to $s = f(3) = 0$, then forward again.
>
> **(f) Total distance in the first five seconds.** Because the direction changes at $t = 1$ and $t = 3$, add the distances over $[0, 1]$, $[1, 3]$ and $[3, 5]$ separately:
>
> $$
> |f(1) - f(0)| = |4 - 0| = 4, \qquad |f(3) - f(1)| = |0 - 4| = 4, \qquad |f(5) - f(3)| = |20 - 0| = 20 .
> $$
>
> The total distance is $4 + 4 + 20 = 28$ m. (The net displacement $f(5) - f(0) = 20$ m is smaller.)
>
> **(g) Acceleration.** $a(t) = \dfrac{d^2 s}{dt^2} = \dfrac{dv}{dt} = 6t - 12$, so $a(4) = 6(4) - 12 = 12$ m/s².
>
> **(i) Speeding up and slowing down.** $v > 0$ for $t < 1$ and $t > 3$, and $v < 0$ for $1 < t < 3$; $a < 0$ for $t < 2$ and $a > 0$ for $t > 2$. The signs agree, and the particle speeds up, when $1 < t < 2$ and when $t > 3$. They differ, and it slows down, when $0 \le t < 1$ and when $2 < t < 3$.
>
> (Parts (e) and (h) of Stewart's example are the motion diagram and the graphs; see the figure below.)
>
> *Stewart: Example 3.7.1*

^ex-23-1

![[m233-20-1.svg]]
*[[§23 Rates of Change in the Natural and Social Sciences#^ex-23-1|Example §23.1]]: position $s$ (red), velocity $v$ (blue) and acceleration $a$ (green) for $0 \le t \le 5$. The particle reverses direction where $v = 0$ ($t = 1, 3$), and $a = 0$ at $t = 2$. It speeds up on the shaded intervals, where $v$ and $a$ have the same sign, and slows down on the others.*

> [!definition] Definition §23.4: Linear Density
> **Linear density.** Let the mass of a rod (or piece of wire), measured from its left end to the point $x$, be $m = f(x)$. The mass between $x_1$ and $x_2$ is $\Delta m = f(x_2) - f(x_1)$, and $\Delta m / \Delta x$ is the average density of that part of the rod. The **linear density** at $x_1$ is the limit of these average densities:
>
> $$
> \rho = \lim_{\Delta x \to 0} \frac{\Delta m}{\Delta x} = \frac{dm}{dx} ,
> $$
>
> the rate of change of mass with respect to length (kg/m). A homogeneous rod has constant density $\rho = m/l$.
>
> *Stewart: 3.7 (Examples 3.7.2 and 3.7.3)*

^def-23-4

> [!definition] Definition §23.5: Current
> **Current.** If $\Delta Q$ is the net charge that passes through a surface (a cross-section of a wire) during a time period $\Delta t$, then $\Delta Q / \Delta t$ is the average current, and the **current** at time $t_1$ is
>
> $$
> I = \lim_{\Delta t \to 0} \frac{\Delta Q}{\Delta t} = \frac{dQ}{dt} ,
> $$
>
> the rate at which charge flows through the surface (coulombs per second, called amperes).
>
> *Stewart: 3.7 (Examples 3.7.2 and 3.7.3)*

^def-23-5

> [!example] Example §23.2: Density of a Nonhomogeneous Rod
> A rod has mass $m = f(x) = \sqrt{x}$ kg from its left end to $x$ m. Over $1 \le x \le 1.2$ the average density is
>
> $$
> \frac{\Delta m}{\Delta x} = \frac{f(1.2) - f(1)}{1.2 - 1} = \frac{\sqrt{1.2} - 1}{0.2} \approx \frac{1.09545 - 1}{0.2} \approx 0.48 \text{ kg/m},
> $$
>
> while the density right at $x = 1$ is
>
> $$
> \rho = \frac{dm}{dx}\Big|_{x=1} = \frac{1}{2\sqrt{x}}\Big|_{x=1} = 0.50 \text{ kg/m} .
> $$
>
> *Stewart: Example 3.7.2*

^ex-23-2

Other rates of change in physics include power (the rate at which work is done), the rate of heat flow, the temperature gradient (the rate of change of temperature with respect to position), and the rate of decay of a radioactive substance ([[§24 Exponential Growth and Decay#^def-24-1|Definition §24.1]]).

## Chemistry

> [!definition] Definition §23.6: Rate of Reaction
> In a chemical reaction $\mathrm{A} + \mathrm{B} \to \mathrm{C}$, with reactants A, B and product C, the **concentration** $[\mathrm{A}]$ of A is the number of moles ($1$ mole $= 6.022 \times 10^{23}$ molecules) per liter; $[\mathrm{A}]$, $[\mathrm{B}]$, $[\mathrm{C}]$ are functions of time $t$. The average rate of reaction of C over $t_1 \le t \le t_2$ is $\Delta[\mathrm{C}]/\Delta t = \dfrac{[\mathrm{C}](t_2) - [\mathrm{C}](t_1)}{t_2 - t_1}$, and the **instantaneous rate of reaction** is
>
> $$
> \text{rate of reaction} = \lim_{\Delta t \to 0} \frac{\Delta[\mathrm{C}]}{\Delta t} = \frac{d[\mathrm{C}]}{dt} .
> $$
>
> The concentrations of the reactants decrease, so minus signs make their rates positive. Since $[\mathrm{A}]$ and $[\mathrm{B}]$ each decrease at the rate at which $[\mathrm{C}]$ increases,
>
> $$
> \text{rate of reaction} = \frac{d[\mathrm{C}]}{dt} = -\frac{d[\mathrm{A}]}{dt} = -\frac{d[\mathrm{B}]}{dt} .
> $$
>
> More generally, for a reaction $a\mathrm{A} + b\mathrm{B} \to c\mathrm{C} + d\mathrm{D}$,
>
> $$
> -\frac1a\,\frac{d[\mathrm{A}]}{dt} = -\frac1b\,\frac{d[\mathrm{B}]}{dt} = \frac1c\,\frac{d[\mathrm{C}]}{dt} = \frac1d\,\frac{d[\mathrm{D}]}{dt} .
> $$
>
> *Stewart: 3.7 (Example 3.7.4)*

^def-23-6

> [!definition] Definition §23.7: Isothermal Compressibility
> If a substance is kept at a constant temperature, its volume $V$ is a function of its pressure $P$. As $P$ increases, $V$ decreases, so $dV/dP < 0$. The **(isothermal) compressibility** is
>
> $$
> \beta = -\frac1V\,\frac{dV}{dP} ,
> $$
>
> which measures how fast, per unit volume, the volume decreases as the pressure increases at constant temperature. For instance, for a sample of air at $25^\circ$C with $V = 5.3/P$ ($V$ in m³, $P$ in kPa), at $P = 50$ kPa: $\dfrac{dV}{dP} = -\dfrac{5.3}{P^2} = -\dfrac{5.3}{2500} = -0.00212$ m³/kPa, and $\beta = \dfrac{0.00212}{5.3/50} = 0.02$ (m³/kPa)/m³.
>
> *Stewart: 3.7 (Example 3.7.5)*

^def-23-7

## Biology

> [!definition] Definition §23.8: Growth Rate
> **Growth rate.** If $n = f(t)$ is the number of individuals in an animal or plant population at time $t$, the average rate of growth over $t_1 \le t \le t_2$ is $\Delta n / \Delta t$, and the **instantaneous rate of growth** is
>
> $$
> \text{growth rate} = \lim_{\Delta t \to 0} \frac{\Delta n}{\Delta t} = \frac{dn}{dt} .
> $$
>
> *Stewart: 3.7 (Examples 3.7.6 and 3.7.7)*

^def-23-8

> [!definition] Definition §23.9: Velocity Gradient
> **Velocity gradient.** If the velocity $v$ of a fluid in a tube depends on the distance $r$ from the axis, the **velocity gradient** is the instantaneous rate of change of velocity with respect to $r$:
>
> $$
> \text{velocity gradient} = \lim_{\Delta r \to 0} \frac{\Delta v}{\Delta r} = \frac{dv}{dr} .
> $$
>
> *Stewart: 3.7 (Examples 3.7.6 and 3.7.7)*

^def-23-9

> [!remark] Remark: Smooth Models of Discrete Quantities
> Strictly speaking, a population function $n = f(t)$ is a step function: it jumps by $1$ at every birth or death, so it is discontinuous there and not differentiable. For a large population we replace its graph by a smooth approximating curve and differentiate that. The same applies to the cost of producing $x$ items when $x$ takes only integer values ([[§23 Rates of Change in the Natural and Social Sciences#^def-23-10|Definition §23.10]]).

^rem-23-1

> [!example] Example §23.3: Bacteria That Double Every Hour
> A population of bacteria in a homogeneous nutrient medium doubles every hour. If the initial population is $n_0$ and $t$ is measured in hours, then $f(1) = 2f(0) = 2n_0$, $f(2) = 2f(1) = 2^2 n_0$, $f(3) = 2f(2) = 2^3 n_0$, and in general $f(t) = 2^t n_0$. By [[§20 The Chain Rule#^thm-20-5|Theorem §20.5]], $\frac{d}{dt}(b^t) = b^t \ln b$, so the rate of growth at time $t$ is
>
> $$
> \frac{dn}{dt} = \frac{d}{dt}(n_0 2^t) = n_0 2^t \ln 2 .
> $$
>
> With $n_0 = 100$, after $4$ hours
>
> $$
> \frac{dn}{dt}\Big|_{t=4} = 100 \cdot 2^4 \ln 2 = 1600 \ln 2 \approx 1109 :
> $$
>
> the population is growing at about $1109$ bacteria per hour.
>
> *Stewart: Example 3.7.6*

^ex-23-3

*Chain:* ← [[§4 Exponential Functions#^ex-4-3|Chapter 1]]

> [!example] Example §23.4: Blood Flow in an Artery
> Model a blood vessel as a cylindrical tube of radius $R$ and length $l$. Friction at the wall makes the velocity $v$ of the blood greatest along the axis and $0$ at the wall. Poiseuille's **law of laminar flow** (1838) states
>
> $$
> v = \frac{P}{4\eta l}(R^2 - r^2), \qquad 0 \le r \le R , \qquad (1)
> $$
>
> where $\eta$ is the viscosity of the blood and $P$ the pressure difference between the ends of the tube. With $P$ and $l$ constant, the velocity gradient is
>
> $$
> \frac{dv}{dr} = \frac{P}{4\eta l}(0 - 2r) = -\frac{Pr}{2\eta l} .
> $$
>
> For one of the smaller human arteries take $\eta = 0.027$, $R = 0.008$ cm, $l = 2$ cm and $P = 4000$ dynes/cm². Then
>
> $$
> v = \frac{4000}{4(0.027)2}\,(0.000064 - r^2) \approx 1.85 \times 10^4\,(6.4 \times 10^{-5} - r^2) .
> $$
>
> At $r = 0.002$ cm, $v(0.002) \approx 1.85 \times 10^4\,(64 \times 10^{-6} - 4 \times 10^{-6}) = 1.11$ cm/s, and
>
> $$
> \frac{dv}{dr}\Big|_{r=0.002} = -\frac{4000(0.002)}{2(0.027)2} \approx -74 \text{ (cm/s)/cm} .
> $$
>
> In micrometers ($1$ cm $= 10{,}000$ μm): the radius is $80$ μm, the velocity is $11{,}850$ μm/s on the axis and $11{,}110$ μm/s at $r = 20$ μm, and $dv/dr = -74$ (μm/s)/μm there: the velocity decreases by about $74$ μm/s for each micrometer away from the center.
>
> *Stewart: Example 3.7.7*

^ex-23-4

## Economics

> [!definition] Definition §23.10: Cost Function and Marginal Cost
> If $C(x)$ is the total cost of producing $x$ units of a commodity, $C$ is a **cost function**. Increasing production from $x_1$ to $x_2$ costs $\Delta C = C(x_2) - C(x_1)$ more, at the average rate
>
> $$
> \frac{\Delta C}{\Delta x} = \frac{C(x_2) - C(x_1)}{x_2 - x_1} = \frac{C(x_1 + \Delta x) - C(x_1)}{\Delta x} .
> $$
>
> The instantaneous rate of change of cost with respect to the number of items is the **marginal cost**:
>
> $$
> \text{marginal cost} = \lim_{\Delta x \to 0} \frac{\Delta C}{\Delta x} = \frac{dC}{dx} .
> $$
>
> Taking $\Delta x = 1$ and $n$ large, $C'(n) \approx C(n + 1) - C(n)$: the marginal cost of producing $n$ units is approximately the cost of producing one more unit, the $(n + 1)$st.
>
> *Stewart: 3.7 (Example 3.7.8)*

^def-23-10

> [!example] Example §23.5: Marginal Cost
> Cost functions are often polynomials $C(x) = a + bx + cx^2 + dx^3$: $a$ is the overhead (rent, heat, maintenance), and the other terms are raw materials, labor and so on (labor may grow faster than linearly because of overtime and inefficiencies at large scale). Suppose
>
> $$
> C(x) = 10{,}000 + 5x + 0.01x^2 \text{ dollars} .
> $$
>
> The marginal cost function is $C'(x) = 5 + 0.02x$, and at a production level of $500$ items
>
> $$
> C'(500) = 5 + 0.02(500) = \$15/\text{item} .
> $$
>
> This is the rate at which costs increase at $x = 500$, and it predicts the cost of the $501$st item. The actual cost of the $501$st item is
>
> $$
> C(501) - C(500) = [10{,}000 + 5(501) + 0.01(501)^2] - [10{,}000 + 5(500) + 0.01(500)^2] = 5 + 0.01(501^2 - 500^2) = 5 + 10.01 = \$15.01 ,
> $$
>
> so indeed $C'(500) \approx C(501) - C(500)$. (Marginal demand, revenue and profit are taken up in Chapter 4, with optimization: [[§34 Optimization Problems#^def-34-1|Definition §34.1]], [[§34 Optimization Problems#^def-34-2|Definition §34.2]] and [[§34 Optimization Problems#^def-34-3|Definition §34.3]].)
>
> *Stewart: Example 3.7.8*

^ex-23-5

## A Single Idea, Many Interpretations

> [!remark]- Remark: Other Sciences
> Rates of change occur in all the sciences. A geologist studies the rate at which an intruded body of molten rock cools by conduction of heat into surrounding rocks; an engineer, the rate at which water flows out of a reservoir; an urban geographer, the rate of change of population density with distance from the city center; a meteorologist, the rate of change of atmospheric pressure with height. In psychology, the learning curve $P(t)$ measures performance after training time $t$, and $dP/dt$ is the rate at which performance improves; there are also models for the rate of memory retention. In sociology, if $p(t)$ is the proportion of a population that knows a rumor by time $t$, then $dp/dt$ is the rate at which the rumor spreads.
>
> Velocity, density, current, power and temperature gradient in physics; rate of reaction and compressibility in chemistry; rate of growth and blood velocity gradient in biology; marginal cost and marginal profit in economics; rate of heat flow in geology; rate of improvement of performance in psychology; rate of spread of a rumor in sociology: all are special cases of a single mathematical concept, the derivative. Part of the power of mathematics lies in this abstractness: properties proved once for the derivative apply in every science. Fourier: "Mathematics compares the most diverse phenomena and discovers the secret analogies that unite them."

^rem-23-2
