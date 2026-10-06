---
type: section
subject: "[[Calculus]]"
chapter: 13
section: 100
stewart: "13.1"
aliases: ["Stewart 13.1"]
tags: [calculus, math233]
---
← [[§99 Cylinders and Quadric Surfaces]] · ↑ [[· 13 Vector Functions]] · [[§101 Derivatives and Integrals of Vector Functions]] →

*Stewart, Section 13.1 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q14(a), Q17, Q18, Q19, Q20), Exam 1 Review (Q10(a)–(b), Q11).*

A vector function assigns to each number $t$ a vector $\mathbf{r}(t) = \langle f(t), g(t), h(t) \rangle$. As $t$ varies, the tip of $\mathbf{r}(t)$ traces a curve in space, so vector functions are the natural way to describe the path of a moving particle. Limits and continuity are defined component by component, which reduces them to one-variable calculus. The section then goes in both directions between formulas and pictures: recognizing the curve of a given vector function (a line, a helix), and finding a vector function for a given curve, such as a segment or the intersection of two surfaces. Chapter 13 develops the calculus of these curves: tangent vectors in [[§101 Derivatives and Integrals of Vector Functions|§101]], length and curvature in [[§102 Arc Length and Curvature|§102]], velocity and acceleration in [[§104 Motion in Space꞉ Velocity and Acceleration|§104]].

## Vector-Valued Functions

> [!definition] Definition §100.1: Vector Function
> A **vector-valued function**, or **vector function**, is a function whose domain is a set of real numbers and whose range is a set of vectors. For a vector function $\mathbf{r}$ with values in $V_3$, each number $t$ in the domain is assigned a unique vector $\mathbf{r}(t)$. If $f(t)$, $g(t)$, $h(t)$ are the components of $\mathbf{r}(t)$, the real-valued functions $f$, $g$, $h$ are the **component functions** of $\mathbf{r}$, and
>
> $$
> \mathbf{r}(t) = \langle f(t), g(t), h(t) \rangle = f(t)\,\mathbf{i} + g(t)\,\mathbf{j} + h(t)\,\mathbf{k} .
> $$
>
> By the usual convention, the domain of $\mathbf{r}$ is the set of all $t$ for which the expression for $\mathbf{r}(t)$ is defined, that is, the intersection of the domains of the component functions. The letter $t$ is used because it represents time in most applications.
>
> *Stewart: 13.1 (text)*

^def-100-1

## Limits and Continuity

> [!definition] Definition §100.2: Limit of a Vector Function
> If $\mathbf{r}(t) = \langle f(t), g(t), h(t) \rangle$, then
>
> $$
> \lim_{t \to a} \mathbf{r}(t) = \Big\langle \lim_{t \to a} f(t),\ \lim_{t \to a} g(t),\ \lim_{t \to a} h(t) \Big\rangle ,
> $$
>
> provided the limits of the component functions exist.
>
> *Stewart: 13.1, Definition 1*

^def-100-2

