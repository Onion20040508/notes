---
type: section
subject: "[[Calculus]]"
chapter: 13
section: 104
stewart: "13.4"
aliases: ["Stewart 13.4"]
tags: [calculus, math233]
---
← [[§103 The TNB Frame and Torsion]] · ↑ [[· 13 Vector Functions]] · [[§105 The Helix]] →

*Stewart, Section 13.4 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q14(b), Q21), Practice Exam 1 (Q3(a), Q6), Exam 1 Review (Q15).*

If $\mathbf{r}(t)$ is the position of a moving particle, its derivative is the velocity, the length of the velocity is the speed, and the second derivative is the acceleration. Integrating runs the other way: from acceleration and initial values to velocity and position, which together with Newton's Second Law gives the equations of projectile motion. Splitting the acceleration along the unit tangent and unit normal of [[§102 Arc Length and Curvature|§102]] shows that it always lies in the osculating plane, with tangential part $v'$ (change of speed) and normal part $\kappa v^2$ (turning). The section ends with one of the great accomplishments of calculus: Newton's derivation of Kepler's First Law, that planets move in ellipses, using only the vector calculus of this chapter.

## Velocity, Speed, and Acceleration

> [!definition] Definition §122.1: Velocity
> Suppose a particle moves through space so that its position vector at time $t$ is $\mathbf{r}(t)$. For small $h$, the vector $\dfrac{\mathbf{r}(t + h) - \mathbf{r}(t)}{h}$ is its **average velocity** over a time interval of length $h$: it approximates the direction of motion, and its magnitude is the displacement per unit time. The **velocity vector** at time $t$ is the limit
>
> $$
> \mathbf{v}(t) = \lim_{h \to 0} \frac{\mathbf{r}(t + h) - \mathbf{r}(t)}{h} = \mathbf{r}'(t) .
> $$
>
> So the velocity is also the tangent vector and points along the tangent line.
>
> *Stewart: 13.4, Equation 2 and text*

^def-104-1

> [!definition] Definition §104.2: Speed
> The **speed** at time $t$ is the magnitude $|\mathbf{v}(t)|$ of the velocity.
>
> *Stewart: 13.4, Equation 2 and text*

^def-104-2

> [!definition] Definition §104.3: Acceleration
> The **acceleration** is the derivative of the velocity:
>
> $$
> \mathbf{a}(t) = \mathbf{v}'(t) = \mathbf{r}''(t) .
> $$
>
> *Stewart: 13.4, Equation 2 and text*

^def-104-3

> [!theorem] Proposition §122.1: Speed Is the Rate of Change of Distance
> $$
> |\mathbf{v}(t)| = |\mathbf{r}'(t)| = \frac{ds}{dt} ,
> $$
>
> the rate of change of distance traveled (arc length) with respect to time.
>
> *Stewart: 13.4 (text)*

^prop-104-1

