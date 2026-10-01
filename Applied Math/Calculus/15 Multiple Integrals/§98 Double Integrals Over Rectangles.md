---
type: section
subject: "[[Calculus]]"
chapter: 15
section: 98
stewart: "15.1"
aliases: ["Stewart 15.1"]
tags: [calculus, math233]
---
← [[§97 Lagrange Multipliers]] · ↑ [[· 15 Multiple Integrals]] · [[§99 Double Integrals Over General Regions]] →

*Stewart, Section 15.1 · MATH 233 (UMass, Spring 2023): Exam 2 Practice Questions (Q8).*

The volume under the graph of $f(x, y)$ over a rectangle is approximated by boxes, exactly as the area under $y = f(x)$ was approximated by rectangles, and the limit of these double Riemann sums is the double integral. Computing it from the definition is hopeless except in a few cases. Fubini's Theorem gives the practical method: a double integral of a continuous function is an iterated integral, two single integrals done one after the other, in either order. The section also gives the Midpoint Rule for estimating double integrals and the average value of a function of two variables.

## Review of the Definite Integral

For $f$ defined on $[a, b]$, divide $[a, b]$ into $n$ subintervals $[x_{i-1}, x_i]$ of equal width $\Delta x = (b - a)/n$, choose sample points $x_i^*$ in them and form the Riemann sum $\sum_{i=1}^n f(x_i^*)\,\Delta x$. Its limit as $n \to \infty$ is the definite integral ([[§35 The Definite Integral|§35]]):

$$
\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^n f(x_i^*)\,\Delta x \qquad\text{(Stewart 15.1, Equations 1 and 2).}
$$

When $f \ge 0$, the Riemann sum is the total area of the approximating rectangles and the integral is the area under the curve. Everything in this section is the same construction one dimension up.

## Volumes and Double Integrals

Let $f$ be defined on the closed rectangle

$$
R = [a, b] \times [c, d] = \{(x, y) \in \mathbb{R}^2 \mid a \le x \le b,\ c \le y \le d\},
$$

and suppose first that $f(x, y) \ge 0$. Let $S = \{(x, y, z) \in \mathbb{R}^3 \mid 0 \le z \le f(x, y),\ (x, y) \in R\}$ be the solid that lies above $R$ and under the graph of $f$.

> [!definition] Definition §98.1: Subrectangles, Sample Points and the Volume Under a Graph
> Divide $[a, b]$ into $m$ subintervals $[x_{i-1}, x_i]$ of equal width $\Delta x = (b - a)/m$ and $[c, d]$ into $n$ subintervals $[y_{j-1}, y_j]$ of equal width $\Delta y = (d - c)/n$. The lines parallel to the axes through the endpoints cut $R$ into the $mn$ **subrectangles**
>
> $$
> R_{ij} = [x_{i-1}, x_i] \times [y_{j-1}, y_j] = \{(x, y) \mid x_{i-1} \le x \le x_i,\ y_{j-1} \le y \le y_j\},
> $$
>
> each of area $\Delta A = \Delta x\,\Delta y$. Choose a **sample point** $(x_{ij}^*, y_{ij}^*)$ in each $R_{ij}$. The thin box with base $R_{ij}$ and height $f(x_{ij}^*, y_{ij}^*)$ has volume $f(x_{ij}^*, y_{ij}^*)\,\Delta A$, and the sum of these volumes approximates the volume of $S$:
>
> $$
> V \approx \sum_{i=1}^m \sum_{j=1}^n f(x_{ij}^*, y_{ij}^*)\,\Delta A . \qquad (3)
> $$
>
> The **volume** of the solid $S$ under the graph of $f \ge 0$ and above $R$ is defined to be
>
> $$
> V = \lim_{m, n \to \infty} \sum_{i=1}^m \sum_{j=1}^n f(x_{ij}^*, y_{ij}^*)\,\Delta A . \qquad (4)
> $$
>
> The double limit means that the double sum can be made as close as we like to $V$, for any choice of the sample points, by taking $m$ and $n$ sufficiently large. (This definition agrees with the volume by cross-sections of [[§40 Volumes|§40]].)
>
> *Stewart: 15.1, Equations 3 and 4*

