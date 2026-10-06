---
type: section
subject: "[[Calculus]]"
chapter: 15
section: 117
stewart: "15.3"
aliases: ["Stewart 15.3"]
tags: [calculus, math233]
---
← [[§116 Double Integrals Over General Regions]] · ↑ [[· 15 Multiple Integrals]] · [[§118 Applications of Double Integrals]] →

*Stewart, Section 15.3 · MATH 233 (UMass, Spring 2023): Chapter 15 Review (Q3, Q5), Exam 2 Practice Questions (Q14).*

Disks, annuli, sectors and regions bounded by polar curves are awkward to describe in rectangular coordinates but simple in polar coordinates. This section shows how to convert a double integral: write $x = r\cos\theta$, $y = r\sin\theta$, use limits for $r$ and $\theta$, and replace $dA$ by $r\,dr\,d\theta$. The extra factor $r$ is the area scale: a small polar rectangle with sides $\Delta r$ and $\Delta\theta$ has area about $r\,\Delta r\,\Delta\theta$, not $\Delta r\,\Delta\theta$. Integrands involving $x^2 + y^2$ usually become easier as well.

## Review of Polar Coordinates

The polar coordinates $(r, \theta)$ of a point are related to its rectangular coordinates $(x, y)$ by

$$
r^2 = x^2 + y^2, \qquad x = r\cos\theta, \qquad y = r\sin\theta
$$

