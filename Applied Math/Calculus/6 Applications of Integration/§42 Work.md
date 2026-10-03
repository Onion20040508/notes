---
type: section
subject: "[[Calculus]]"
chapter: 6
section: 42
stewart: "6.4"
aliases: ["Stewart 6.4"]
tags: [calculus]
---
← [[§41 Volumes by Cylindrical Shells]] · ↑ [[· 6 Applications of Integration]] · [[§43 Average Value of a Function]] →

*Stewart, Section 6.4.*

In physics, *work* is force times distance when the force is constant. When the force varies with position, cut the path into short pieces on which the force is nearly constant, add the products, and take the limit: $W = \int_a^b f(x)\,dx$. The same slicing handles problems where the force is constant but different parts of the object move different distances, such as lifting a hanging cable or pumping water out of a tank. There one slices the *object* rather than the path, and each slice contributes (its weight) × (the distance it is lifted).

## Force and Work

> [!definition] Definition §42.1: Force
> If an object of mass $m$ moves along a straight line with position function $s(t)$, then the **force** $F$ on the object (in the same direction) is given by Newton's Second Law of Motion as the product of its mass and its acceleration $a$:
>
> $$
> F = ma = m\,\frac{d^2 s}{dt^2} .
> $$
>
> **Units.** In the SI metric system mass is measured in kilograms (kg), displacement in meters (m), time in seconds (s), and force in newtons ($\mathrm{N} = \mathrm{kg \cdot m/s^2}$): a force of $1$ N acting on a mass of $1$ kg produces an acceleration of $1\ \mathrm{m/s^2}$. In the US Customary system the fundamental unit is the unit of force, the pound.
>
> *Stewart: 6.4, Equation 1*

^def-42-1

> [!definition] Definition §42.2: Work Done by a Constant Force
> If the acceleration, and hence the force $F$, is constant, the **work** done in moving the object a distance $d$ is
>
> $$
> W = Fd \qquad (\text{work} = \text{force} \times \text{distance}) .
> $$
>
> If $F$ is in newtons and $d$ in meters, $W$ is in newton-meters, called **joules** (J). If $F$ is in pounds and $d$ in feet, $W$ is in **foot-pounds** (ft-lb); $1$ ft-lb $\approx 1.36$ J.
>
> *Stewart: 6.4, Equation 2*

^def-42-2

Now let the force vary. An object moves along the $x$-axis in the positive direction from $x = a$ to $x = b$, and at each point $x$ a force $f(x)$ acts on it, where $f$ is continuous. Divide $[a, b]$ into $n$ subintervals of equal width $\Delta x$ with endpoints $x_0, \ldots, x_n$, and choose $x_i^* \in [x_{i-1}, x_i]$. For large $n$, $\Delta x$ is small, and since $f$ is continuous its values hardly change over $[x_{i-1}, x_i]$: the force is almost constant there. So the work $W_i$ done in moving the particle from $x_{i-1}$ to $x_i$ is approximately $f(x_i^*)\,\Delta x$, and

$$
W \approx \sum_{i=1}^{n} f(x_i^*)\,\Delta x . \qquad (3)
$$

The approximation improves as $n$ grows, and the right side of (3) is a Riemann sum.

> [!definition] Definition §42.3: Work Done by a Variable Force
> The **work done in moving the object from $a$ to $b$** under the continuous force $f(x)$ is the limit of the sums (3):
>
> $$
> W = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*)\,\Delta x = \int_a^b f(x)\,dx .
> $$
>
> For a constant force $f(x) = F$ this gives $W = F(b - a)$, in agreement with Definition §42.2.
>
> *Stewart: 6.4, Equation 4*

^def-42-3