^def-98-1

The same limits occur for functions that are not positive (mass, charge, probability; [[§101 Applications of Double Integrals|§101]]), so they get a name of their own.

> [!definition] Definition §98.2: The Double Integral
> The **double integral** of $f$ over the rectangle $R$ is
>
> $$
> \iint_R f(x, y)\,dA = \lim_{m, n \to \infty} \sum_{i=1}^m \sum_{j=1}^n f(x_{ij}^*, y_{ij}^*)\,\Delta A
> $$
>
> if this limit exists. Precisely: for every $\varepsilon > 0$ there is an integer $N$ such that
>
> $$
> \left| \iint_R f(x, y)\,dA - \sum_{i=1}^m \sum_{j=1}^n f(x_{ij}^*, y_{ij}^*)\,\Delta A \right| < \varepsilon
> $$
>
> for all integers $m, n > N$ and every choice of sample points $(x_{ij}^*, y_{ij}^*)$ in $R_{ij}$. The function $f$ is **integrable** over $R$ if the limit exists, and the sum is a **double Riemann sum**.
>
> Since any sample points may be used, choosing the upper right-hand corner $(x_i, y_j)$ of each $R_{ij}$ gives, for integrable $f$,
>
> $$
> \iint_R f(x, y)\,dA = \lim_{m, n \to \infty} \sum_{i=1}^m \sum_{j=1}^n f(x_i, y_j)\,\Delta A . \qquad (6)
> $$
>
> *Stewart: 15.1, Definition 5 and Equation 6*

^def-98-2

