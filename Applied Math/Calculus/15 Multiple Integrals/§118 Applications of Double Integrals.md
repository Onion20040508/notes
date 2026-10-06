---
type: section
subject: "[[Calculus]]"
chapter: 15
section: 118
stewart: "15.4"
aliases: ["Stewart 15.4"]
tags: [calculus, math233]
---
← [[§117 Double Integrals in Polar Coordinates]] · ↑ [[· 15 Multiple Integrals]] · [[§119 Surface Area]] →

*Stewart, Section 15.4 · MATH 233 (UMass, Spring 2023): this section was not on the course syllabus.*

Volume is one application of double integrals. This section gives the physical and probabilistic ones: whenever a quantity is spread over a plane region with a density (mass per unit area, charge per unit area, probability per unit area), the total is the double integral of the density. Weighting the density by $x$, $y$ or the squared distance to an axis gives moments, the center of mass and moments of inertia. In probability the density is a joint density function of two random variables, and the analogues of the center of mass are their expected values. All the definitions follow the same pattern: cut the region into small rectangles, approximate the quantity on each, add, and pass to the limit, which is a double integral by [[§115 Double Integrals Over Rectangles#^def-115-2|Definition §115.2]].

## Density and Mass

In [[§63 Moments and Centers of Mass#^thm-63-3|Theorem §63.3]] single integrals gave the moments and center of mass of a thin plate (lamina) of constant density. With double integrals the density may vary.

> [!definition] Definition §141.1: Density of a Lamina
> Suppose a lamina occupies a region $D$ of the $xy$-plane and its **density** (in units of mass per unit area) at a point $(x, y)$ of $D$ is $\rho(x, y)$, where $\rho$ is continuous on $D$. That is,
>
> $$
> \rho(x, y) = \lim \frac{\Delta m}{\Delta A} ,
> $$
>
> where $\Delta m$ and $\Delta A$ are the mass and area of a small rectangle containing $(x, y)$ and the limit is taken as the dimensions of the rectangle approach $0$.
>
> *Stewart: 15.4, Equation 1*

^def-118-1

> [!definition] Definition §141.2: Mass of a Lamina
> Let a lamina occupy a region $D$ with density $\rho(x, y)$ ([[§118 Applications of Double Integrals#^def-118-1|Definition §118.1]]). Enclose $D$ in a rectangle, divide it into subrectangles $R_{ij}$, and let $\rho = 0$ outside $D$. The mass of the part of the lamina in $R_{ij}$ is approximately $\rho(x_{ij}^{\ast}, y_{ij}^{\ast})\,\Delta A$, and the **total mass** of the lamina is
>
> $$
> m = \lim_{k, l \to \infty} \sum_{i=1}^k \sum_{j=1}^l \rho(x_{ij}^*, y_{ij}^*)\,\Delta A = \iint_D \rho(x, y)\,dA . \qquad (1)
> $$
>
> *Stewart: 15.4, Equation 1*

^def-118-2

> [!definition] Definition §141.3: Charge
> If an electric charge is distributed over a region $D$ with **charge density** $\sigma(x, y)$ (in units of charge per unit area), the **total charge** is
>
> $$
> Q = \iint_D \sigma(x, y)\,dA . \qquad (2)
> $$
>
> For example (Stewart's Example 15.4.1), the charge density $\sigma(x, y) = xy$ C/m² on the triangle $D$ with vertices $(0, 1)$, $(1, 1)$, $(1, 0)$, that is $0 \le x \le 1$, $1 - x \le y \le 1$, gives $Q = \int_0^1 \int_{1-x}^1 xy\,dy\,dx = \frac12 \int_0^1 (2x^2 - x^3)\,dx = \frac{5}{24}$ C.
>
> *Stewart: 15.4, Equation 2*

^def-118-3

## Moments and Centers of Mass

The moment of a particle about an axis is its mass times its directed distance from the axis ([[§63 Moments and Centers of Mass#^def-63-3|Definition §63.3]]). The mass of $R_{ij}$ is about $\rho(x_{ij}^*, y_{ij}^*)\,\Delta A$, so its moment about the $x$-axis is about $[\rho(x_{ij}^*, y_{ij}^*)\,\Delta A]\,y_{ij}^*$.

> [!definition] Definition §141.4: Moments of a Lamina
> The **moment** of the lamina **about the $x$-axis** and **about the $y$-axis** are
>
> $$
> M_x = \lim_{m, n \to \infty} \sum_{i=1}^m \sum_{j=1}^n y_{ij}^*\,\rho(x_{ij}^*, y_{ij}^*)\,\Delta A = \iint_D y\,\rho(x, y)\,dA , \qquad (3)
> $$
>
> $$
> M_y = \lim_{m, n \to \infty} \sum_{i=1}^m \sum_{j=1}^n x_{ij}^*\,\rho(x_{ij}^*, y_{ij}^*)\,\Delta A = \iint_D x\,\rho(x, y)\,dA . \qquad (4)
> $$
>
> *Stewart: 15.4, Equations 3, 4 and 5*

^def-118-4

> [!definition] Definition §118.5: Center of Mass of a Lamina
> The **center of mass** $(\bar x, \bar y)$ of the lamina is defined by $m\bar x = M_y$ and $m\bar y = M_x$, with the moments of [[§118 Applications of Double Integrals#^def-118-4|Definition §118.4]]:
>
> $$
> \bar x = \frac{M_y}{m} = \frac1m \iint_D x\,\rho(x, y)\,dA , \qquad \bar y = \frac{M_x}{m} = \frac1m \iint_D y\,\rho(x, y)\,dA , \qquad m = \iint_D \rho(x, y)\,dA . \qquad (5)
> $$
>
> *Stewart: 15.4, Equations 3, 4 and 5*

^def-118-5

Physically, the lamina behaves as if its entire mass were concentrated at its center of mass: supported at $(\bar x, \bar y)$, it balances horizontally.

> [!example] Example §141.1: A Triangular Lamina with Variable Density
> Find the mass and center of mass of a triangular lamina with vertices $(0, 0)$, $(1, 0)$ and $(0, 2)$ if the density function is $\rho(x, y) = 1 + 3x + y$.
>
> The upper boundary is the line through $(1, 0)$ and $(0, 2)$, $y = 2 - 2x$, so $D = \{0 \le x \le 1,\ 0 \le y \le 2 - 2x\}$.
>
> **Mass.** At $y = 2 - 2x$ the antiderivative $y + 3xy + \frac{y^2}{2}$ equals $(2 - 2x) + 3x(2 - 2x) + 2(1 - x)^2 = 4 - 4x^2$, so
>
> $$
> m = \int_0^1 \int_0^{2 - 2x} (1 + 3x + y)\,dy\,dx = \int_0^1 \Big[ y + 3xy + \frac{y^2}{2} \Big]_{y=0}^{y=2-2x} dx = 4\int_0^1 (1 - x^2)\,dx = 4\Big[ x - \frac{x^3}{3} \Big]_0^1 = \frac83 .
> $$
>
> **The coordinate $\bar x$.**
>
> $$
> \bar x = \frac1m \iint_D x\rho\,dA = \frac38 \int_0^1 \int_0^{2-2x} (x + 3x^2 + xy)\,dy\,dx = \frac38 \int_0^1 \Big[ xy + 3x^2 y + x\frac{y^2}{2} \Big]_{y=0}^{y=2-2x} dx = \frac32 \int_0^1 (x - x^3)\,dx = \frac32 \Big[ \frac{x^2}{2} - \frac{x^4}{4} \Big]_0^1 = \frac38 .
> $$
>
> **The coordinate $\bar y$.**
>
> $$
> \begin{aligned}
> \bar y &= \frac1m \iint_D y\rho\,dA = \frac38 \int_0^1 \int_0^{2-2x} (y + 3xy + y^2)\,dy\,dx = \frac38 \int_0^1 \Big[ \frac{y^2}{2} + 3x\frac{y^2}{2} + \frac{y^3}{3} \Big]_{y=0}^{y=2-2x} dx \\
> &= \frac14 \int_0^1 (7 - 9x - 3x^2 + 5x^3)\,dx = \frac14 \Big[ 7x - 9\frac{x^2}{2} - x^3 + 5\frac{x^4}{4} \Big]_0^1 = \frac{11}{16} .
> \end{aligned}
> $$
>
> The center of mass is $\big(\frac38, \frac{11}{16}\big)$. (The centroid of the triangle, for constant density, is $\big(\frac13, \frac23\big)$; the density $1 + 3x + y$ is larger to the right and above, and pulls the center of mass that way.)
>
> *Stewart: Example 15.4.2*

^ex-118-1

> [!example] Example §141.2: A Semicircular Lamina
> The density at any point of a semicircular lamina is proportional to the distance from the center of the circle. Find the center of mass of the lamina.
>
> Place the lamina as the upper half of the disk $x^2 + y^2 \le a^2$. The distance from $(x, y)$ to the center is $\sqrt{x^2 + y^2}$, so $\rho(x, y) = K\sqrt{x^2 + y^2} = Kr$ for a constant $K$. Both the density and the shape suggest polar coordinates ([[§117 Double Integrals in Polar Coordinates#^thm-117-1|Theorem §117.1]]): $D$ is $0 \le r \le a$, $0 \le \theta \le \pi$.
>
> **Mass.**
>
> $$
> m = \iint_D K\sqrt{x^2 + y^2}\,dA = \int_0^{\pi} \int_0^a (Kr)\,r\,dr\,d\theta = K\int_0^{\pi} d\theta \int_0^a r^2\,dr = K\pi \frac{a^3}{3} .
> $$
>
> **Center of mass.** The lamina and the density are symmetric with respect to the $y$-axis, so $\bar x = 0$. And
>
> $$
> \bar y = \frac1m \iint_D y\rho\,dA = \frac{3}{K\pi a^3} \int_0^{\pi} \int_0^a (r\sin\theta)(Kr)\,r\,dr\,d\theta = \frac{3}{\pi a^3} \int_0^{\pi} \sin\theta\,d\theta \int_0^a r^3\,dr = \frac{3}{\pi a^3} \cdot 2 \cdot \frac{a^4}{4} = \frac{3a}{2\pi} .
> $$
>
> The center of mass is $\big(0, \frac{3a}{2\pi}\big)$. For the same semicircle with uniform density the center of mass is $\big(0, \frac{4a}{3\pi}\big)$ (Stewart's Example 8.3.4, [[§63 Moments and Centers of Mass#^ex-63-2|Example §63.2]]); here the density grows toward the rim and the center of mass is higher.
>
> *Stewart: Example 15.4.3*

^ex-118-2

![[m233-101-1.svg]]
*[[§118 Applications of Double Integrals#^ex-118-2|Example §118.2]]. The shading shows the density $\rho = Kr$, heavier toward the rim. The center of mass $(0, 3a/(2\pi)) \approx (0, 0.48a)$ (red) lies above the centroid $(0, 4a/(3\pi)) \approx (0, 0.42a)$ (gray) of the same semicircle with uniform density.*

## Moment of Inertia

The **moment of inertia** (or **second moment**) of a particle of mass $m$ about an axis is $mr^2$, where $r$ is its distance from the axis. Approximating each $R_{ij}$ by a particle and passing to the limit gives the following.

> [!definition] Definition §118.6: Moments of Inertia
> The **moment of inertia** of the lamina **about the $x$-axis**, **about the $y$-axis**, and **about the origin** (the **polar moment of inertia**) are
>
> $$
> I_x = \lim_{m, n \to \infty} \sum_{i=1}^m \sum_{j=1}^n (y_{ij}^*)^2 \rho(x_{ij}^*, y_{ij}^*)\,\Delta A = \iint_D y^2\rho(x, y)\,dA , \qquad (6)
> $$
>
> $$
> I_y = \lim_{m, n \to \infty} \sum_{i=1}^m \sum_{j=1}^n (x_{ij}^*)^2 \rho(x_{ij}^*, y_{ij}^*)\,\Delta A = \iint_D x^2\rho(x, y)\,dA , \qquad (7)
> $$
>
> $$
> I_0 = \lim_{m, n \to \infty} \sum_{i=1}^m \sum_{j=1}^n \big[ (x_{ij}^*)^2 + (y_{ij}^*)^2 \big] \rho(x_{ij}^*, y_{ij}^*)\,\Delta A = \iint_D (x^2 + y^2)\rho(x, y)\,dA . \qquad (8)
> $$
>
> *Stewart: 15.4, Equations 6, 7 and 8*

^def-118-6

> [!theorem] Proposition §141.1: Polar Moment of Inertia
> $I_0 = I_x + I_y$.
>
> *Stewart: 15.4 (text)*

^prop-118-1

> [!proof]+ Proof
> By Property 5 of double integrals ([[§116 Double Integrals Over General Regions#^thm-116-3|Theorem §116.3]]), $I_0 = \iint_D (x^2 + y^2)\rho\,dA = \iint_D y^2\rho\,dA + \iint_D x^2\rho\,dA = I_x + I_y$.

^pf-118-1

*Uses:* [[§118 Applications of Double Integrals#^def-118-6|Def. §118.6]], [[§116 Double Integrals Over General Regions#^thm-116-3|§116.3]]

The moment of inertia plays the same role in rotational motion that mass plays in linear motion: the moment of inertia of a wheel is what makes it hard to start or stop its rotation, just as the mass of a car is what makes it hard to start or stop its motion.

> [!definition] Definition §118.7: Radius of Gyration
> The **radius of gyration of a lamina about an axis** is the number $R$ such that
>
> $$
> mR^2 = I , \qquad (9)
> $$
>
> where $m$ is the mass of the lamina and $I$ its moment of inertia about the axis: if all the mass were concentrated at distance $R$ from the axis, this "point mass" would have the same moment of inertia. In particular, the radius of gyration $\bar{\bar y}$ with respect to the $x$-axis and $\bar{\bar x}$ with respect to the $y$-axis are given by
>
> $$
> m\bar{\bar y}^{\,2} = I_x , \qquad m\bar{\bar x}^{\,2} = I_y . \qquad (10)
> $$
>
> So $(\bar{\bar x}, \bar{\bar y})$ is the point at which the mass can be concentrated without changing the moments of inertia about the coordinate axes (compare the center of mass, which preserves the first moments).
>
> *Stewart: 15.4, Equations 9 and 10*

^def-118-7

> [!example] Example §141.3: A Homogeneous Disk
> Find the moments of inertia $I_x$, $I_y$, $I_0$ of a homogeneous disk $D$ with density $\rho(x, y) = \rho$, center the origin and radius $a$, and its radius of gyration about the $x$-axis.
>
> In polar coordinates $D$ is $0 \le \theta \le 2\pi$, $0 \le r \le a$. By Formula 6,
>
> $$
> I_x = \iint_D y^2\rho\,dA = \rho\int_0^{2\pi} \int_0^a (r\sin\theta)^2 r\,dr\,d\theta = \rho\int_0^{2\pi} \tfrac12 (1 - \cos 2\theta)\,d\theta \int_0^a r^3\,dr = \frac{\rho}{2} \Big[ \theta - \tfrac12 \sin 2\theta \Big]_0^{2\pi} \Big[ \frac{r^4}{4} \Big]_0^a = \frac{\pi\rho a^4}{4} .
> $$
>
> Similarly (as expected from the symmetry) $I_y = \rho\int_0^{2\pi} \frac12(1 + \cos 2\theta)\,d\theta \int_0^a r^3\,dr = \frac{\pi\rho a^4}{4}$, and by [[§118 Applications of Double Integrals#^prop-118-1|Proposition §118.1]]
>
> $$
> I_0 = I_x + I_y = \frac{\pi\rho a^4}{2} .
> $$
>
> The mass of the disk is $m = \rho(\pi a^2)$, so $I_0 = \frac12 (\rho\pi a^2) a^2 = \frac12 ma^2$: a wheel is harder to spin up the heavier it is and, more strongly, the larger its radius.
>
> **Radius of gyration.** By Equation 10,
>
> $$
> \bar{\bar y}^{\,2} = \frac{I_x}{m} = \frac{\frac14 \pi\rho a^4}{\rho\pi a^2} = \frac{a^2}{4} ,
> $$
>
> so the radius of gyration about the $x$-axis is $\bar{\bar y} = \frac12 a$, half the radius of the disk.
>
> *Stewart: Examples 15.4.4 and 15.4.5*

^ex-118-3

## Probability

A probability density function $f$ of one continuous random variable $X$ satisfies $f \ge 0$, $\int_{-\infty}^{\infty} f(x)\,dx = 1$, and $P(a \le X \le b) = \int_a^b f(x)\,dx$ ([[§65 Probability#^def-65-2|Definition §65.2]]). For two random variables, such as the lifetimes of two components of a machine, or the height and weight of a person chosen at random, the density is a function of two variables.

> [!definition] Definition §118.8: Joint Density Function
> The **joint density function** of two continuous random variables $X$ and $Y$ is a function $f$ of two variables such that the probability that $(X, Y)$ lies in a region $D$ is
>
> $$
> P\big((X, Y) \in D\big) = \iint_D f(x, y)\,dA .
> $$
>
> In particular, for a rectangle, $P(a \le X \le b,\ c \le Y \le d) = \int_a^b \int_c^d f(x, y)\,dy\,dx$, the volume above the rectangle and below the graph of $f$. Because probabilities are nonnegative and measured on a scale from $0$ to $1$, a joint density function satisfies
>
> $$
> f(x, y) \ge 0 , \qquad \iint_{\mathbb{R}^2} f(x, y)\,dA = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y)\,dx\,dy = 1 ,
> $$
>
> where the integral over $\mathbb{R}^2$ is an improper integral, the limit of the integrals over expanding disks or squares (as in Stewart's Exercise 15.3.50; compare [[§58 Improper Integrals#^def-58-1|Definition §58.1]]).
>
> *Stewart: 15.4 (text)*

^def-118-8

> [!remark]- Connections
> - For $f \ge 0$ the improper integral over $\mathbb{R}^2$ may always be computed as an iterated integral in either order, with the same (possibly infinite) value: this is Tonelli's Theorem, [[§25 Invariance Properties and Fubini's Theorem#^thm-25-3|551 Thm. §25.3]]. It is what justifies writing $\iint_{\mathbb{R}^2} f\,dA = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f\,dx\,dy$ above and in [[§118 Applications of Double Integrals#^ex-118-4|Examples §118.4]] and [[§118 Applications of Double Integrals#^ex-118-5|§118.5]].

> [!example] Example §141.4: Normalizing a Joint Density
> If the joint density function for $X$ and $Y$ is
>
> $$
> f(x, y) = \begin{cases} C(x + 2y) & \text{if } 0 \le x \le 10,\ 0 \le y \le 10 \\ 0 & \text{otherwise,} \end{cases}
> $$
>
> find the value of the constant $C$. Then find $P(X \le 7,\ Y \ge 2)$.
>
> **The constant.** $f = 0$ outside $[0, 10] \times [0, 10]$, so
>
> $$
> \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y)\,dy\,dx = \int_0^{10} \int_0^{10} C(x + 2y)\,dy\,dx = C\int_0^{10} \Big[ xy + y^2 \Big]_{y=0}^{y=10} dx = C\int_0^{10} (10x + 100)\,dx = 1500C .
> $$
>
> This must equal $1$, so $C = \frac{1}{1500}$.
>
> **The probability.** Since $f = 0$ for $x < 0$ and $y > 10$,
>
> $$
> P(X \le 7,\ Y \ge 2) = \int_{-\infty}^{7} \int_2^{\infty} f(x, y)\,dy\,dx = \int_0^7 \int_2^{10} \tfrac{1}{1500}(x + 2y)\,dy\,dx = \tfrac{1}{1500} \int_0^7 \Big[ xy + y^2 \Big]_{y=2}^{y=10} dx = \tfrac{1}{1500} \int_0^7 (8x + 96)\,dx = \frac{868}{1500} \approx 0.5787 .
> $$
>
> *Stewart: Example 15.4.6*

^ex-118-4

> [!definition] Definition §118.9: Independent Random Variables
> Let $X$ be a random variable with probability density function $f_1(x)$ and $Y$ a random variable with density function $f_2(y)$. Then $X$ and $Y$ are **independent random variables** if their joint density function is the product of their individual density functions:
>
> $$
> f(x, y) = f_1(x)\,f_2(y) .
> $$
>
> *Stewart: 15.4 (text)*

^def-118-9

> [!example] Example §118.5: Two Independent Waiting Times
> The manager of a movie theater determines that the average time moviegoers wait in line to buy a ticket is $10$ minutes and the average time they wait to buy popcorn is $5$ minutes. Assuming that the waiting times are independent, find the probability that a moviegoer waits a total of less than $20$ minutes before taking his or her seat.
>
> Model the waiting times $X$ (ticket) and $Y$ (popcorn) by exponential density functions with means $\mu = 10$ and $\mu = 5$ ([[§65 Probability#^def-65-3|Definition §65.3]] with $c = 1/\mu$, which has mean $\mu$ by [[§65 Probability#^ex-65-3|Example §65.3]]: $f(t) = \mu^{-1}e^{-t/\mu}$ for $t \ge 0$, $0$ for $t < 0$):
>
> $$
> f_1(x) = \begin{cases} 0 & x < 0 \\ \frac{1}{10}e^{-x/10} & x \ge 0 \end{cases} \qquad
> f_2(y) = \begin{cases} 0 & y < 0 \\ \frac15 e^{-y/5} & y \ge 0 . \end{cases}
> $$
>
> By independence the joint density is $f(x, y) = f_1(x)f_2(y) = \frac{1}{50}e^{-x/10}e^{-y/5}$ for $x, y \ge 0$, and $0$ otherwise. The event $X + Y < 20$ is $(X, Y) \in D$, where $D$ is the triangle $0 \le x \le 20$, $0 \le y \le 20 - x$. So
>
> $$
> \begin{aligned}
> P(X + Y < 20) &= \iint_D f(x, y)\,dA = \int_0^{20} \int_0^{20 - x} \tfrac{1}{50}e^{-x/10}e^{-y/5}\,dy\,dx = \tfrac{1}{50} \int_0^{20} \Big[ e^{-x/10}(-5)e^{-y/5} \Big]_{y=0}^{y=20-x} dx \\
> &= \tfrac{1}{10} \int_0^{20} e^{-x/10}\big( 1 - e^{(x - 20)/5} \big)\,dx = \tfrac{1}{10} \int_0^{20} \big( e^{-x/10} - e^{-4}e^{x/10} \big)\,dx \\
> &= \Big[ -e^{-x/10} - e^{-4}e^{x/10} \Big]_0^{20} = \big( -e^{-2} - e^{-2} \big) - \big( -1 - e^{-4} \big) = 1 + e^{-4} - 2e^{-2} \approx 0.7476 .
> \end{aligned}
> $$
>
> About $75\%$ of the moviegoers wait less than $20$ minutes before taking their seats.
>
> *Stewart: Example 15.4.7*

^ex-118-5

## Expected Values

> [!definition] Definition §118.10: Expected Values
> If $X$ and $Y$ are random variables with joint density function $f$, the **$X$-mean** and **$Y$-mean**, also called the **expected values** of $X$ and $Y$, are
>
> $$
> \mu_1 = \iint_{\mathbb{R}^2} x f(x, y)\,dA , \qquad \mu_2 = \iint_{\mathbb{R}^2} y f(x, y)\,dA . \qquad (11)
> $$
>
> This extends the mean $\mu = \int_{-\infty}^{\infty} x f(x)\,dx$ of one random variable ([[§65 Probability#^def-65-4|Definition §65.4]]).
>
> *Stewart: 15.4, Equation 11*

^def-118-10

> [!remark] Remark: Probability as Mass
> The formulas for $\mu_1$, $\mu_2$ are those for the moments $M_y$, $M_x$ of a lamina with density $\rho = f$ (Equations 3 and 4). Probability is computed the way mass is, by integrating a density, and the total "probability mass" is $1$. So by Equation 5 the expected values $(\mu_1, \mu_2)$ are the coordinates of the "center of mass" of the probability distribution.
>
> Stewart's Example 15.4.8 uses independent normal distributions $f_i(t) = \frac{1}{\sigma\sqrt{2\pi}}e^{-(t - \mu)^2/(2\sigma^2)}$: roller bearings with diameters $X$ (mean $4.0$ cm) and lengths $Y$ (mean $6.0$ cm), both with standard deviation $0.01$ cm, have joint density $f(x, y) = \frac{5000}{\pi}e^{-5000[(x - 4)^2 + (y - 6)^2]}$. A numerical integration gives $P(3.98 < X < 4.02,\ 5.98 < Y < 6.02) \approx 0.91$, so about $9\%$ of the bearings differ from the specifications by more than $0.02$ cm in diameter or length.

^rem-118-1