> [!remark]- Connections
> - Along a curve instead of a line, with the force a vector field, the work is the line integral $\int_C \mathbf{F} \cdot d\mathbf{r}$ ([[§108 Line Integrals#^def-108-7|Def. §108.7]], [[§108 Line Integrals#^def-108-8|Def. §108.8]]; [[§16 Line Integrals and Green's Theorem#^def-16-2|452 Def. §16.2]]). For motion along the $x$-axis with $\mathbf{F} = f(x)\,\mathbf{i}$ it reduces to Definition §42.3.

> [!example] Example §42.1: Constant and Variable Forces
> **(a)** How much work is done in lifting a $1.2$-kg book off the floor onto a desk $0.7$ m high? (Use $g = 9.8\ \mathrm{m/s^2}$.)
>
> The force exerted is equal and opposite to that of gravity, so by Definition §42.1, $F = mg = (1.2)(9.8) = 11.76$ N, and by Definition §42.2
>
> $$
> W = Fd = (11.76\ \mathrm{N})(0.7\ \mathrm{m}) \approx 8.2\ \mathrm{J} .
> $$
>
> **(b)** How much work is done in lifting a $20$-lb weight $6$ ft off the ground?
>
> Here the force is given: $F = 20$ lb, so $W = Fd = (20\ \mathrm{lb})(6\ \mathrm{ft}) = 120$ ft-lb. Unlike in (a), there is no multiplication by $g$, because the *weight* (a force) was given, not the mass.
>
> **(c)** At a distance $x$ feet from the origin, a force of $x^2 + 2x$ pounds acts on a particle. How much work is done in moving it from $x = 1$ to $x = 3$?
>
> By Definition §42.3,
>
> $$
> W = \int_1^3 (x^2 + 2x)\,dx = \frac{x^3}{3} + x^2 \Big]_1^3 = (9 + 9) - \Big(\frac13 + 1\Big) = \frac{50}{3} .
> $$
>
> The work done is $16\frac23$ ft-lb.
>
> *Stewart: Examples 6.4.1 and 6.4.2*

^ex-42-1

## Springs

> [!definition] Definition §42.4: Hooke's Law; Spring Constant
> **Hooke's Law** states that the force required to maintain a spring stretched $x$ units beyond its natural length is proportional to $x$:
>
> $$
> f(x) = kx ,
> $$
>
> where $k$ is a positive constant called the **spring constant**. (Hooke's Law is a law of physics, valid provided that $x$ is not too large.)
>
> *Stewart: 6.4 (text)*

^def-42-4

> [!example] Example §42.2: Stretching a Spring
> A force of $40$ N is required to hold a spring that has been stretched from its natural length of $10$ cm to a length of $15$ cm. How much work is done in stretching the spring from $15$ cm to $18$ cm?
>
> By Hooke's Law the force needed to hold the spring stretched $x$ meters beyond its natural length is $f(x) = kx$. Stretching from $10$ cm to $15$ cm is $x = 5$ cm $= 0.05$ m, so $f(0.05) = 40$:
>
> $$
> 0.05k = 40, \qquad k = \frac{40}{0.05} = 800 .
> $$
>
> So $f(x) = 800x$. Stretching from $15$ cm to $18$ cm means $x$ goes from $0.05$ m to $0.08$ m (lengths beyond the natural length, in meters), and
>
> $$
> W = \int_{0.05}^{0.08} 800x\,dx = 800\,\frac{x^2}{2} \Big]_{0.05}^{0.08} = 400\big[(0.08)^2 - (0.05)^2\big] = 400(0.0064 - 0.0025) = 1.56\ \mathrm{J} .
> $$
>
> *Stewart: Example 6.4.3*

^ex-42-2

## Lifting by Slicing the Object

When different parts of an object move different distances, slice the object instead of the path.

> [!remark] Remark: Method — Work by Slicing the Object
> 1. Choose a coordinate axis along the direction of motion and say where its origin is and which way it points. (Measuring depth from the top, axis pointing down, often keeps the formulas simple.)
> 2. Cut the object into $n$ thin pieces of thickness $\Delta x$ at $x_i^*$, so thin that every point of a piece moves about the same distance.
> 3. For each piece find its **force**: its weight; for a mass, density × volume × $g$ (the volume from the geometry, often by similar triangles).
> 4. Find the **distance** that piece is moved.
> 5. Work on the piece ≈ force × distance. Add over the pieces and let $n \to \infty$: the Riemann sum becomes an integral.
> 6. Check units: the unit of $\int_a^b f(x)\,dx$ is the unit of $f(x)$ times the unit of $x$ ([[§37 Indefinite Integrals and the Net Change Theorem#^ex-37-4|Example §37.4]]).

^rem-42-1

> [!example] Example §42.3: Lifting a Cable
> A $200$-lb cable is $100$ ft long and hangs vertically from the top of a tall building.
>
> **(a)** How much work is required to lift the cable to the top of the building?
>
> **(b)** How much work is required to pull up only $20$ ft of the cable?
>
> **(a)** Put the origin at the top of the building with the $x$-axis pointing downward. Divide the cable into small parts of length $\Delta x$. If $x_i^{\ast}$ is a point in the $i$th part, every point of that part is lifted about the same distance $x_i^{\ast}$. The cable weighs $200/100 = 2$ lb/ft, so the $i$th part weighs $(2\ \mathrm{lb/ft})(\Delta x\ \mathrm{ft}) = 2\Delta x$ lb. The work done on it is
>
> $$
> \underbrace{(2\Delta x)}_{\text{force}} \cdot \underbrace{x_i^*}_{\text{distance}} = 2x_i^*\,\Delta x \ \text{ft-lb} .
> $$
>
> Adding and letting $n \to \infty$ (so $\Delta x \to 0$):
>
> $$
> W = \lim_{n \to \infty} \sum_{i=1}^{n} 2x_i^*\,\Delta x = \int_0^{100} 2x\,dx = x^2 \Big]_0^{100} = 10{,}000\ \text{ft-lb} .
> $$
>
> (With the origin at the bottom of the cable and the axis pointing up, a piece at height $x$ is lifted $100 - x$, and $W = \int_0^{100} 2(100 - x)\,dx = 10{,}000$ ft-lb as well.)
>
> **(b)** The top $20$ ft of cable is lifted as in (a):
>
> $$
> W_1 = \int_0^{20} 2x\,dx = x^2 \Big]_0^{20} = 400\ \text{ft-lb} .
> $$
>
> Every part of the lower $80$ ft moves the same distance, $20$ ft:
>
> $$
> W_2 = \lim_{n \to \infty} \sum_{i=1}^{n} \underbrace{20}_{\text{distance}} \cdot \underbrace{2\Delta x}_{\text{force}} = \int_{20}^{100} 40\,dx = 40 \cdot 80 = 3200\ \text{ft-lb} .
> $$
>
> (Or directly: the lower $80$ ft weighs $160$ lb and is lifted uniformly $20$ ft, so $160 \cdot 20 = 3200$ ft-lb.) The total is $W_1 + W_2 = 400 + 3200 = 3600$ ft-lb.
>
> *Stewart: Example 6.4.4*

^ex-42-3

> [!example] Example §42.4: Pumping Water out of a Conical Tank
> A tank has the shape of an inverted circular cone with height $10$ m and base radius $4$ m. It is filled with water to a height of $8$ m. Find the work required to empty the tank by pumping all of the water to the top of the tank. (The density of water is $1000\ \mathrm{kg/m^3}$.)
>
> **Coordinates.** Measure depth $x$ from the top of the tank. The water extends from depth $2$ m to depth $10$ m. Divide $[2, 10]$ into $n$ subintervals with endpoints $x_0, \ldots, x_n$ and choose $x_i^{\ast}$ in the $i$th one. This divides the water into $n$ layers.
>
> **One layer.** The $i$th layer is approximately a circular cylinder of radius $r_i$ and height $\Delta x$. By similar triangles (the cone narrows from radius $4$ at depth $0$ to radius $0$ at depth $10$),
>
> $$
> \frac{r_i}{10 - x_i^*} = \frac{4}{10}, \qquad r_i = \tfrac25 (10 - x_i^*) .
> $$
>
> So the layer has volume $V_i \approx \pi r_i^2\,\Delta x = \frac{4\pi}{25}(10 - x_i^*)^2\,\Delta x$, mass
>
> $$
> m_i = \text{density} \times \text{volume} \approx 1000 \cdot \frac{4\pi}{25}(10 - x_i^*)^2\,\Delta x = 160\pi (10 - x_i^*)^2\,\Delta x ,
> $$
>
> and the force needed to raise it overcomes gravity:
>
> $$
> F_i = m_i g \approx (9.8)\,160\pi (10 - x_i^*)^2\,\Delta x = 1568\pi (10 - x_i^*)^2\,\Delta x .
> $$
>
> Each particle of the layer travels upward about $x_i^*$, so the work to raise this layer to the top is $W_i \approx F_i x_i^* \approx 1568\pi\,x_i^* (10 - x_i^*)^2\,\Delta x$.
>
> **Total.** Adding over the layers and letting $n \to \infty$:
>
> $$
> \begin{aligned}
> W &= \lim_{n \to \infty} \sum_{i=1}^{n} 1568\pi\,x_i^* (10 - x_i^*)^2\,\Delta x = \int_2^{10} 1568\pi\,x (10 - x)^2\,dx \\
> &= 1568\pi \int_2^{10} (100x - 20x^2 + x^3)\,dx = 1568\pi \Big[50x^2 - \frac{20x^3}{3} + \frac{x^4}{4}\Big]_2^{10} \\
> &= 1568\pi \Big(\frac{2500}{3} - \frac{452}{3}\Big) = 1568\pi \cdot \frac{2048}{3} \approx 3.4 \times 10^6\ \mathrm{J} .
> \end{aligned}
> $$
>
> (At $x = 10$ the bracket is $5000 - \frac{20000}{3} + 2500 = \frac{2500}{3}$; at $x = 2$ it is $200 - \frac{160}{3} + 4 = \frac{452}{3}$.)
>
> *Stewart: Example 6.4.5*

^ex-42-4

![[m233-42-1.svg]]
*Example §42.4. Depth $x$ is measured downward from the top of the tank, and the water fills depths $2$ to $10$. The layer at depth $x$ (red) is a disk of thickness $\Delta x$ whose radius comes from similar triangles: $r/(10 - x) = 4/10$. It must be lifted a distance $x$ to the top. Deeper layers are smaller but travel farther.*