> [!proof]+ Proof
> $\mathbf{v} = \mathbf{r}'$ by [[§104 Motion in Space꞉ Velocity and Acceleration#^def-104-1|Definition §104.1]], and $|\mathbf{r}'(t)| = ds/dt$ by [[§102 Arc Length and Curvature#^prop-102-2|Proposition §102.2]].

^pf-104-1

*Uses:* [[§104 Motion in Space꞉ Velocity and Acceleration#^def-104-1|Def. §104.1]], [[§104 Motion in Space꞉ Velocity and Acceleration#^def-104-2|Def. §104.2]], [[§102 Arc Length and Curvature#^prop-102-2|§102.2]]

> [!remark] Remark: The Road and the Drive
> A curve can be parametrized in many ways, and its geometric properties (arc length, curvature, torsion) do not depend on the parametrization. Velocity, speed and acceleration *do*. Think of the curve as a road and the parametrization as a way of driving along it: the length and curvature of the road do not depend on how you travel, but your velocity and acceleration do.

^rem-104-1

> [!example] Example §122.1: Velocity, Speed and Acceleration
> **(a)** An object in the plane has position $\mathbf{r}(t) = t^3\,\mathbf{i} + t^2\,\mathbf{j}$. Then
>
> $$
> \mathbf{v}(t) = 3t^2\,\mathbf{i} + 2t\,\mathbf{j}, \qquad \mathbf{a}(t) = 6t\,\mathbf{i} + 2\,\mathbf{j}, \qquad |\mathbf{v}(t)| = \sqrt{9t^4 + 4t^2} .
> $$
>
> At $t = 1$: $\mathbf{v}(1) = 3\mathbf{i} + 2\mathbf{j}$, $\mathbf{a}(1) = 6\mathbf{i} + 2\mathbf{j}$, $|\mathbf{v}(1)| = \sqrt{13}$. Drawn at the point $(1, 1)$, the velocity is tangent to the curve and the acceleration points toward the side to which the path bends.
>
> **(b)** $\mathbf{r}(t) = \langle t^2, e^t, te^t \rangle$: $\mathbf{v}(t) = \langle 2t, e^t, (1 + t)e^t \rangle$, $\mathbf{a}(t) = \langle 2, e^t, (2 + t)e^t \rangle$, and $|\mathbf{v}(t)| = \sqrt{4t^2 + e^{2t} + (1 + t)^2e^{2t}}$.
>
> **(c)** $\mathbf{r}(t) = t\ln t\,\mathbf{i} + t\,\mathbf{j} + e^{-t}\,\mathbf{k}$: $\mathbf{v}(t) = \langle \ln t + 1, 1, -e^{-t} \rangle$, $|\mathbf{v}(t)| = \sqrt{(1 + \ln t)^2 + 1 + e^{-2t}}$, $\mathbf{a}(t) = \langle 1/t, 0, e^{-t} \rangle$.
>
> **(d)** $\mathbf{r}(t) = 2t\,\mathbf{i} + (t^2 - 6)\,\mathbf{j} - \frac13 t^3\,\mathbf{k}$: $\mathbf{v}(t) = \langle 2, 2t, -t^2 \rangle$ and $|\mathbf{v}(t)| = \sqrt{4 + 4t^2 + t^4} = \sqrt{(t^2 + 2)^2} = t^2 + 2$. Similarly, $\mathbf{r}(t) = \langle t^2, t\sqrt2, \frac12\ln t \rangle$ has $\mathbf{v} = \big\langle 2t, \sqrt2, \frac{1}{2t} \big\rangle$, $\mathbf{a} = \big\langle 2, 0, -\frac{1}{2t^2} \big\rangle$ and speed $2t + \frac{1}{2t}$ ([[§102 Arc Length and Curvature#^ex-102-2|Example §102.2]]).
>
> *Stewart: Examples 13.4.1 and 13.4.2*
> *Source: 233 Exam 1 Review, Q15; 233 Midterm 1 Practice Questions, Q14(b); 233 Practice Exam 1, Q3(a)*

^ex-104-1

> [!theorem] Proposition §104.2: Velocity and Position from Acceleration
> If $\mathbf{a}$ and $\mathbf{v}$ are continuous, then
>
> $$
> \mathbf{v}(t) = \mathbf{v}(t_0) + \int_{t_0}^t \mathbf{a}(u)\,du, \qquad \mathbf{r}(t) = \mathbf{r}(t_0) + \int_{t_0}^t \mathbf{v}(u)\,du .
> $$
>
> *Stewart: 13.4 (text)*

^prop-104-2

> [!proof]+ Proof
> $\mathbf{v}$ is an antiderivative of $\mathbf{a}$ and $\mathbf{r}$ an antiderivative of $\mathbf{v}$ ([[§104 Motion in Space꞉ Velocity and Acceleration#^def-104-1|Definition §104.1]], [[§104 Motion in Space꞉ Velocity and Acceleration#^def-104-3|Definition §104.3]]). By the Fundamental Theorem of Calculus for vector functions ([[§101 Derivatives and Integrals of Vector Functions#^thm-101-5|Theorem §101.5]]), $\int_{t_0}^t \mathbf{a}(u)\,du = \mathbf{v}(t) - \mathbf{v}(t_0)$ and $\int_{t_0}^t \mathbf{v}(u)\,du = \mathbf{r}(t) - \mathbf{r}(t_0)$.

^pf-104-2

*Uses:* [[§104 Motion in Space꞉ Velocity and Acceleration#^def-104-1|Def. §104.1]], [[§104 Motion in Space꞉ Velocity and Acceleration#^def-104-3|Def. §104.3]], [[§101 Derivatives and Integrals of Vector Functions#^thm-101-5|§101.5]]

> [!example] Example §122.2: From Acceleration to Position
> A particle starts at $\mathbf{r}(0) = \langle 1, 0, 0 \rangle$ with initial velocity $\mathbf{v}(0) = \mathbf{i} - \mathbf{j} + \mathbf{k}$, and its acceleration is $\mathbf{a}(t) = 4t\,\mathbf{i} + 6t\,\mathbf{j} + \mathbf{k}$. Find its velocity and position at time $t$.
>
> Since $\mathbf{v}' = \mathbf{a}$,
>
> $$
> \mathbf{v}(t) = \int (4t\,\mathbf{i} + 6t\,\mathbf{j} + \mathbf{k})\,dt = 2t^2\,\mathbf{i} + 3t^2\,\mathbf{j} + t\,\mathbf{k} + \mathbf{C} .
> $$
>
> At $t = 0$ this gives $\mathbf{v}(0) = \mathbf{C}$, so $\mathbf{C} = \mathbf{i} - \mathbf{j} + \mathbf{k}$ and
>
> $$
> \mathbf{v}(t) = (2t^2 + 1)\,\mathbf{i} + (3t^2 - 1)\,\mathbf{j} + (t + 1)\,\mathbf{k} .
> $$
>
> Since $\mathbf{r}' = \mathbf{v}$,
>
> $$
> \mathbf{r}(t) = \big(\tfrac23 t^3 + t\big)\,\mathbf{i} + (t^3 - t)\,\mathbf{j} + \big(\tfrac12 t^2 + t\big)\,\mathbf{k} + \mathbf{D} ,
> $$
>
> and $t = 0$ gives $\mathbf{D} = \mathbf{r}(0) = \mathbf{i}$. So
>
> $$
> \mathbf{r}(t) = \big(\tfrac23 t^3 + t + 1\big)\,\mathbf{i} + (t^3 - t)\,\mathbf{j} + \big(\tfrac12 t^2 + t\big)\,\mathbf{k} .
> $$
>
> *Stewart: Example 13.4.3*

^ex-104-2

> [!remark] Remark: Newton's Second Law of Motion
> If the force acting on a particle is known, its acceleration follows from **Newton's Second Law of Motion**, a law of physics taken here as given. In vector form: if at any time $t$ a force $\mathbf{F}(t)$ acts on an object of mass $m$ producing an acceleration $\mathbf{a}(t)$, then
>
> $$
> \mathbf{F}(t) = m\,\mathbf{a}(t) .
> $$

^rem-104-2

> [!example] Example §122.3: Centripetal Force
> An object of mass $m$ moves on a circular path with constant angular speed $\omega$, with position $\mathbf{r}(t) = a\cos\omega t\,\mathbf{i} + a\sin\omega t\,\mathbf{j}$. Find the force acting on it and show that it is directed toward the origin.
>
> $$
> \mathbf{v}(t) = \mathbf{r}'(t) = -a\omega\sin\omega t\,\mathbf{i} + a\omega\cos\omega t\,\mathbf{j}, \qquad \mathbf{a}(t) = \mathbf{v}'(t) = -a\omega^2\cos\omega t\,\mathbf{i} - a\omega^2\sin\omega t\,\mathbf{j} .
> $$
>
> By Newton's Second Law, $\mathbf{F}(t) = m\,\mathbf{a}(t) = -m\omega^2(a\cos\omega t\,\mathbf{i} + a\sin\omega t\,\mathbf{j}) = -m\omega^2\,\mathbf{r}(t)$. The force points opposite to the radius vector $\mathbf{r}(t)$, toward the origin: a **centripetal** (center-seeking) force. (Here $\omega = d\theta/dt$, where $\theta$ is the polar angle of the object.)
>
> *Stewart: Example 13.4.4*

^ex-104-3

## Projectile Motion

> [!theorem] Proposition §104.3: Projectile Motion
> A projectile is fired from the origin with angle of elevation $\alpha$ and initial velocity $\mathbf{v}_0$, with initial speed $v_0 = |\mathbf{v}_0|$. Assume air resistance is negligible and the only external force is gravity, $\mathbf{F} = -mg\,\mathbf{j}$ (with $g \approx 9.8$ m/s$^2$). Then its position is
>
> $$
> \mathbf{r}(t) = -\tfrac12 g t^2\,\mathbf{j} + t\,\mathbf{v}_0 , \qquad (3)
> $$
>
> with parametric equations
>
> $$
> x = (v_0\cos\alpha)\,t, \qquad y = (v_0\sin\alpha)\,t - \tfrac12 g t^2 . \qquad (4)
> $$
>
> The path is part of a parabola, and the range (horizontal distance traveled back to ground level) is $d = \dfrac{v_0^2\sin 2\alpha}{g}$, which is largest for $\alpha = 45^\circ$.
>
> *Stewart: Example 13.4.5, Equations 3 and 4*

^prop-104-3

> [!proof]+ Proof
> By Newton's Second Law, $m\mathbf{a} = -mg\,\mathbf{j}$, so $\mathbf{a} = -g\,\mathbf{j}$. Integrating ([[§104 Motion in Space꞉ Velocity and Acceleration#^prop-104-2|Proposition §104.2]]), $\mathbf{v}(t) = -gt\,\mathbf{j} + \mathbf{C}$ with $\mathbf{C} = \mathbf{v}(0) = \mathbf{v}_0$, so $\mathbf{r}'(t) = -gt\,\mathbf{j} + \mathbf{v}_0$. Integrating again, $\mathbf{r}(t) = -\frac12 gt^2\,\mathbf{j} + t\,\mathbf{v}_0 + \mathbf{D}$ with $\mathbf{D} = \mathbf{r}(0) = \mathbf{0}$. This is (3). Writing $\mathbf{v}_0 = v_0\cos\alpha\,\mathbf{i} + v_0\sin\alpha\,\mathbf{j}$,
>
> $$
> \mathbf{r}(t) = (v_0\cos\alpha)\,t\,\mathbf{i} + \big[(v_0\sin\alpha)\,t - \tfrac12 gt^2\big]\,\mathbf{j} ,
> $$
>
> which is (4). Eliminating $t = x/(v_0\cos\alpha)$ (for $\alpha \ne 90^\circ$) makes $y$ a quadratic function of $x$, so the path is part of a parabola. The projectile is back at ground level when $y = 0$, that is, $t = 0$ or $t = (2v_0\sin\alpha)/g$; the second value gives
>
> $$
> d = (v_0\cos\alpha)\,\frac{2v_0\sin\alpha}{g} = \frac{v_0^2(2\sin\alpha\cos\alpha)}{g} = \frac{v_0^2\sin 2\alpha}{g} ,
> $$
>
> which is largest when $\sin 2\alpha = 1$, that is, $\alpha = 45^\circ$.

^pf-104-3

*Uses:* [[§104 Motion in Space꞉ Velocity and Acceleration#^prop-104-2|§104.2]], Newton's Second Law ([[§104 Motion in Space꞉ Velocity and Acceleration#^rem-104-2|Remark]])

> [!remark] Remark: Method — Projectile Problems
> 1. Choose axes: origin at ground level below the launch point, $\mathbf{j}$ up. Then $\mathbf{a} = -g\,\mathbf{j}$ (use the value of $g$ the problem gives: $9.8$ m/s$^2$, $10$ m/s$^2$, or $32$ ft/s$^2$).
> 2. Write $\mathbf{v}(0) = v_0\langle \cos\alpha, \sin\alpha \rangle$ and $\mathbf{r}(0) = \langle 0, h \rangle$ for a launch height $h$; integrate twice: $\mathbf{v}(t) = \langle v_0\cos\alpha,\ v_0\sin\alpha - gt \rangle$, $\mathbf{r}(t) = \langle (v_0\cos\alpha)t,\ h + (v_0\sin\alpha)t - \frac12 gt^2 \rangle$.
> 3. Highest point: the vertical velocity is $0$. Landing: $y(t) = 0$, the positive root of the quadratic. Range: $x$ at landing. Impact speed: $|\mathbf{v}|$ at landing.

^rem-104-3

> [!example] Example §122.4: Projectiles Launched Above the Ground
> **(a)** A projectile is fired with initial speed $150$ m/s and angle of elevation $30^\circ$ from a position $10$ m above ground level. Where does it hit the ground, and with what speed?
>
> With the origin at ground level the initial position is $(0, 10)$, so we add $10$ to $y$ in (4). With $v_0 = 150$, $\alpha = 30^\circ$, $g = 9.8$:
>
> $$
> x = 150\cos(30^\circ)\,t = 75\sqrt3\,t, \qquad y = 10 + 150\sin(30^\circ)\,t - \tfrac12(9.8)t^2 = 10 + 75t - 4.9t^2 .
> $$
>
> Impact occurs when $4.9t^2 - 75t - 10 = 0$; the positive root is
>
> $$
> t = \frac{75 + \sqrt{5625 + 196}}{9.8} \approx 15.44 .
> $$
>
> Then $x \approx 75\sqrt3\,(15.44) \approx 2006$, so the projectile lands about $2006$ m away. Its velocity is $\mathbf{v}(t) = 75\sqrt3\,\mathbf{i} + (75 - 9.8t)\,\mathbf{j}$, so the impact speed is
>
> $$
> |\mathbf{v}(15.44)| = \sqrt{(75\sqrt3)^2 + (75 - 9.8 \cdot 15.44)^2} \approx 151\ \text{m/s} .
> $$
>
> **(b)** A basketball is thrown at $45^\circ$ with initial speed $12$ m/s from $2$ m above the ground, with $g = 10$ m/s$^2$. Find $\mathbf{v}(t)$, $\mathbf{r}(t)$, the time $T$ of the highest point and the speed there.
>
> $\mathbf{v}(0) = 12\langle \cos 45^\circ, \sin 45^\circ \rangle = \langle 6\sqrt2, 6\sqrt2 \rangle$, $\mathbf{r}(0) = \langle 0, 2 \rangle$ and $\mathbf{a} = \langle 0, -10 \rangle$, so
>
> $$
> \mathbf{v}(t) = \langle 6\sqrt2,\ 6\sqrt2 - 10t \rangle, \qquad \mathbf{r}(t) = \langle 6\sqrt2\,t,\ 2 + 6\sqrt2\,t - 5t^2 \rangle .
> $$
>
> At the highest point the vertical velocity vanishes: $6\sqrt2 - 10T = 0$, so $T = \dfrac{3\sqrt2}{5}$ s. There $\mathbf{v}(T) = \langle 6\sqrt2, 0 \rangle$, and the speed is $6\sqrt2$ m/s, the horizontal component, which never changes.
>
> *The posted answer gives $\mathbf{r}(t) = \langle 6\sqrt2, 2 + 6\sqrt2\,t - 5t^2 \rangle$, without the factor $t$ in the first component, and does not state $\mathbf{v}(t)$.*
>
> **(c)** A projectile is fired from $5$ m above the ground at $30^\circ$ with initial speed $100$ m/s. Then $\mathbf{v}(0) = 50\sqrt3\,\mathbf{i} + 50\,\mathbf{j}$, $\mathbf{r}(0) = 5\,\mathbf{j}$, and $\mathbf{r}(t) = 50\sqrt3\,t\,\mathbf{i} + \big(5 + 50t - \frac12 gt^2\big)\mathbf{j}$. It hits the ground at the positive root of $\frac12 gt^2 - 50t - 5 = 0$,
>
> $$
> t = \frac{50 + \sqrt{2500 + 10g}}{g} \quad\Big(= \frac{100 + \sqrt{100^2 + 40g}}{2g}\Big) \approx 10.30\ \text{s for } g = 9.8 ,
> $$
>
> after traveling $50\sqrt3\,t \approx 892$ m horizontally.
>
> *Stewart: Example 13.4.6*
> *Source: 233 Midterm 1 Practice Questions, Q21; 233 Practice Exam 1, Q6*

^ex-104-4

## Tangential and Normal Components of Acceleration

> [!theorem] Theorem §104.4: Tangential and Normal Components of Acceleration
> Let $v = |\mathbf{v}|$ be the speed of a particle moving along a smooth curve, and $\mathbf{T}$, $\mathbf{N}$, $\kappa$ the unit tangent, unit normal and curvature ([[§101 Derivatives and Integrals of Vector Functions#^def-101-4|Definition §101.4]], [[§103 The TNB Frame and Torsion#^def-103-1|Definition §103.1]], [[§102 Arc Length and Curvature#^def-102-4|Definition §102.4]]). Then
>
> $$
> \mathbf{a} = v'\,\mathbf{T} + \kappa v^2\,\mathbf{N} . \qquad (7)
> $$
>
> That is, $\mathbf{a} = a_T\,\mathbf{T} + a_N\,\mathbf{N}$ with **tangential component** $a_T = v'$ and **normal component** $a_N = \kappa v^2$.
>
> *Stewart: 13.4, Equations 7 and 8*

^thm-104-4

> [!proof]+ Proof
> Since $\mathbf{T}(t) = \dfrac{\mathbf{r}'(t)}{|\mathbf{r}'(t)|} = \dfrac{\mathbf{v}(t)}{|\mathbf{v}(t)|} = \dfrac{\mathbf{v}}{v}$, we have $\mathbf{v} = v\mathbf{T}$. Differentiating with the Product Rule ([[§101 Derivatives and Integrals of Vector Functions#^thm-101-2|Theorem §101.2]], Formula 3),
>
> $$
> \mathbf{a} = \mathbf{v}' = v'\,\mathbf{T} + v\,\mathbf{T}' . \qquad (5)
> $$
>
> By [[§102 Arc Length and Curvature#^prop-102-3|Proposition §102.3]], $\kappa = \dfrac{|\mathbf{T}'|}{|\mathbf{r}'|} = \dfrac{|\mathbf{T}'|}{v}$, so $|\mathbf{T}'| = \kappa v$. (6) Since $\mathbf{N} = \mathbf{T}'/|\mathbf{T}'|$ ([[§103 The TNB Frame and Torsion#^def-103-1|Definition §103.1]]), $\mathbf{T}' = |\mathbf{T}'|\,\mathbf{N} = \kappa v\,\mathbf{N}$. (Where $\kappa = 0$, $\mathbf{T}' = \mathbf{0}$ and the second term vanishes whatever $\mathbf{N}$ is.) Substituting into (5) gives (7).

^pf-104-4

*Uses:* [[§101 Derivatives and Integrals of Vector Functions#^thm-101-2|§101.2]], [[§102 Arc Length and Curvature#^prop-102-3|§102.3]], [[§103 The TNB Frame and Torsion#^def-103-1|Def. §103.1]]

![[m233-89-1.svg]]
*[[§104 Motion in Space꞉ Velocity and Acceleration#^thm-104-4|Theorem §104.4]]: the acceleration $\mathbf{a}$ (red) splits into a component $a_T\mathbf{T}$ along the direction of motion and a component $a_N\mathbf{N}$ toward the inside of the bend (green); there is no $\mathbf{B}$-component. The tangential part changes the speed, $a_T = v'$; the normal part turns the direction, $a_N = \kappa v^2$.*

> [!remark] Remark: What Formula 7 Says
> The binormal $\mathbf{B}$ is absent: however an object moves through space, its acceleration lies in the plane of $\mathbf{T}$ and $\mathbf{N}$, the osculating plane. The tangential component $v'$ is the rate of change of speed. The normal component $\kappa v^2$ is curvature times the square of the speed: a passenger in a car taking a sharp turn (large $\kappa$) is thrown against the door, and taking it at high speed has the same effect; doubling the speed multiplies $a_N$ by $4$.

^rem-104-4

> [!theorem] Theorem §104.5: Formulas for the Components of Acceleration
> In terms of $\mathbf{r}$, $\mathbf{r}'$ and $\mathbf{r}''$,
>
> $$
> a_T = \frac{\mathbf{r}'(t) \cdot \mathbf{r}''(t)}{|\mathbf{r}'(t)|}, \qquad a_N = \frac{|\mathbf{r}'(t) \times \mathbf{r}''(t)|}{|\mathbf{r}'(t)|} .
> $$
>
> *Stewart: 13.4, Equations 9 and 10*

^thm-104-5

> [!proof]+ Proof
> Take the dot product of $\mathbf{v} = v\mathbf{T}$ with (7):
>
> $$
> \mathbf{v} \cdot \mathbf{a} = v\mathbf{T} \cdot (v'\,\mathbf{T} + \kappa v^2\,\mathbf{N}) = vv'\,\mathbf{T} \cdot \mathbf{T} + \kappa v^3\,\mathbf{T} \cdot \mathbf{N} = vv' ,
> $$
>
> since $\mathbf{T} \cdot \mathbf{T} = 1$ and $\mathbf{T} \cdot \mathbf{N} = 0$. Therefore $a_T = v' = \dfrac{\mathbf{v} \cdot \mathbf{a}}{v} = \dfrac{\mathbf{r}' \cdot \mathbf{r}''}{|\mathbf{r}'|}$. By [[§102 Arc Length and Curvature#^thm-102-4|Theorem §102.4]],
>
> $$
> a_N = \kappa v^2 = \frac{|\mathbf{r}' \times \mathbf{r}''|}{|\mathbf{r}'|^3}\,|\mathbf{r}'|^2 = \frac{|\mathbf{r}' \times \mathbf{r}''|}{|\mathbf{r}'|} .
> $$

^pf-104-5

*Uses:* [[§104 Motion in Space꞉ Velocity and Acceleration#^thm-104-4|§104.4]], [[§102 Arc Length and Curvature#^thm-102-4|§102.4]], [[§103 The TNB Frame and Torsion#^def-103-1|Def. §103.1]]

> [!example] Example §122.5: Components of Acceleration
> A particle moves with position $\mathbf{r}(t) = \langle t^2, t^2, t^3 \rangle$. Find the tangential and normal components of acceleration.
>
> $$
> \mathbf{r}'(t) = 2t\,\mathbf{i} + 2t\,\mathbf{j} + 3t^2\,\mathbf{k}, \qquad \mathbf{r}''(t) = 2\,\mathbf{i} + 2\,\mathbf{j} + 6t\,\mathbf{k}, \qquad |\mathbf{r}'(t)| = \sqrt{8t^2 + 9t^4} .
> $$
>
> By [[§104 Motion in Space꞉ Velocity and Acceleration#^thm-104-5|Theorem §104.5]],
>
> $$
> a_T = \frac{\mathbf{r}' \cdot \mathbf{r}''}{|\mathbf{r}'|} = \frac{4t + 4t + 18t^3}{\sqrt{8t^2 + 9t^4}} = \frac{8t + 18t^3}{\sqrt{8t^2 + 9t^4}} .
> $$
>
> Since
>
> $$
> \mathbf{r}' \times \mathbf{r}'' = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 2t & 2t & 3t^2 \\ 2 & 2 & 6t \end{vmatrix} = (12t^2 - 6t^2)\,\mathbf{i} - (12t^2 - 6t^2)\,\mathbf{j} + (4t - 4t)\,\mathbf{k} = 6t^2\,\mathbf{i} - 6t^2\,\mathbf{j} ,
> $$
>
> $|\mathbf{r}' \times \mathbf{r}''| = 6\sqrt2\,t^2$, and
>
> $$
> a_N = \frac{|\mathbf{r}' \times \mathbf{r}''|}{|\mathbf{r}'|} = \frac{6\sqrt2\,t^2}{\sqrt{8t^2 + 9t^4}} .
> $$
>
> *Stewart: Example 13.4.7*

^ex-104-5

## Kepler's Laws of Planetary Motion

> [!theorem] Theorem §104.6: Kepler's Laws
> 1. A planet revolves around the sun in an elliptical orbit with the sun at one focus.
> 2. The line joining the sun to a planet sweeps out equal areas in equal times.
> 3. The square of the period of revolution of a planet is proportional to the cube of the length of the major axis of its orbit.
>
> These are consequences of Newton's Second Law of Motion and his Law of Universal Gravitation.
>
> *Stewart: 13.4, Kepler's Laws*

^thm-104-6

*Stewart proves the First Law below; the Second and Third Laws are derived in the Applied Project following the section.*

> [!proof]- Proof of Kepler's First Law
> Ignore all bodies except the sun and one planet, put the sun at the origin, and let $\mathbf{r} = \mathbf{r}(t)$ be the position of the planet, $\mathbf{v} = \mathbf{r}'$, $\mathbf{a} = \mathbf{r}''$. Newton's laws give
>
> $$
> \mathbf{F} = m\mathbf{a} \quad\text{(Second Law)}, \qquad \mathbf{F} = -\frac{GMm}{r^3}\,\mathbf{r} = -\frac{GMm}{r^2}\,\mathbf{u} \quad\text{(Gravitation)},
> $$
>
> where $m$ and $M$ are the masses of the planet and the sun, $G$ is the gravitational constant, $r = |\mathbf{r}|$, and $\mathbf{u} = (1/r)\mathbf{r}$ is the unit vector in the direction of $\mathbf{r}$.
>
> **The orbit is planar.** Equating the two expressions for $\mathbf{F}$ gives $\mathbf{a} = -\dfrac{GM}{r^3}\,\mathbf{r}$, so $\mathbf{a}$ is parallel to $\mathbf{r}$ and $\mathbf{r} \times \mathbf{a} = \mathbf{0}$. By Formula 5 of [[§101 Derivatives and Integrals of Vector Functions#^thm-101-2|Theorem §101.2]],
>
> $$
> \frac{d}{dt}(\mathbf{r} \times \mathbf{v}) = \mathbf{r}' \times \mathbf{v} + \mathbf{r} \times \mathbf{v}' = \mathbf{v} \times \mathbf{v} + \mathbf{r} \times \mathbf{a} = \mathbf{0} + \mathbf{0} = \mathbf{0} .
> $$
>
> Therefore $\mathbf{r} \times \mathbf{v} = \mathbf{h}$ for a constant vector $\mathbf{h}$ (each component has derivative $0$, so is constant by [[§29 Rolle's Theorem and the Mean Value Theorem#^thm-29-3|Theorem §29.3]]). Assume $\mathbf{h} \ne \mathbf{0}$, that is, $\mathbf{r}$ and $\mathbf{v}$ are not parallel. Then $\mathbf{r}(t) \perp \mathbf{h}$ for all $t$ ([[§96 The Cross Product#^thm-96-2|Theorem §96.2]]), so the planet always lies in the plane through the origin perpendicular to $\mathbf{h}$.
>
> **Rewriting h.** With $\mathbf{r} = r\mathbf{u}$ and the Product Rule,
>
> $$
> \mathbf{h} = \mathbf{r} \times \mathbf{r}' = r\mathbf{u} \times (r\mathbf{u})' = r\mathbf{u} \times (r\mathbf{u}' + r'\mathbf{u}) = r^2(\mathbf{u} \times \mathbf{u}') + rr'(\mathbf{u} \times \mathbf{u}) = r^2(\mathbf{u} \times \mathbf{u}') .
> $$
>
> **Integrating $\mathbf{v} \times \mathbf{h}$.** Then, using Property 6 of [[§96 The Cross Product#^thm-96-8|Theorem §96.8]],
>
> $$
> \mathbf{a} \times \mathbf{h} = \frac{-GM}{r^2}\,\mathbf{u} \times \big(r^2\,\mathbf{u} \times \mathbf{u}'\big) = -GM\,\mathbf{u} \times (\mathbf{u} \times \mathbf{u}') = -GM\big[(\mathbf{u} \cdot \mathbf{u}')\,\mathbf{u} - (\mathbf{u} \cdot \mathbf{u})\,\mathbf{u}'\big] .
> $$
>
> But $\mathbf{u} \cdot \mathbf{u} = |\mathbf{u}|^2 = 1$, and since $|\mathbf{u}(t)| = 1$, $\mathbf{u} \cdot \mathbf{u}' = 0$ ([[§101 Derivatives and Integrals of Vector Functions#^thm-101-3|Theorem §101.3]]). So $\mathbf{a} \times \mathbf{h} = GM\,\mathbf{u}'$, and since $\mathbf{h}$ is constant,
>
> $$
> (\mathbf{v} \times \mathbf{h})' = \mathbf{v}' \times \mathbf{h} + \mathbf{v} \times \mathbf{h}' = \mathbf{a} \times \mathbf{h} = GM\,\mathbf{u}' .
> $$
>
> Integrating both sides (that is, $\mathbf{v} \times \mathbf{h} - GM\,\mathbf{u}$ has derivative $\mathbf{0}$, so it is constant),
>
> $$
> \mathbf{v} \times \mathbf{h} = GM\,\mathbf{u} + \mathbf{c} \qquad (11)
> $$
>
> for a constant vector $\mathbf{c}$.
>
> **Choosing axes.** Choose coordinates so that $\mathbf{k}$ points in the direction of $\mathbf{h}$; the planet then moves in the $xy$-plane. Both $\mathbf{v} \times \mathbf{h}$ and $\mathbf{u}$ are perpendicular to $\mathbf{h}$, so (11) shows that $\mathbf{c}$ lies in the $xy$-plane, and we may choose the $x$- and $y$-axes so that $\mathbf{i}$ points in the direction of $\mathbf{c}$. If $\theta$ is the angle between $\mathbf{c}$ and $\mathbf{r}$, then $(r, \theta)$ are polar coordinates of the planet.
>
> **The polar equation.** From (11),
>
> $$
> \mathbf{r} \cdot (\mathbf{v} \times \mathbf{h}) = \mathbf{r} \cdot (GM\,\mathbf{u} + \mathbf{c}) = GM\,r\,\mathbf{u} \cdot \mathbf{u} + |\mathbf{r}|\,|\mathbf{c}|\cos\theta = GMr + rc\cos\theta ,
> $$
>
> where $c = |\mathbf{c}|$. Hence, with $e = c/(GM)$,
>
> $$
> r = \frac{\mathbf{r} \cdot (\mathbf{v} \times \mathbf{h})}{GM + c\cos\theta} = \frac{1}{GM}\,\frac{\mathbf{r} \cdot (\mathbf{v} \times \mathbf{h})}{1 + e\cos\theta} .
> $$
>
> By Property 5 of [[§96 The Cross Product#^thm-96-8|Theorem §96.8]], $\mathbf{r} \cdot (\mathbf{v} \times \mathbf{h}) = (\mathbf{r} \times \mathbf{v}) \cdot \mathbf{h} = \mathbf{h} \cdot \mathbf{h} = h^2$, where $h = |\mathbf{h}|$. So
>
> $$
> r = \frac{h^2/(GM)}{1 + e\cos\theta} = \frac{eh^2/c}{1 + e\cos\theta}, \qquad\text{and with } d = h^2/c, \qquad r = \frac{ed}{1 + e\cos\theta} . \qquad (12)
> $$
>
> If $\mathbf{c} \ne \mathbf{0}$, then $d > 0$ and by the polar equation of conics ([[§78 Conic Sections in Polar Coordinates#^thm-78-3|Theorem §78.3]]; Stewart's Theorem 10.6.6), (12) is a conic section with focus at the origin and eccentricity $e$. (If $\mathbf{c} = \mathbf{0}$, then $GMr = \mathbf{r} \cdot (\mathbf{v} \times \mathbf{h}) = h^2$, so $r = h^2/(GM)$ is constant: a circle centered at the sun, the case $e = 0$.) The orbit of a planet is a closed curve, and of the conics only the ellipse is closed, so $e < 1$ and the orbit is an ellipse with the sun at a focus.

^pf-104-6

*Uses:* [[§101 Derivatives and Integrals of Vector Functions#^thm-101-2|§101.2]], [[§101 Derivatives and Integrals of Vector Functions#^thm-101-3|§101.3]], [[§96 The Cross Product#^thm-96-2|§96.2]], [[§96 The Cross Product#^thm-96-8|§96.8]], [[§78 Conic Sections in Polar Coordinates#^thm-78-3|§78.3]], [[§29 Rolle's Theorem and the Mean Value Theorem#^thm-29-3|§29.3]]

> [!remark] Remark: What the Proof Uses
> The proof uses only the vector calculus of Chapters 12 and 13: the product rule for cross products, a constant-length vector being perpendicular to its derivative, and the two triple-product identities. The constant $\mathbf{h} = \mathbf{r} \times \mathbf{v}$ is the angular momentum per unit mass, and its constancy is exactly what the Second Law (equal areas in equal times) expresses. The same argument applies to a moon or satellite moving around a planet, or a comet around a star.

^rem-104-5