([[§75 Polar Coordinates#^thm-75-2|Theorem §75.2]]). Circles centered at the origin are especially simple: the disk $x^2 + y^2 \le 1$ is $\{(r, \theta) \mid 0 \le r \le 1,\ 0 \le \theta \le 2\pi\}$, and the upper half-annulus between the circles $x^2 + y^2 = 1$ and $x^2 + y^2 = 4$ is $\{(r, \theta) \mid 1 \le r \le 2,\ 0 \le \theta \le \pi\}$. Table 10.3.1 of Stewart lists other curves that are simple in polar coordinates.

## Double Integrals in Polar Coordinates

> [!definition] Definition §117.1: Polar Rectangle
> A **polar rectangle** is a region of the form
>
> $$
> R = \{(r, \theta) \mid a \le r \le b,\ \alpha \le \theta \le \beta\} .
> $$
>
> Dividing $[a, b]$ into $m$ subintervals $[r_{i-1}, r_i]$ of equal width $\Delta r = (b - a)/m$ and $[\alpha, \beta]$ into $n$ subintervals $[\theta_{j-1}, \theta_j]$ of equal width $\Delta\theta = (\beta - \alpha)/n$, the circles $r = r_i$ and the rays $\theta = \theta_j$ cut $R$ into the **polar subrectangles**
>
> $$
> R_{ij} = \{(r, \theta) \mid r_{i-1} \le r \le r_i,\ \theta_{j-1} \le \theta \le \theta_j\} ,
> $$
>
> whose "center" has polar coordinates $r_i^* = \tfrac12 (r_{i-1} + r_i)$, $\theta_j^* = \tfrac12 (\theta_{j-1} + \theta_j)$.
>
> *Stewart: 15.3 (text)*

^def-117-1

> [!theorem] Theorem §117.1: Change to Polar Coordinates in a Double Integral
> If $f$ is continuous on a polar rectangle $R$ given by $0 \le a \le r \le b$, $\alpha \le \theta \le \beta$, where $0 \le \beta - \alpha \le 2\pi$, then
>
> $$
> \iint_R f(x, y)\,dA = \int_\alpha^\beta \int_a^b f(r\cos\theta, r\sin\theta)\,r\,dr\,d\theta .
> $$
>
> *Stewart: 15.3, Formula 2*

^thm-117-1

> [!proof]+ Proof
> *Stewart gives this as a sketch.* **The area of a polar subrectangle.** A sector of a circle with radius $r$ and central angle $\theta$ has area $\tfrac12 r^2\theta$. $R_{ij}$ is the difference of two such sectors with central angle $\Delta\theta = \theta_j - \theta_{j-1}$, so its area is exactly
>
> $$
> \Delta A_i = \tfrac12 r_i^2\,\Delta\theta - \tfrac12 r_{i-1}^2\,\Delta\theta = \tfrac12 (r_i + r_{i-1})(r_i - r_{i-1})\,\Delta\theta = r_i^*\,\Delta r\,\Delta\theta .
> $$
>
> **The Riemann sums.** The double integral was defined with ordinary rectangles, but for continuous $f$ the same value is obtained with polar subrectangles (Stewart asserts this: "it can be shown"). Taking the center of $R_{ij}$, whose rectangular coordinates are $(r_i^{\ast}\cos\theta_j^{\ast}, r_i^{\ast}\sin\theta_j^{\ast})$, as sample point, a typical Riemann sum is
>
> $$
> \sum_{i=1}^m \sum_{j=1}^n f(r_i^*\cos\theta_j^*, r_i^*\sin\theta_j^*)\,\Delta A_i = \sum_{i=1}^m \sum_{j=1}^n f(r_i^*\cos\theta_j^*, r_i^*\sin\theta_j^*)\,r_i^*\,\Delta r\,\Delta\theta . \qquad (1)
> $$
>
> With $g(r, \theta) = r f(r\cos\theta, r\sin\theta)$, the right side is $\sum_{i,j} g(r_i^*, \theta_j^*)\,\Delta r\,\Delta\theta$, an ordinary double Riemann sum ([[§115 Double Integrals Over Rectangles#^def-115-2|Definition §115.2]]) for $g$ over the rectangle $[a, b] \times [\alpha, \beta]$ in the $r\theta$-plane. Since $g$ is continuous, letting $m, n \to \infty$ and using Fubini's Theorem ([[§115 Double Integrals Over Rectangles#^thm-115-3|Theorem §115.3]]),
>
> $$
> \iint_R f(x, y)\,dA = \lim_{m, n \to \infty} \sum_{i=1}^m \sum_{j=1}^n g(r_i^*, \theta_j^*)\,\Delta r\,\Delta\theta = \int_\alpha^\beta \int_a^b g(r, \theta)\,dr\,d\theta = \int_\alpha^\beta \int_a^b f(r\cos\theta, r\sin\theta)\,r\,dr\,d\theta .
> $$

^pf-117-1

*Uses:* [[§117 Double Integrals in Polar Coordinates#^def-117-1|Def. §117.1]], [[§115 Double Integrals Over Rectangles#^def-115-2|Def. §115.2]], [[§115 Double Integrals Over Rectangles#^thm-115-3|§115.3]], [[§76 Calculus in Polar Coordinates#^thm-76-1|§76.1]] (area of a sector)

![[m233-100-1.svg]]
*Dividing a polar rectangle by circles $r = r_i$ and rays $\theta = \theta_j$. The highlighted subrectangle $R_{ij}$ is nearly an ordinary rectangle with sides $\Delta r$ (radial) and $r_i^{\ast}\Delta\theta$ (an arc of radius $r_i^{\ast}$), and its area is exactly $r_i^{\ast}\,\Delta r\,\Delta\theta$. Subrectangles far from the origin are larger: this is the factor $r$ in $dA = r\,dr\,d\theta$.*

> [!remark]- Connections
> - Rigorous treatment: [[§22 Properties of the Integral#^thm-22-6|452 Thm. §22.6]], proved there by the same computation with polar rectangles; the factor $r$ is the Jacobian of the polar map ([[§25 Change of Variables on General Domains#^ex-25-1|452 Ex. §25.1]]), the general formula being [[§124 Change of Variables in Multiple Integrals#^thm-124-1|Theorem §124.1]] (polar coordinates as a special case: [[§124 Change of Variables in Multiple Integrals#^ex-124-2|Example §124.2]]). Hub: [[Polar and spherical coordinates]].
> - The standard application to an improper integral, $\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt\pi$ (Stewart's Exercise 15.3.50): [[§25 Change of Variables on General Domains#^ex-25-4|452 Ex. §25.4]].
> - See also: [[§34★ The Error Function#^prop-34-1|341 Prop. §34.1]](d), the same computation of $\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt\pi$, with the passage to the improper integral justified by squeezing between quarter disks; it normalizes the error function.

> [!remark] Remark: Don't Forget the Factor r
> Formula 2 says: convert by writing $x = r\cos\theta$ and $y = r\sin\theta$, use the appropriate limits for $r$ and $\theta$, and replace $dA$ by $r\,dr\,d\theta$. Forgetting the $r$ is the classic mistake. A way to remember it: the "infinitesimal" polar rectangle is an ordinary rectangle with sides $dr$ and $r\,d\theta$, so it has "area" $dA = r\,dr\,d\theta$.

^rem-117-1

> [!example] Example §117.1: A Half-Ring
> Evaluate $\displaystyle\iint_R (3x + 4y^2)\,dA$, where $R$ is the region in the upper half-plane bounded by the circles $x^2 + y^2 = 1$ and $x^2 + y^2 = 4$.
>
> $R = \{(x, y) \mid y \ge 0,\ 1 \le x^2 + y^2 \le 4\}$ is the half-ring $1 \le r \le 2$, $0 \le \theta \le \pi$. By [[§117 Double Integrals in Polar Coordinates#^thm-117-1|Theorem §117.1]],
>
> $$
> \begin{aligned}
> \iint_R (3x + 4y^2)\,dA &= \int_0^{\pi} \int_1^2 \big[ 3r\cos\theta + 4r^2\sin^2\theta \big]\,r\,dr\,d\theta = \int_0^{\pi} \int_1^2 (3r^2\cos\theta + 4r^3\sin^2\theta)\,dr\,d\theta \\
> &= \int_0^{\pi} \Big[ r^3\cos\theta + r^4\sin^2\theta \Big]_{r=1}^{r=2} d\theta = \int_0^{\pi} (7\cos\theta + 15\sin^2\theta)\,d\theta \\
> &= \int_0^{\pi} \Big[ 7\cos\theta + \tfrac{15}{2}(1 - \cos 2\theta) \Big]\,d\theta = \Big[ 7\sin\theta + \frac{15\theta}{2} - \frac{15}{4}\sin 2\theta \Big]_0^{\pi} = \frac{15\pi}{2} ,
> \end{aligned}
> $$
>
> using $\sin^2\theta = \frac12(1 - \cos 2\theta)$ ([[§52 Trigonometric Integrals#^thm-52-1|Theorem §52.1]]).
>
> *Stewart: Example 15.3.1*

^ex-117-1

> [!example] Example §117.2: The Volume Between Two Paraboloids
> Find the volume of the solid enclosed by the paraboloids $z = x^2 + y^2$ and $z = 4 - x^2 - y^2$.
>
> The paraboloids meet where $x^2 + y^2 = 4 - x^2 - y^2$, that is, $x^2 + y^2 = 2$. Over the disk $D$: $x^2 + y^2 \le 2$ the downward paraboloid is on top, so the volume is $\iint_D \big[ (4 - x^2 - y^2) - (x^2 + y^2) \big]\,dA$ (the volume under the top surface minus the volume under the bottom one). In polar coordinates $D$ is $0 \le r \le \sqrt2$, $0 \le \theta \le 2\pi$, and the height is $4 - 2r^2$:
>
> $$
> V = \int_0^{2\pi} \int_0^{\sqrt2} (4 - 2r^2)\,r\,dr\,d\theta = 2\pi \Big[ 2r^2 - \frac{r^4}{2} \Big]_0^{\sqrt2} = 2\pi (4 - 2) = 4\pi .
> $$
>
> In rectangular coordinates the same integral would be $\int_{-\sqrt2}^{\sqrt2} \int_{-\sqrt{2 - x^2}}^{\sqrt{2 - x^2}} (4 - 2x^2 - 2y^2)\,dy\,dx$, which leads to $\int (2 - x^2)^{3/2}\,dx$; Stewart's Example 15.3.3 (the volume $\pi/2$ under $z = 1 - x^2 - y^2$) makes the same point.
>
> *Source: 233 Chapter 15 Review, Q3*

^ex-117-2

> [!example] Example §117.3: Rewriting an Iterated Integral in Polar Coordinates
> Rewrite $\displaystyle\int_0^{\sqrt2} \int_x^{\sqrt{4 - x^2}} x \sin\big((x^2 + y^2)^{3/2}\big)\,dy\,dx$ using polar coordinates, and evaluate it.
>
> **The region.** $0 \le x \le \sqrt2$ and $x \le y \le \sqrt{4 - x^2}$: above the line $y = x$, below the circle $x^2 + y^2 = 4$, and to the right of the $y$-axis. The line meets the circle at $(\sqrt2, \sqrt2)$, so the region is the sector $0 \le r \le 2$, $\pi/4 \le \theta \le \pi/2$.
>
> **The integrand.** $x \sin\big((x^2 + y^2)^{3/2}\big) = r\cos\theta \sin(r^3)$, and $dA = r\,dr\,d\theta$:
>
> $$
> \int_0^{\sqrt2} \int_x^{\sqrt{4 - x^2}} x \sin\big((x^2 + y^2)^{3/2}\big)\,dy\,dx = \int_{\pi/4}^{\pi/2} \int_0^2 r^2\cos\theta \sin(r^3)\,dr\,d\theta .
> $$
>
> **The value.** The integrand is a product ([[§115 Double Integrals Over Rectangles#^thm-115-4|Theorem §115.4]] in the $r\theta$-plane):
>
> $$
> \int_{\pi/4}^{\pi/2} \cos\theta\,d\theta \int_0^2 r^2\sin(r^3)\,dr = \Big(1 - \frac{\sqrt2}{2}\Big) \Big[ -\frac{\cos(r^3)}{3} \Big]_0^2 = \frac{(2 - \sqrt2)(1 - \cos 8)}{6} .
> $$
>
> The extra $r$ from $dA$ is exactly what makes $\int r^2\sin(r^3)\,dr$ elementary.
>
> *Source: 233 Exam 2 Practice Questions, Q14 (the evaluation is added here)*

^ex-117-3

What has been done for polar rectangles extends to regions that play the role of type II regions ([[§116 Double Integrals Over General Regions#^def-116-3|Definition §116.3]]) in polar coordinates.

> [!theorem] Theorem §117.2: Integrals over Polar Regions
> If $f$ is continuous on a polar region of the form
>
> $$
> D = \{(r, \theta) \mid \alpha \le \theta \le \beta,\ h_1(\theta) \le r \le h_2(\theta)\} ,
> $$
>
> then
>
> $$
> \iint_D f(x, y)\,dA = \int_\alpha^\beta \int_{h_1(\theta)}^{h_2(\theta)} f(r\cos\theta, r\sin\theta)\,r\,dr\,d\theta .
> $$
>
> *Stewart: 15.3, Formula 3*

^thm-117-2

> [!proof]+ Proof
> *Stewart says this follows by "combining Formula 2 with Formula 15.2.4"; here are the details.* Choose $0 \le a \le h_1(\theta)$ and $b \ge h_2(\theta)$ for all $\theta$ (the $h_i$ are continuous, hence bounded), so that $D$ lies in the polar rectangle $R = \{a \le r \le b,\ \alpha \le \theta \le \beta\}$. Let $F = f$ on $D$ and $F = 0$ on the rest of $R$; by Definition 15.2.2 ([[§116 Double Integrals Over General Regions#^def-116-1|Definition §116.1]]), $\iint_D f\,dA = \iint_R F\,dA$. Applying Formula 2 to $F$ (the argument of [[§117 Double Integrals in Polar Coordinates#^thm-117-1|Theorem §117.1]] goes through for $F$, which is bounded and discontinuous only on the curves $r = h_1(\theta)$, $r = h_2(\theta)$),
>
> $$
> \iint_R F\,dA = \int_\alpha^\beta \int_a^b F(r\cos\theta, r\sin\theta)\,r\,dr\,d\theta .
> $$
>
> For fixed $\theta$ the inner integrand is $0$ unless $h_1(\theta) \le r \le h_2(\theta)$, where it equals $f(r\cos\theta, r\sin\theta)\,r$. So the inner integral is $\int_{h_1(\theta)}^{h_2(\theta)} f(r\cos\theta, r\sin\theta)\,r\,dr$, exactly as in the proof of [[§116 Double Integrals Over General Regions#^thm-116-2|Theorem §116.2]].

^pf-117-2

*Uses:* [[§117 Double Integrals in Polar Coordinates#^thm-117-1|§117.1]], [[§116 Double Integrals Over General Regions#^def-116-1|Def. §116.1]], [[§116 Double Integrals Over General Regions#^thm-116-2|§116.2]]

> [!theorem] Corollary §117.3: Area of a Polar Region
> The area of the region $D$ bounded by $\theta = \alpha$, $\theta = \beta$ and $r = h(\theta)$ (with $h \ge 0$) is
>
> $$
> A(D) = \int_\alpha^\beta \tfrac12 [h(\theta)]^2\,d\theta ,
> $$
>
> in agreement with Formula 10.4.3 ([[§76 Calculus in Polar Coordinates#^thm-76-2|Theorem §76.2]]).
>
> *Stewart: 15.3 (text)*

^cor-117-3

> [!proof]+ Proof
> Take $f(x, y) = 1$, $h_1(\theta) = 0$ and $h_2(\theta) = h(\theta)$ in [[§117 Double Integrals in Polar Coordinates#^thm-117-2|Theorem §117.2]] and use $\iint_D 1\,dA = A(D)$ ([[§116 Double Integrals Over General Regions#^thm-116-5|Theorem §116.5]]):
>
> $$
> A(D) = \iint_D 1\,dA = \int_\alpha^\beta \int_0^{h(\theta)} r\,dr\,d\theta = \int_\alpha^\beta \Big[ \frac{r^2}{2} \Big]_0^{h(\theta)} d\theta = \int_\alpha^\beta \tfrac12 [h(\theta)]^2\,d\theta .
> $$

^pf-117-3

*Uses:* [[§117 Double Integrals in Polar Coordinates#^thm-117-2|§117.2]], [[§116 Double Integrals Over General Regions#^thm-116-5|§116.5]]

> [!example] Example §117.4: One Loop of a Rose
> Use a double integral to find the area enclosed by one loop of the four-leaved rose $r = \cos 2\theta$.
>
> The loop along the positive $x$-axis is traced as $\theta$ runs from $-\pi/4$ to $\pi/4$ (where $\cos 2\theta = 0$), so it is the region
>
> $$
> D = \{(r, \theta) \mid -\pi/4 \le \theta \le \pi/4,\ 0 \le r \le \cos 2\theta\} .
> $$
>
> So
>
> $$
> \begin{aligned}
> A(D) &= \iint_D dA = \int_{-\pi/4}^{\pi/4} \int_0^{\cos 2\theta} r\,dr\,d\theta = \int_{-\pi/4}^{\pi/4} \Big[ \tfrac12 r^2 \Big]_0^{\cos 2\theta} d\theta = \frac12 \int_{-\pi/4}^{\pi/4} \cos^2 2\theta\,d\theta \\
> &= \frac14 \int_{-\pi/4}^{\pi/4} (1 + \cos 4\theta)\,d\theta = \frac14 \Big[ \theta + \tfrac14 \sin 4\theta \Big]_{-\pi/4}^{\pi/4} = \frac{\pi}{8} .
> \end{aligned}
> $$
>
> *Stewart: Example 15.3.4 (= 233 Chapter 15 Review, Q5)*

^ex-117-4

*Chain: the four-leaved rose earlier in [[§79 The Cycloid, the Cardioid and the Four-Leaved Rose#The Four-Leaved Rose|Chapter 10]].*

> [!example] Example §117.5: Inside an Off-Center Cylinder
> Find the volume of the solid that lies under the paraboloid $z = x^2 + y^2$, above the $xy$-plane, and inside the cylinder $x^2 + y^2 = 2x$.
>
> **The region.** The solid lies above the disk $D$ bounded by $x^2 + y^2 = 2x$, that is, $(x - 1)^2 + y^2 = 1$ after completing the square: the circle of radius $1$ centered at $(1, 0)$. In polar coordinates $x^2 + y^2 = r^2$ and $x = r\cos\theta$, so the circle is $r^2 = 2r\cos\theta$, or $r = 2\cos\theta$. It passes through the origin and is traced once as $\theta$ runs from $-\pi/2$ to $\pi/2$:
>
> $$
> D = \{(r, \theta) \mid -\pi/2 \le \theta \le \pi/2,\ 0 \le r \le 2\cos\theta\} .
> $$
>
> **The volume.** By [[§117 Double Integrals in Polar Coordinates#^thm-117-2|Theorem §117.2]],
>
> $$
> \begin{aligned}
> V &= \iint_D (x^2 + y^2)\,dA = \int_{-\pi/2}^{\pi/2} \int_0^{2\cos\theta} r^2 \cdot r\,dr\,d\theta = \int_{-\pi/2}^{\pi/2} \Big[ \frac{r^4}{4} \Big]_0^{2\cos\theta} d\theta = 4\int_{-\pi/2}^{\pi/2} \cos^4\theta\,d\theta \\
> &= 8\int_0^{\pi/2} \cos^4\theta\,d\theta = 8\int_0^{\pi/2} \Big( \frac{1 + \cos 2\theta}{2} \Big)^2 d\theta = 2\int_0^{\pi/2} \big[ 1 + 2\cos 2\theta + \tfrac12 (1 + \cos 4\theta) \big]\,d\theta \\
> &= 2\Big[ \tfrac32\theta + \sin 2\theta + \tfrac18 \sin 4\theta \Big]_0^{\pi/2} = 2\Big(\frac32\Big)\Big(\frac{\pi}{2}\Big) = \frac{3\pi}{2} .
> \end{aligned}
> $$
>
> *Stewart: Example 15.3.5*

^ex-117-5