> [!remark]- Connections
> - Stewart notes (Exercise 62) that this is equivalent to the $\varepsilon$–$\delta$ condition: for every $\varepsilon > 0$ there is $\delta > 0$ with $|\mathbf{r}(t) - \mathbf{L}| < \varepsilon$ whenever $0 < |t - a| < \delta$. That is the definition of a limit with the Euclidean distance on the target, as in [[§3 Continuity and Limits of Functions#^def-3-2|452 Def. §3.2]] and [[§1 Sequences and Limits in ℝⁿ#^def-1-1|452 Def. §1.1]]. Since each $|r_i - L_i| \le |\mathbf{r} - \mathbf{L}| \le |r_1 - L_1| + |r_2 - L_2| + |r_3 - L_3|$, convergence of the vector is the same as convergence of each component. Geometrically, the length and direction of $\mathbf{r}(t)$ approach those of $\mathbf{L}$.

> [!theorem] Theorem §100.1: Limit Laws for Vector Functions
> Suppose $\mathbf{u}$ and $\mathbf{v}$ have limits as $t \to a$, and $c$ is a constant. Then
>
> $$
> \begin{aligned}
> &\lim_{t \to a}[\mathbf{u}(t) + \mathbf{v}(t)] = \lim_{t \to a}\mathbf{u}(t) + \lim_{t \to a}\mathbf{v}(t), &\qquad &\lim_{t \to a} c\,\mathbf{u}(t) = c\lim_{t \to a}\mathbf{u}(t), \\
> &\lim_{t \to a}[\mathbf{u}(t) \cdot \mathbf{v}(t)] = \lim_{t \to a}\mathbf{u}(t) \cdot \lim_{t \to a}\mathbf{v}(t), &\qquad &\lim_{t \to a}[\mathbf{u}(t) \times \mathbf{v}(t)] = \lim_{t \to a}\mathbf{u}(t) \times \lim_{t \to a}\mathbf{v}(t) .
> \end{aligned}
> $$
>
> *Stewart: 13.1 (text; Exercise 61)*

^thm-100-1

> [!proof]+ Proof
> Stewart states that "limits of vector functions obey the same rules as limits of real-valued functions" and leaves the proof as an exercise. Write $\mathbf{u} = \langle u_1, u_2, u_3 \rangle$, $\mathbf{v} = \langle v_1, v_2, v_3 \rangle$, and $\lim_{t \to a} u_i(t) = p_i$, $\lim_{t \to a} v_i(t) = q_i$, which exist by [[§100 Vector Functions and Space Curves#^def-100-2|Definition §100.2]]. Each component of $\mathbf{u} + \mathbf{v}$, $c\mathbf{u}$, $\mathbf{u} \cdot \mathbf{v}$ and $\mathbf{u} \times \mathbf{v}$ is a sum of constant multiples of $u_i$, $v_j$ or of products $u_iv_j$. For instance, $\mathbf{u} \cdot \mathbf{v} = u_1v_1 + u_2v_2 + u_3v_3$, and the first component of $\mathbf{u} \times \mathbf{v}$ is $u_2v_3 - u_3v_2$. By the Sum, Constant Multiple and Product Laws for real-valued limits ([[§9 Calculating Limits Using the Limit Laws#^thm-9-1|Theorem §9.1]]),
>
> $$
> \lim_{t \to a}(u_1v_1 + u_2v_2 + u_3v_3) = p_1q_1 + p_2q_2 + p_3q_3, \qquad \lim_{t \to a}(u_2v_3 - u_3v_2) = p_2q_3 - p_3q_2 ,
> $$
>
> which are $\langle p_1, p_2, p_3 \rangle \cdot \langle q_1, q_2, q_3 \rangle$ and the first component of $\langle p_1, p_2, p_3 \rangle \times \langle q_1, q_2, q_3 \rangle$. The remaining components and the other two laws are the same computation.

^pf-100-1

*Uses:* [[§100 Vector Functions and Space Curves#^def-100-2|Def. §100.2]], [[§9 Calculating Limits Using the Limit Laws#^thm-9-1|§9.1]], [[§95 The Dot Product#^def-95-1|Def. §95.1]], [[§96 The Cross Product#^def-96-1|Def. §96.1]]

> [!definition] Definition §100.3: Continuity of a Vector Function
> A vector function $\mathbf{r}$ is **continuous at $a$** if
>
> $$
> \lim_{t \to a} \mathbf{r}(t) = \mathbf{r}(a) .
> $$
>
> *Stewart: 13.1 (text)*

^def-100-3

> [!theorem] Proposition §100.2: Continuity Is Componentwise
> $\mathbf{r} = \langle f, g, h \rangle$ is continuous at $a$ if and only if its component functions $f$, $g$ and $h$ are continuous at $a$.
>
> *Stewart: 13.1 (text)*

^prop-100-2

> [!proof]+ Proof
> By [[§100 Vector Functions and Space Curves#^def-100-2|Definition §100.2]], $\lim_{t \to a}\mathbf{r}(t) = \mathbf{r}(a)$ means that the three component limits exist and $\langle \lim f, \lim g, \lim h \rangle = \langle f(a), g(a), h(a) \rangle$. Two vectors are equal exactly when their components are equal, so this says $\lim_{t \to a} f(t) = f(a)$, $\lim_{t \to a} g(t) = g(a)$ and $\lim_{t \to a} h(t) = h(a)$, which is continuity of $f$, $g$, $h$ at $a$ ([[§12 Continuity#^def-12-1|Definition §12.1]]).

^pf-100-2

*Uses:* [[§100 Vector Functions and Space Curves#^def-100-2|Def. §100.2]], [[§100 Vector Functions and Space Curves#^def-100-3|Def. §100.3]], [[§12 Continuity#^def-12-1|Def. §12.1]]

> [!example] Example §100.1: Domains and Limits
> **(a)** The component functions of $\mathbf{r}(t) = \langle t^3, \ln(3 - t), \sqrt t \rangle$ are $f(t) = t^3$, $g(t) = \ln(3 - t)$, $h(t) = \sqrt t$. They are all defined when $3 - t > 0$ and $t \ge 0$, so the domain of $\mathbf{r}$ is $[0, 3)$.
>
> **(b)** Find $\lim_{t \to 0}\mathbf{r}(t)$ for $\mathbf{r}(t) = (1 + t^3)\,\mathbf{i} + te^{-t}\,\mathbf{j} + \dfrac{\sin t}{t}\,\mathbf{k}$. By [[§100 Vector Functions and Space Curves#^def-100-2|Definition §100.2]],
>
> $$
> \lim_{t \to 0}\mathbf{r}(t) = \Big[\lim_{t \to 0}(1 + t^3)\Big]\mathbf{i} + \Big[\lim_{t \to 0} te^{-t}\Big]\mathbf{j} + \Big[\lim_{t \to 0}\frac{\sin t}{t}\Big]\mathbf{k} = \mathbf{i} + 0\,\mathbf{j} + 1\,\mathbf{k} = \mathbf{i} + \mathbf{k} ,
> $$
>
> using $\lim_{t \to 0}(\sin t)/t = 1$ ([[§19 Derivatives of Trigonometric Functions#^thm-19-6|Theorem §19.6]]).
>
> **(c)** For $\mathbf{r}(t) = \Big\langle \sqrt{2 - t},\ \dfrac{e^t - 1}{t},\ \ln(t + 1) \Big\rangle$: the components need $t \le 2$, $t \ne 0$ and $t > -1$, so the domain is $(-1, 0) \cup (0, 2]$. As $t \to 0$, $\sqrt{2 - t} \to \sqrt2$, $\ln(t + 1) \to 0$, and $\dfrac{e^t - 1}{t} = \dfrac{e^t - e^0}{t - 0} \to \dfrac{d}{dt}e^t\Big|_{t = 0} = 1$. So $\lim_{t \to 0}\mathbf{r}(t) = \langle \sqrt2, 1, 0 \rangle$, even though $\mathbf{r}(0)$ is undefined.
>
> **(d)** As $t \to \infty$:
>
> $$
> \frac{t^2}{\sqrt{2t^4 + 1}} = \frac{1}{\sqrt{2 + 1/t^4}} \to \frac{1}{\sqrt2}, \qquad \frac{t + 1}{e^t} \to 0, \qquad \arctan t \to \frac{\pi}{2} ,
> $$
>
> (the middle one by [[§31 Indeterminate Forms and L'Hospital's Rule#^thm-31-2|l'Hospital's Rule]], $\lim (t + 1)/e^t = \lim 1/e^t = 0$), so $\lim_{t \to \infty}\Big\langle \dfrac{t^2}{\sqrt{2t^4 + 1}}, \dfrac{t + 1}{e^t}, \arctan t \Big\rangle = \Big\langle \dfrac{1}{\sqrt2}, 0, \dfrac{\pi}{2} \Big\rangle$.
>
> *Stewart: Examples 13.1.1 and 13.1.2*
> *Source: 233 Exam 1 Review, Q10(a)–(b); 233 Midterm 1 Practice Questions, Q19*

^ex-100-1

## Space Curves

> [!definition] Definition §100.4: Space Curve and Parametric Equations
> Let $f$, $g$, $h$ be continuous real-valued functions on an interval $I$. The set $C$ of all points $(x, y, z)$ in space with
>
> $$
> x = f(t), \qquad y = g(t), \qquad z = h(t), \qquad (2)
> $$
>
> as $t$ varies throughout $I$, is a **space curve**. The equations (2) are **parametric equations of $C$**, and $t$ is a **parameter**. A vector function giving $C$ in this way is a **parametrization** of $C$.
>
> If $\mathbf{r}(t) = \langle f(t), g(t), h(t) \rangle$, then $\mathbf{r}(t)$ is the position vector of the point $P(f(t), g(t), h(t))$ on $C$. So every continuous vector function defines a space curve, traced out by the tip of the moving vector $\mathbf{r}(t)$, like the path of a particle whose position at time $t$ is $\mathbf{r}(t)$. Plane curves are the special case $\mathbf{r}(t) = \langle f(t), g(t) \rangle = f(t)\,\mathbf{i} + g(t)\,\mathbf{j}$ (compare [[§73 Curves Defined by Parametric Equations#^def-73-1|Definition §73.1]]).
>
> *Stewart: 13.1 (text)*

^def-100-4

> [!example] Example §100.2: Recognizing Curves
> **(a)** $\mathbf{r}(t) = \langle 1 + t, 2 + 5t, -1 + 6t \rangle$ has parametric equations $x = 1 + t$, $y = 2 + 5t$, $z = -1 + 6t$: the line through $(1, 2, -1)$ parallel to $\langle 1, 5, 6 \rangle$ ([[§98 Equations of Lines and Planes#^prop-98-2|Proposition §98.2]]). Equivalently, $\mathbf{r} = \mathbf{r}_0 + t\mathbf{v}$ with $\mathbf{r}_0 = \langle 1, 2, -1 \rangle$ and $\mathbf{v} = \langle 1, 5, 6 \rangle$.
>
> **(b)** Sketch $\mathbf{r}(t) = \cos t\,\mathbf{i} + \sin t\,\mathbf{j} + t\,\mathbf{k}$. The parametric equations are $x = \cos t$, $y = \sin t$, $z = t$. Since $x^2 + y^2 = \cos^2 t + \sin^2 t = 1$ for all $t$, the curve lies on the circular cylinder $x^2 + y^2 = 1$. The point $(x, y, z)$ lies directly above $(x, y, 0)$, which moves counterclockwise around the unit circle in the $xy$-plane, while $z = t$ increases. So the curve spirals upward around the cylinder: it is a **helix**, rising $2\pi$ per turn.
>
> **(c)** The plane curve $\mathbf{u}(t) = \langle 1 + \cos t, \sin t \rangle$, $0 \le t \le 2\pi$: from $x - 1 = \cos t$ and $y = \sin t$, eliminating $t$ gives $(x - 1)^2 + y^2 = \cos^2 t + \sin^2 t = 1$. It is the circle of radius $1$ centered at $(1, 0)$, traversed once counterclockwise starting from $(2, 0)$.
>
> *Stewart: Examples 13.1.3 and 13.1.4*
> *Source: 233 Midterm 1 Practice Questions, Q18*

^ex-100-2

> [!remark] Remark: Method — Parametrizing a Curve of Intersection
> To find a vector function for the curve where two surfaces meet:
> 1. **Project.** Combine the two equations to eliminate one variable; the result describes the projection of the curve onto a coordinate plane (a cylinder containing the curve).
> 2. **Parametrize the projection**: a circle $(x - h)^2 + (y - k)^2 = R^2$ by $x = h + R\cos t$, $y = k + R\sin t$, $0 \le t \le 2\pi$; a graph $y = f(x)$ by $x = t$, $y = f(t)$.
> 3. **Lift.** Solve one of the original equations for the remaining variable in terms of $t$.

^rem-100-1

> [!example] Example §100.3: Finding Parametrizations
> **(a)** The line segment from $P(1, 3, -2)$ to $Q(2, -1, 3)$: by [[§98 Equations of Lines and Planes#^prop-98-4|Proposition §98.4]] with $\mathbf{r}_0 = \langle 1, 3, -2 \rangle$, $\mathbf{r}_1 = \langle 2, -1, 3 \rangle$,
>
> $$
> \mathbf{r}(t) = (1 - t)\langle 1, 3, -2 \rangle + t\langle 2, -1, 3 \rangle = \langle 1 + t,\ 3 - 4t,\ -2 + 5t \rangle, \qquad 0 \le t \le 1 .
> $$
>
> **(b)** The curve of intersection of the cylinder $x^2 + y^2 = 1$ and the plane $y + z = 2$. Its projection onto the $xy$-plane is the circle $x^2 + y^2 = 1$, $z = 0$, so $x = \cos t$, $y = \sin t$, $0 \le t \le 2\pi$. The plane gives $z = 2 - y = 2 - \sin t$:
>
> $$
> \mathbf{r}(t) = \cos t\,\mathbf{i} + \sin t\,\mathbf{j} + (2 - \sin t)\,\mathbf{k}, \qquad 0 \le t \le 2\pi .
> $$
>
> The curve is an ellipse, traced counterclockwise when viewed from above.
>
> **(c)** The cylinder $x^2 + y^2 = 16$ and the plane $x + z = 5$: in the same way, $x = 4\cos t$, $y = 4\sin t$, $z = 5 - x = 5 - 4\cos t$, so $\mathbf{r}(t) = \langle 4\cos t, 4\sin t, 5 - 4\cos t \rangle$, $0 \le t \le 2\pi$.
>
> **(d)** The paraboloid $4y = x^2 + z^2$ and the plane $y = x$. Substituting $y = x$: $4x = x^2 + z^2$, and completing the square, $(x - 2)^2 + z^2 = 4$. So the curve lies on the circular cylinder $(x - 2)^2 + z^2 = 4$, and its projection onto the $xz$-plane is the circle with center $(2, 0, 0)$ and radius $2$. Hence $x = 2 + 2\cos t$, $z = 2\sin t$, and since $y = x$,
>
> $$
> x = 2 + 2\cos t, \qquad y = 2 + 2\cos t, \qquad z = 2\sin t, \qquad 0 \le t \le 2\pi .
> $$
>
> **(e)** The paraboloid $z = 4x^2 + y^2$ and the parabolic cylinder $y = x^2$. The projection onto the $xy$-plane is the parabola $y = x^2$; take $x = t$, $y = t^2$. Then $z = 4t^2 + (t^2)^2$, so $\mathbf{r}(t) = \langle t, t^2, 4t^2 + t^4 \rangle$, $t \in \mathbb{R}$.
>
> *Stewart: Examples 13.1.5, 13.1.6 and 13.1.7*
> *Source: 233 Exam 1 Review, Q11; 233 Midterm 1 Practice Questions, Q20*

^ex-100-3

![[m233-86-1.svg]]
*(a) The helix of [[§100 Vector Functions and Space Curves#^ex-100-2|Example §100.2]](b) winds up the cylinder $x^2 + y^2 = 1$, passing $(1, 0, 0)$ at $t = 0$ and $(0, 1, \pi/2)$ at $t = \pi/2$. (b) [[§100 Vector Functions and Space Curves#^ex-100-3|Example §100.3]](b): the slanted plane $y + z = 2$ (green) cuts the cylinder in an ellipse (red). The points $(1, 0, 2)$, $(0, 1, 1)$, $(-1, 0, 2)$, $(0, -1, 3)$ correspond to $t = 0, \pi/2, \pi, 3\pi/2$.*

> [!example] Example §100.4: Do Two Curves Meet?
> **(a)** Do $\mathbf{r}_1(t) = \langle t^2 - 2, 7t, t^3 - 1 \rangle$ and $\mathbf{r}_2(s) = \langle 1 + 2s, 6 + 5s, 4 + 3s \rangle$ intersect?
>
> The curves may pass through a common point at *different* parameter values, so use two parameters and solve $\mathbf{r}_1(t) = \mathbf{r}_2(s)$:
>
> $$
> t^2 - 2 = 1 + 2s, \qquad 7t = 6 + 5s, \qquad t^3 - 1 = 4 + 3s .
> $$
>
> The second gives $s = (7t - 6)/5$. Substituting in the first, $5t^2 - 10 = 5 + 14t - 12$, so $5t^2 - 14t - 3 = 0$, that is, $(5t + 1)(t - 3) = 0$. For $t = 3$, $s = 3$, and the third equation would need $26 = 13$. For $t = -\frac15$, $s = -\frac{37}{25}$, and the third would need $-\frac{126}{125} = -\frac{11}{25} = -\frac{55}{125}$. Both fail, so the curves do not intersect.
>
> **(b)** Show that the paths $\mathbf{r}(t) = 2t\,\mathbf{i} + (t^2 - 6)\,\mathbf{j} - \frac13 t^3\,\mathbf{k}$ and $\mathbf{w}(s) = \langle 2, 5, 1 \rangle + s\langle 2, -1, -5 \rangle$ meet.
>
> Solve $2t = 2 + 2s$, $t^2 - 6 = 5 - s$, $-\frac13 t^3 = 1 - 5s$. The first gives $s = t - 1$; the second becomes $t^2 - 6 = 6 - t$, so $t^2 + t - 12 = (t + 4)(t - 3) = 0$. For $t = 3$, $s = 2$ and the third equation reads $-9 = 1 - 10$, which holds. (For $t = -4$, $s = -5$: $\frac{64}{3} \ne 26$.) So the paths meet at $\mathbf{r}(3) = \mathbf{w}(2) = (6, 3, -9)$. The two objects pass through this point at different times, $t = 3$ and $s = 2$, so they do not collide there.
>
> *Source: 233 Midterm 1 Practice Questions, Q17, Q14(a)*

^ex-100-4

## Using Technology to Draw Space Curves

> [!remark]- Remark: Visualizing Space Curves
> Space curves are hard to draw by hand; computer plots help, though optical illusions make them hard to read (Stewart shows a toroidal spiral and a trefoil knot). Two tricks help. First, view the curve in a box from several vantage points, including straight down each axis, which shows its projections. Second, draw it on a surface that contains it. For the **twisted cubic** $\mathbf{r}(t) = \langle t, t^2, t^3 \rangle$ (Stewart's Example 13.1.8), eliminating $t$ from $x = t$, $y = t^2$ shows that the curve lies on the parabolic cylinder $y = x^2$ (its projection onto the $xy$-plane), and from $x = t$, $z = t^3$ on the cylinder $z = x^3$; it is the curve of intersection of these two cylinders and climbs through the origin as it twists. The helix was visualized the same way, on the cylinder $x^2 + y^2 = 1$. Space curves also appear in science: the double helix of DNA, and the paths of charged particles in perpendicular electric and magnetic fields, such as $\mathbf{r}(t) = \langle t - \sin t, 1 - \cos t, t \rangle$, whose projection is a cycloid.

^rem-100-2
