---
type: section
subject: "[[Calculus]]"
chapter: 3
section: 22
stewart: "3.9"
aliases: ["Stewart 3.9"]
tags: [calculus]
---
← [[§21 Exponential Growth and Decay]] · ↑ [[· 3 Differentiation Rules]] · [[§23 Linear Approximations and Differentials]] →

*Stewart, Section 3.9.*

When air is pumped into a balloon, its volume and its radius both increase, and their rates of increase are related; the first is much easier to measure than the second. In a related rates problem one computes the rate of change of one quantity from the rate of change of another (which may be easier to measure). The procedure: find an equation that relates the two quantities at every time $t$, differentiate both sides with respect to $t$ by the Chain Rule ([[§17 The Chain Rule#^thm-17-2|Theorem §17.2]]), as in implicit differentiation ([[§18 Implicit Differentiation#^rem-18-1|Remark: Method — Implicit Differentiation]]), and only then substitute the numbers. The section consists of a strategy and five model problems.

## The Strategy

> [!remark] Remark: Method — Related Rates
> 1. Read the problem carefully: identify the *given* information and the *unknown*.
> 2. Draw a diagram if possible.
> 3. Introduce notation. Assign symbols to all quantities that are functions of time.
> 4. Express the given information and the required rate in terms of derivatives: rates of change are derivatives with respect to $t$.
> 5. Write an equation that relates the various quantities of the problem. If necessary, use the geometry of the situation to eliminate one of the variables by substitution (as in Example §22.3).
> 6. Use the Chain Rule to differentiate both sides of the equation with respect to $t$.
> 7. Substitute the given information into the resulting equation and solve for the unknown rate.
>
> *Stewart: 3.9, Problem Solving Strategy*

^rem-22-1

> [!remark] Remark: Substitute Only After Differentiating
> A common error is to substitute the given numerical information, for quantities that vary with time, too early. Step 7 must follow Step 6. In Example §22.1, the radius is kept as a general $r$ until the last step; putting $r = 25$ into $V = \frac43 \pi r^3$ before differentiating would give the constant $V = \frac43 \pi (25)^3$ and so $dV/dt = 0$, which is clearly wrong. Constants of the problem (the length of a ladder, the dimensions of a tank) may be substituted at any time.

^rem-22-2

## Examples

> [!example] Example §22.1: Inflating a Balloon
> Air is pumped into a spherical balloon so that its volume increases at a rate of $100$ cm³/s. How fast is the radius increasing when the diameter is $50$ cm?
>
> **Given and unknown.** Let $V$ be the volume and $r$ the radius of the balloon, both functions of time $t$. Given: $\dfrac{dV}{dt} = 100$ cm³/s. Unknown: $\dfrac{dr}{dt}$ when $r = 25$ cm.
>
> **Relate and differentiate.** $V = \frac43 \pi r^3$. Differentiate each side with respect to $t$, using the Chain Rule on the right:
>
> $$
> \frac{dV}{dt} = \frac{dV}{dr}\,\frac{dr}{dt} = 4\pi r^2 \frac{dr}{dt}, \qquad\text{so}\qquad \frac{dr}{dt} = \frac{1}{4\pi r^2}\,\frac{dV}{dt} .
> $$
>
> **Substitute.** With $r = 25$ and $dV/dt = 100$,
>
> $$
> \frac{dr}{dt} = \frac{1}{4\pi (25)^2}\,100 = \frac{1}{25\pi} \approx 0.0127 \text{ cm/s} .
> $$
>
> Although $dV/dt$ is constant, $dr/dt$ is not: it decreases like $1/r^2$ as the balloon grows.
>
> *Stewart: Example 3.9.1*

^ex-22-1

> [!example] Example §22.2: A Sliding Ladder
> A ladder $10$ ft long rests against a vertical wall. If the bottom of the ladder slides away from the wall at a rate of $4$ ft/s, how fast is the top sliding down the wall when the bottom is $6$ ft from the wall?
>
> Let $x$ ft be the distance from the bottom of the ladder to the wall and $y$ ft the height of the top of the ladder, both functions of $t$ (seconds). Given: $dx/dt = 4$ ft/s. Unknown: $dy/dt$ when $x = 6$ ft. By the Pythagorean Theorem,
>
> $$
> x^2 + y^2 = 100 .
> $$
>
> Differentiate each side with respect to $t$ and solve:
>
> $$
> 2x\,\frac{dx}{dt} + 2y\,\frac{dy}{dt} = 0, \qquad \frac{dy}{dt} = -\frac{x}{y}\,\frac{dx}{dt} .
> $$
>
> When $x = 6$, $y = \sqrt{100 - 36} = 8$, so
>
> $$
> \frac{dy}{dt} = -\frac68 (4) = -3 \text{ ft/s} .
> $$
>
> The negative sign means that the height is *decreasing*: the top of the ladder slides down the wall at $3$ ft/s.
>
> *Stewart: Example 3.9.2*

^ex-22-2

> [!example] Example §22.3: Filling a Conical Tank
> A water tank has the shape of an inverted circular cone with base radius $2$ m and height $4$ m. Water is pumped in at $2$ m³/min. How fast is the water level rising when the water is $3$ m deep?
>
> Let $V$, $r$ and $h$ be the volume of the water, the radius of its surface and its depth at time $t$ (minutes). Given: $dV/dt = 2$ m³/min. Unknown: $dh/dt$ when $h = 3$ m. The quantities are related by $V = \frac13 \pi r^2 h$.
>
> **Eliminate $r$** (Step 5). The water forms a cone similar to the tank, so by similar triangles
>
> $$
> \frac{r}{h} = \frac24, \qquad r = \frac h2, \qquad V = \frac13 \pi \left( \frac h2 \right)^2 h = \frac{\pi}{12} h^3 .
> $$
>
> **Differentiate** with respect to $t$:
>
> $$
> \frac{dV}{dt} = \frac{\pi}{4} h^2 \frac{dh}{dt}, \qquad \frac{dh}{dt} = \frac{4}{\pi h^2}\,\frac{dV}{dt} .
> $$
>
> **Substitute** $h = 3$ and $dV/dt = 2$:
>
> $$
> \frac{dh}{dt} = \frac{4}{\pi (3)^2} \cdot 2 = \frac{8}{9\pi} \approx 0.28 \text{ m/min} .
> $$
>
> *Stewart: Example 3.9.3*

^ex-22-3

![[m233-22-1.svg]]
*The conical tank of Example §22.3. The water (blue) is a smaller cone similar to the tank, so its surface radius and depth are in the ratio $r : h = 2 : 4$ of the tank (the red triangles). This is the relation that eliminates $r$ before differentiating.*

> [!example] Example §22.4: Two Cars Approaching an Intersection
> Car A travels west at $50$ mi/h and car B travels north at $60$ mi/h, both toward the intersection $C$ of their roads. At what rate are the cars approaching each other when car A is $0.3$ mi and car B is $0.4$ mi from the intersection?
>
> At time $t$ let $x$ be the distance from car A to $C$, $y$ the distance from car B to $C$, and $z$ the distance between the cars (in miles). Given: $dx/dt = -50$ mi/h and $dy/dt = -60$ mi/h (negative because $x$ and $y$ decrease). Unknown: $dz/dt$. By the Pythagorean Theorem $z^2 = x^2 + y^2$, so
>
> $$
> 2z\,\frac{dz}{dt} = 2x\,\frac{dx}{dt} + 2y\,\frac{dy}{dt}, \qquad \frac{dz}{dt} = \frac1z \left( x\,\frac{dx}{dt} + y\,\frac{dy}{dt} \right) .
> $$
>
> When $x = 0.3$ and $y = 0.4$, $z = \sqrt{0.09 + 0.16} = 0.5$, so
>
> $$
> \frac{dz}{dt} = \frac{1}{0.5}\big[0.3(-50) + 0.4(-60)\big] = 2(-15 - 24) = -78 \text{ mi/h} .
> $$
>
> The cars are approaching each other at $78$ mi/h.
>
> *Stewart: Example 3.9.4*

^ex-22-4

> [!example] Example §22.5: A Rotating Spotlight
> A man walks along a straight path at $4$ ft/s. A spotlight on the ground $20$ ft from the path is kept focused on him. At what rate is the spotlight rotating when he is $15$ ft from the point on the path closest to the light?
>
> Let $x$ be the distance from the man to the point on the path closest to the spotlight, and $\theta$ the angle between the beam and the perpendicular from the light to the path. Given: $dx/dt = 4$ ft/s. Unknown: $d\theta/dt$ when $x = 15$. From the right triangle,
>
> $$
> \frac{x}{20} = \tan\theta, \qquad x = 20\tan\theta .
> $$
>
> Differentiate with respect to $t$:
>
> $$
> \frac{dx}{dt} = 20\sec^2\theta\,\frac{d\theta}{dt}, \qquad \frac{d\theta}{dt} = \frac{1}{20}\cos^2\theta\,\frac{dx}{dt} = \frac{1}{20}\cos^2\theta\,(4) = \frac15 \cos^2\theta .
> $$
>
> When $x = 15$, the beam has length $\sqrt{20^2 + 15^2} = 25$, so $\cos\theta = \frac{20}{25} = \frac45$ and
>
> $$
> \frac{d\theta}{dt} = \frac15 \left( \frac45 \right)^2 = \frac{16}{125} = 0.128 \text{ rad/s} ,
> $$
>
> that is, $0.128 \cdot \frac{60}{2\pi} \approx 1.22$ rotations per minute.
>
> *Stewart: Example 3.9.5*

^ex-22-5