> [!remark]- Connections
> - Rigorous treatment with arbitrary partitions and Darboux sums: [[§15 Multivariable Integration#^def-15-10|452 Def. §15.10]], [[§15 Multivariable Integration#^def-15-11|452 Def. §15.11]]; that every choice of sample points gives the same limit is [[§15 Multivariable Integration#^rem-15-6|452 Remark (Evaluating the Integral)]].
> - The volume interpretation in measure theory: for $f \ge 0$ the Lebesgue measure of the region under the graph equals $\int f$, [[§17 Invariance Properties and Fubini's Theorem#^thm-17-11|551 Thm. §17.11]] (the Subgraph Theorem).

> [!remark] Remark: Equal Subrectangles
> Stewart divides $R$ into subrectangles of equal size. Unequal subrectangles $R_{ij}$ would also do, provided all their dimensions tend to $0$ in the limit.

^rem-98-1

> [!theorem] Theorem §98.1: Integrable Functions
> Every continuous function on $R$ is integrable over $R$. More generally, if $f$ is bounded on $R$ (there is a constant $M$ with $|f(x, y)| \le M$ for all $(x, y) \in R$) and $f$ is continuous on $R$ except possibly on a finite number of smooth curves, then $f$ is integrable over $R$.
>
> *Stewart: 15.1 (text)*

^thm-98-1

*Stewart omits the proof ("shown in courses on advanced calculus"). For continuous $f$, the one-variable proof from uniform continuity ([[§8 Motivation꞉ The Riemann Integral#^prop-8-1|551 Prop. §8.1]]) carries over word for word to a rectangle; the two-variable theory, including integration over sets bounded by curves, is [[§15 Multivariable Integration|452 §15]].*

> [!theorem] Theorem §98.2: Volume as a Double Integral
> If $f(x, y) \ge 0$, then the volume $V$ of the solid that lies above the rectangle $R$ and below the surface $z = f(x, y)$ is
>
> $$
> V = \iint_R f(x, y)\,dA .
> $$
>
> *Stewart: 15.1 (boxed formula after Equation 6)*

^thm-98-2

> [!proof]+ Proof
> The right-hand sides of Equation 4 in [[§98 Double Integrals Over Rectangles#^def-98-1|Definition §98.1]] and of [[§98 Double Integrals Over Rectangles#^def-98-2|Definition §98.2]] are the same limit of the same double Riemann sums.

^pf-98-2

*Uses:* [[§98 Double Integrals Over Rectangles#^def-98-1|Def. §98.1]], [[§98 Double Integrals Over Rectangles#^def-98-2|Def. §98.2]]

> [!example] Example §98.1: Estimating a Volume with a Riemann Sum
> Estimate the volume of the solid that lies above the square $R = [0, 2] \times [0, 2]$ and below the elliptic paraboloid $z = 16 - x^2 - 2y^2$. Divide $R$ into four equal squares and use the upper right corner of each square $R_{ij}$ as sample point.
>
> The squares are $R_{11} = [0,1]\times[0,1]$, $R_{12} = [0,1]\times[1,2]$, $R_{21} = [1,2]\times[0,1]$ and $R_{22} = [1,2]\times[1,2]$, each of area $\Delta A = 1$, with upper right corners $(1,1)$, $(1,2)$, $(2,1)$, $(2,2)$. With $f(x, y) = 16 - x^2 - 2y^2$ and $m = n = 2$,
>
> $$
> \begin{aligned}
> V &\approx \sum_{i=1}^2 \sum_{j=1}^2 f(x_i, y_j)\,\Delta A = f(1,1)\,\Delta A + f(1,2)\,\Delta A + f(2,1)\,\Delta A + f(2,2)\,\Delta A \\
> &= 13(1) + 7(1) + 10(1) + 4(1) = 34 .
> \end{aligned}
> $$
>
> This is the total volume of the four boxes in the figure below. With $16$, $64$ and $256$ squares the estimates improve to about $41.5$, $44.875$ and $46.46875$. The exact volume is $48$ ([[§98 Double Integrals Over Rectangles#^ex-98-5|Example §98.5]]). The upper right corners are where $f$ is smallest on each square (it decreases in both $x$ and $y$ there), so these sums underestimate.
>
> *Stewart: Example 15.1.1*

^ex-98-1

![[m233-98-1.svg]]
*The Riemann sum of Example §98.1. Each box stands on one square $R_{ij}$ and reaches up to the surface $z = 16 - x^2 - 2y^2$ (blue edges) at the upper right corner of its base (red dots): heights $13, 7, 10, 4$. Since $f$ decreases in $x$ and in $y$, the corner $(x_i, y_j)$ is the lowest point of the surface over $R_{ij}$, so every box lies under the surface and $34$ underestimates the volume $48$.*

> [!example] Example §98.2: A Double Integral Read as a Volume
> If $R = \{(x, y) \mid -1 \le x \le 1,\ -2 \le y \le 2\}$, evaluate $\displaystyle\iint_R \sqrt{1 - x^2}\,dA$.
>
> Evaluating from Definition §98.2 would be very hard. But $\sqrt{1 - x^2} \ge 0$, so by Theorem §98.2 the integral is a volume. If $z = \sqrt{1 - x^2}$, then $x^2 + z^2 = 1$ and $z \ge 0$: the integral is the volume of the solid $S$ under the circular cylinder $x^2 + z^2 = 1$ and above $R$. Its cross-sections perpendicular to the $y$-axis are half-disks of radius $1$, and $S$ has length $4$, so
>
> $$
> \iint_R \sqrt{1 - x^2}\,dA = \tfrac12 \pi (1)^2 \times 4 = 2\pi .
> $$
>
> *Stewart: Example 15.1.2*

^ex-98-2

> [!example] Example §98.3: A Riemann Sum with Values of Both Signs
> Use upper right-hand Riemann sums with $9$ equally sized squares ($\Delta x = \Delta y = \pi/3$) to approximate $\displaystyle\iint_R \cos x \sin y\,dA$, where $R = \{(x, y) \mid -\tfrac{\pi}{2} \le x \le \tfrac{\pi}{2},\ 0 \le y \le \pi\}$.
>
> Here $m = n = 3$ and $\Delta A = \pi^2/9$. The right endpoints of the $x$-subintervals are $x_i = -\tfrac{\pi}{6}, \tfrac{\pi}{6}, \tfrac{\pi}{2}$ and the upper endpoints of the $y$-subintervals are $y_j = \tfrac{\pi}{3}, \tfrac{2\pi}{3}, \pi$. The integrand is a product, so the double sum factors:
>
> $$
> \sum_{i=1}^3 \sum_{j=1}^3 \cos x_i \sin y_j\,\Delta A = \Delta A \Big(\sum_{i=1}^3 \cos x_i\Big)\Big(\sum_{j=1}^3 \sin y_j\Big) = \frac{\pi^2}{9}\Big(\frac{\sqrt3}{2} + \frac{\sqrt3}{2} + 0\Big)\Big(\frac{\sqrt3}{2} + \frac{\sqrt3}{2} + 0\Big) = \frac{\pi^2}{9} \cdot 3 = \frac{\pi^2}{3} .
> $$
>
> For comparison, the exact value is $\int_{-\pi/2}^{\pi/2} \cos x\,dx \int_0^{\pi} \sin y\,dy = 2 \cdot 2 = 4$ ([[§98 Double Integrals Over Rectangles#^thm-98-4|Theorem §98.4]]), and $\pi^2/3 \approx 3.29$. The squares in the last column ($x_3 = \pi/2$) and top row ($y_3 = \pi$) contribute $0$, because $\cos x$ and $\sin y$ vanish at those corners.
>
> *Source: 233 Exam 2 Practice Questions, Q8*

^ex-98-3

## The Midpoint Rule

The approximation methods for single integrals (Midpoint, Trapezoidal and Simpson's Rules; [[§50 Approximate Integration|§50]]) all have double-integral versions. Stewart gives only the Midpoint Rule.

> [!definition] Definition §98.3: The Midpoint Rule for Double Integrals
> The **Midpoint Rule** approximates a double integral by the double Riemann sum whose sample point in $R_{ij}$ is its center $(\bar{x}_i, \bar{y}_j)$, where $\bar{x}_i$ is the midpoint of $[x_{i-1}, x_i]$ and $\bar{y}_j$ is the midpoint of $[y_{j-1}, y_j]$:
>
> $$
> \iint_R f(x, y)\,dA \approx \sum_{i=1}^m \sum_{j=1}^n f(\bar{x}_i, \bar{y}_j)\,\Delta A .
> $$
>
> *Stewart: 15.1, Midpoint Rule for Double Integrals*

^def-98-3

> [!example] Example §98.4: The Midpoint Rule
> Use the Midpoint Rule with $m = n = 2$ to estimate $\displaystyle\iint_R (x - 3y^2)\,dA$, where $R = \{(x, y) \mid 0 \le x \le 2,\ 1 \le y \le 2\}$.
>
> The centers of the four subrectangles have $\bar{x}_1 = \tfrac12$, $\bar{x}_2 = \tfrac32$, $\bar{y}_1 = \tfrac54$, $\bar{y}_2 = \tfrac74$, and each subrectangle has area $\Delta A = 1 \cdot \tfrac12 = \tfrac12$. With $f(x, y) = x - 3y^2$,
>
> $$
> f\big(\tfrac12, \tfrac54\big) = \tfrac{8}{16} - \tfrac{75}{16} = -\tfrac{67}{16}, \quad
> f\big(\tfrac12, \tfrac74\big) = \tfrac{8}{16} - \tfrac{147}{16} = -\tfrac{139}{16}, \quad
> f\big(\tfrac32, \tfrac54\big) = \tfrac{24}{16} - \tfrac{75}{16} = -\tfrac{51}{16}, \quad
> f\big(\tfrac32, \tfrac74\big) = \tfrac{24}{16} - \tfrac{147}{16} = -\tfrac{123}{16},
> $$
>
> so
>
> $$
> \iint_R (x - 3y^2)\,dA \approx \Big(-\tfrac{67}{16} - \tfrac{139}{16} - \tfrac{51}{16} - \tfrac{123}{16}\Big)\tfrac12 = -\tfrac{380}{32} = -\tfrac{95}{8} = -11.875 .
> $$
>
> Repeatedly dividing each subrectangle into four gives
>
> | subrectangles | 1 | 4 | 16 | 64 | 256 | 1024 |
> |---|---|---|---|---|---|---|
> | Midpoint Rule | $-11.5000$ | $-11.8750$ | $-11.9687$ | $-11.9922$ | $-11.9980$ | $-11.9995$ |
>
> approaching the exact value $-12$ ([[§98 Double Integrals Over Rectangles#^ex-98-5|Example §98.5]]). The integrand is negative on $R$, so the integral is not a volume: it is minus the volume between $R$ and the graph, which lies below $R$.
>
> *Stewart: Example 15.1.3*

^ex-98-4

## Iterated Integrals

Evaluating a double integral from its definition is even harder than for single integrals. Instead we integrate in one variable at a time.

> [!definition] Definition §98.4: Partial Integration and Iterated Integrals
> Let $f$ be integrable on $R = [a, b] \times [c, d]$. The notation $\int_c^d f(x, y)\,dy$ means that $x$ is held fixed and $f(x, y)$ is integrated with respect to $y$ from $y = c$ to $y = d$ (**partial integration with respect to $y$**). The result is a function of $x$,
>
> $$
> A(x) = \int_c^d f(x, y)\,dy ,
> $$
>
> and integrating it from $a$ to $b$ gives the **iterated integral**
>
> $$
> \int_a^b \int_c^d f(x, y)\,dy\,dx = \int_a^b \left[ \int_c^d f(x, y)\,dy \right] dx . \qquad (7), (8)
> $$
>
> Similarly, in
>
> $$
> \int_c^d \int_a^b f(x, y)\,dx\,dy = \int_c^d \left[ \int_a^b f(x, y)\,dx \right] dy \qquad (9)
> $$
>
> we first integrate with respect to $x$ (holding $y$ fixed) from $a$ to $b$, then the result with respect to $y$ from $c$ to $d$. In both cases we work *from the inside out*; the brackets are usually omitted.
>
> *Stewart: 15.1, Equations 7, 8 and 9*

^def-98-4

> [!theorem] Theorem §98.3: Fubini's Theorem
> If $f$ is continuous on the rectangle $R = \{(x, y) \mid a \le x \le b,\ c \le y \le d\}$, then
>
> $$
> \iint_R f(x, y)\,dA = \int_a^b \int_c^d f(x, y)\,dy\,dx = \int_c^d \int_a^b f(x, y)\,dx\,dy .
> $$
>
> More generally, this is true if $f$ is bounded on $R$, $f$ is discontinuous only on a finite number of smooth curves, and the iterated integrals exist.
>
> *Stewart: 15.1, Theorem 10 (Fubini's Theorem)*

^thm-98-3

*Stewart omits the proof ("too difficult to include in this book"); it is proved in [[§15 Multivariable Integration#^thm-15-8|452 Thm. §15.8]]. Guido Fubini proved a very general version in 1907; the version for continuous functions was known to Cauchy almost a century earlier.*

> [!remark] Remark: Why It Works
> Stewart's intuitive argument, for $f(x, y) \ge 0$. By Theorem §98.2, $\iint_R f(x, y)\,dA$ is the volume $V$ of the solid $S$ above $R$ and under $z = f(x, y)$. By the volume formula of [[§40 Volumes|§40]], $V = \int_a^b A(x)\,dx$, where $A(x)$ is the area of the cross-section of $S$ in the plane through $x$ perpendicular to the $x$-axis. That cross-section is the region under the curve $z = f(x, y)$, $c \le y \le d$, with $x$ held constant, so $A(x) = \int_c^d f(x, y)\,dy$ and
>
> $$
> \iint_R f(x, y)\,dA = V = \int_a^b A(x)\,dx = \int_a^b \int_c^d f(x, y)\,dy\,dx .
> $$
>
> Slicing perpendicular to the $y$-axis instead gives $\iint_R f(x, y)\,dA = \int_c^d \int_a^b f(x, y)\,dx\,dy$. So the order of integration does not matter, much as the order of differentiation does not matter in Clairaut's Theorem ([[§92 Partial Derivatives|§92]]).

^rem-98-2

![[m233-98-2.svg]]
*Fubini's Theorem as slicing. The plane through $x$ perpendicular to the $x$-axis cuts the solid under $z = f(x, y)$ in a region (red) of area $A(x) = \int_c^d f(x, y)\,dy$: the inner integral. Stacking these slices from $x = a$ to $x = b$ is the outer integral $\int_a^b A(x)\,dx$, the volume.*

> [!remark]- Connections
> - Rigorous treatment: [[§15 Multivariable Integration#^thm-15-8|452 Thm. §15.8]] (continuous $f$ on a rectangle). Hub: [[Fubini's Theorem]]. The Lebesgue versions, for $f \ge 0$ measurable and for integrable $f$ on $\mathbb{R}^p \times \mathbb{R}^q$: [[§17 Invariance Properties and Fubini's Theorem#^thm-17-3|551 Thm. §17.3]] (Tonelli), [[§17 Invariance Properties and Fubini's Theorem#^thm-17-6|551 Thm. §17.6]] (Fubini).
> - Some hypothesis is needed: for $f = (x^2 - y^2)/(x^2 + y^2)^2$, unbounded near a corner of $[0,1]^2$, the two iterated integrals are $\pi/4$ and $-\pi/4$ ([[§15 Multivariable Integration#^ex-15-2|452 Ex. §15.2]]); Stewart's Exercise 15.1.57 is a similar example.

> [!example] Example §98.5: Fubini's Theorem in Both Orders
> **(a)** Evaluate $\displaystyle\iint_R (x - 3y^2)\,dA$, where $R = \{(x, y) \mid 0 \le x \le 2,\ 1 \le y \le 2\}$ (compare [[§98 Double Integrals Over Rectangles#^ex-98-4|Example §98.4]]).
>
> Integrating first with respect to $y$:
>
> $$
> \iint_R (x - 3y^2)\,dA = \int_0^2 \int_1^2 (x - 3y^2)\,dy\,dx = \int_0^2 \Big[ xy - y^3 \Big]_{y=1}^{y=2} dx = \int_0^2 (x - 7)\,dx = \Big[ \frac{x^2}{2} - 7x \Big]_0^2 = -12 .
> $$
>
> Integrating first with respect to $x$:
>
> $$
> \iint_R (x - 3y^2)\,dA = \int_1^2 \int_0^2 (x - 3y^2)\,dx\,dy = \int_1^2 \Big[ \frac{x^2}{2} - 3xy^2 \Big]_{x=0}^{x=2} dy = \int_1^2 (2 - 6y^2)\,dy = \Big[ 2y - 2y^3 \Big]_1^2 = -12 .
> $$
>
> The answer is negative because $f$ is negative on $R$: the integral is the negative of the volume that lies above the graph of $f$ and below $R$.
>
> **(b)** Find the volume of the solid $S$ bounded by the elliptic paraboloid $x^2 + 2y^2 + z = 16$, the planes $x = 2$ and $y = 2$, and the three coordinate planes (the solid of [[§98 Double Integrals Over Rectangles#^ex-98-1|Example §98.1]]).
>
> $S$ lies under the surface $z = 16 - x^2 - 2y^2$ and above $R = [0, 2] \times [0, 2]$, so by Theorem §98.2 and Fubini's Theorem
>
> $$
> \begin{aligned}
> V &= \iint_R (16 - x^2 - 2y^2)\,dA = \int_0^2 \int_0^2 (16 - x^2 - 2y^2)\,dx\,dy = \int_0^2 \Big[ 16x - \tfrac13 x^3 - 2y^2 x \Big]_{x=0}^{x=2} dy \\
> &= \int_0^2 \Big( \tfrac{88}{3} - 4y^2 \Big)\,dy = \Big[ \tfrac{88}{3} y - \tfrac43 y^3 \Big]_0^2 = \tfrac{176}{3} - \tfrac{32}{3} = 48 .
> \end{aligned}
> $$
>
> *Stewart: Examples 15.1.5 and 15.1.7*

^ex-98-5

> [!example] Example §98.6: Choosing the Order of Integration
> Evaluate $\displaystyle\iint_R y \sin(xy)\,dA$, where $R = [1, 2] \times [0, \pi]$.
>
> Integrate first with respect to $x$. For fixed $y$, an antiderivative of $y\sin(xy)$ in $x$ is $-\cos(xy)$, so
>
> $$
> \iint_R y \sin(xy)\,dA = \int_0^{\pi} \int_1^2 y \sin(xy)\,dx\,dy = \int_0^{\pi} \Big[ -\cos(xy) \Big]_{x=1}^{x=2} dy = \int_0^{\pi} (-\cos 2y + \cos y)\,dy = \Big[ -\tfrac12 \sin 2y + \sin y \Big]_0^{\pi} = 0 .
> $$
>
> In the other order, $\int_1^2 \int_0^{\pi} y \sin(xy)\,dy\,dx$, the inner integral needs integration by parts, and the outer one then needs it again. When evaluating double integrals it is wise to choose the order that gives simpler integrals.
>
> The value $0$ means that the volume $V_1$ above $R$ and below the graph equals the volume $V_2$ below $R$ and above the graph: for a function of both signs, $\iint_R f\,dA = V_1 - V_2$.
>
> *Stewart: Example 15.1.6*

^ex-98-6

> [!theorem] Theorem §98.4: Integrals of Products
> If $g$ is continuous on $[a, b]$ and $h$ is continuous on $[c, d]$, then
>
> $$
> \iint_R g(x)\,h(y)\,dA = \int_a^b g(x)\,dx \int_c^d h(y)\,dy \qquad\text{where } R = [a, b] \times [c, d] .
> $$
>
> *Stewart: 15.1, Equation 11*

^thm-98-4

> [!proof]+ Proof
> The function $f(x, y) = g(x)h(y)$ is continuous on $R$, so Fubini's Theorem gives
>
> $$
> \iint_R f(x, y)\,dA = \int_c^d \int_a^b g(x)\,h(y)\,dx\,dy = \int_c^d \left[ \int_a^b g(x)\,h(y)\,dx \right] dy .
> $$
>
> In the inner integral $y$ is a constant, so $h(y)$ is a constant and comes out of the integral:
>
> $$
> \int_c^d \left[ h(y) \left( \int_a^b g(x)\,dx \right) \right] dy = \int_a^b g(x)\,dx \int_c^d h(y)\,dy ,
> $$
>
> since $\int_a^b g(x)\,dx$ is a constant and comes out of the outer integral.

^pf-98-4

*Uses:* [[§98 Double Integrals Over Rectangles#^thm-98-3|§98.3]], [[§35 The Definite Integral|§35]] (constant multiple property)

For example (Stewart's Example 15.1.8), on $R = [0, \pi/2] \times [0, \pi/2]$,

$$
\iint_R \sin x \cos y\,dA = \int_0^{\pi/2} \sin x\,dx \int_0^{\pi/2} \cos y\,dy = \Big[-\cos x\Big]_0^{\pi/2} \Big[\sin y\Big]_0^{\pi/2} = 1 \cdot 1 = 1 ,
$$

the volume of the solid above $R$ and below the graph of $\sin x \cos y$, which is positive on $R$.

## Average Value

> [!definition] Definition §98.5: Average Value
> The **average value** of a function $f$ of two variables defined on a rectangle $R$ is
>
> $$
> f_{\text{avg}} = \frac{1}{A(R)} \iint_R f(x, y)\,dA ,
> $$
>
> where $A(R)$ is the area of $R$. This is the analogue of $f_{\text{avg}} = \frac{1}{b - a}\int_a^b f(x)\,dx$ ([[§43 Average Value of a Function|§43]]).
>
> *Stewart: 15.1 (text)*

^def-98-5

> [!remark] Remark: Leveling the Mountains
> If $f(x, y) \ge 0$, the equation
>
> $$
> A(R) \times f_{\text{avg}} = \iint_R f(x, y)\,dA
> $$
>
> says that the box with base $R$ and height $f_{\text{avg}}$ has the same volume as the solid under the graph of $f$. If $z = f(x, y)$ describes a mountainous region and the tops of the mountains are chopped off at height $f_{\text{avg}}$, they exactly fill the valleys, leaving the region flat. In practice $f_{\text{avg}}$ is estimated with the Midpoint Rule: Stewart's Example 15.1.9 reads the snowfall at the centers of $16$ subrectangles of Colorado off a contour map and finds an average of about $13$ inches.

^rem-98-3
