---
type: section
subject: "[[Calculus]]"
chapter: 14
section: 96
stewart: "14.7"
aliases: ["Stewart 14.7"]
tags: [calculus, math233]
---
← [[§95 Directional Derivatives and the Gradient Vector]] · ↑ [[· 14 Partial Derivatives]] · [[§97 Lagrange Multipliers]] →

*Stewart, Section 14.7 · MATH 233 (UMass, Spring 2023): Midterm 1 Practice Questions (Q32) = Exam 2 Practice Questions (Q1), Exam 2 Practice Questions (Q3), Practice Final Set 1 (Part I, Q3).*

One of the main uses of ordinary derivatives is finding maximum and minimum values ([[§25 Maximum and Minimum Values|§25]]); this section does the same for functions of two variables. At a local maximum or minimum the tangent plane is horizontal, so both partial derivatives vanish: extreme values occur at critical points. As in one variable, a critical point need not be an extreme point; a saddle point is the new possibility. The Second Derivatives Test sorts critical points by the sign of $D = f_{xx} f_{yy} - f_{xy}^2$. For absolute extreme values, the Extreme Value Theorem guarantees existence on closed bounded sets, and the Closed Interval Method extends to them: compare the values at critical points with the extreme values on the boundary.

## Local Maximum and Minimum Values

> [!definition] Definition §96.1: Local Maximum and Minimum
> A function of two variables has a **local maximum** at $(a, b)$ if $f(x, y) \le f(a, b)$ when $(x, y)$ is near $(a, b)$, that is, for all points $(x, y)$ in some disk with center $(a, b)$. The number $f(a, b)$ is then a **local maximum value**. If $f(x, y) \ge f(a, b)$ when $(x, y)$ is near $(a, b)$, then $f$ has a **local minimum** at $(a, b)$ and $f(a, b)$ is a **local minimum value**.
>
> If the inequalities hold for *all* points $(x, y)$ in the domain of $f$, then $f$ has an **absolute maximum** (or **absolute minimum**) at $(a, b)$.
>
> *Stewart: 14.7, Definition 1 and text*

^def-96-1

> [!theorem] Theorem §96.1: Fermat's Theorem for Two Variables
> If $f$ has a local maximum or minimum at $(a, b)$ and the first-order partial derivatives of $f$ exist there, then $f_x(a, b) = 0$ and $f_y(a, b) = 0$. In gradient notation: $\nabla f(a, b) = \mathbf{0}$.
>
> *Stewart: 14.7, Theorem 2*

^thm-96-1

> [!proof]+ Proof
> Let $g(x) = f(x, b)$. If $f$ has a local maximum (or minimum) at $(a, b)$, then $g$ has a local maximum (or minimum) at $a$: the points $(x, b)$ with $x$ near $a$ lie in the disk of Definition §96.1. Since $g'(a) = f_x(a, b)$ exists ([[§92 Partial Derivatives#^def-92-1|Definition §92.1]]), Fermat's Theorem for one variable (Stewart, Theorem 4.1.4; [[§25 Maximum and Minimum Values#^thm-25-2|Theorem §25.2]]) gives $g'(a) = 0$, that is, $f_x(a, b) = 0$. Similarly, applying Fermat's Theorem to $G(y) = f(a, y)$ gives $f_y(a, b) = 0$.

^pf-96-1

*Uses:* [[§96 Maximum and Minimum Values#^def-96-1|Def. §96.1]], [[§92 Partial Derivatives#^def-92-1|Def. §92.1]], [[§25 Maximum and Minimum Values#^thm-25-2|§25.2]] (Fermat's Theorem)

> [!remark]- Connections
> - Rigorous treatment: [[§14 Optimization and Lagrange Multipliers#^thm-14-1|452 Thm. §14.1]] (in $\mathbb{R}^n$), which rests on the one-variable [[§29 The Mean Value Theorem#^thm-29-1|451 Thm. §29.1]] (Interior Extremum Theorem).

Putting $f_x(a, b) = 0$ and $f_y(a, b) = 0$ in the equation of the tangent plane ([[§93 Tangent Planes and Linear Approximations#^thm-93-1|Theorem §93.1]]) gives $z = z_0$: if the graph of $f$ has a tangent plane at a local maximum or minimum, the tangent plane is horizontal.

> [!definition] Definition §96.2: Critical Point; Saddle Point
> A point $(a, b)$ is a **critical point** (or **stationary point**) of $f$ if $f_x(a, b) = 0$ and $f_y(a, b) = 0$, or if one of these partial derivatives does not exist. A critical point $(a, b)$ with $f_x(a, b) = f_y(a, b) = 0$ at which $f$ has neither a local maximum nor a local minimum is a **saddle point** of $f$.
>
> *Stewart: 14.7 (text)*

^def-96-2

Theorem §96.1 says that if $f$ has a local maximum or minimum at $(a, b)$, then $(a, b)$ is a critical point of $f$. As in one variable, the converse fails: not every critical point gives a maximum or minimum. The name *saddle point* comes from the shape of the graph near the origin in Example §96.1(b). In general the graph near a saddle point need not resemble a saddle, but it crosses its tangent plane there. (A mountain pass is a saddle: for a hiker crossing it the pass is the lowest point of the route, for one walking along the ridge the highest.)

> [!example] Example §96.1: A Minimum and a Saddle
> **(a)** Let $f(x, y) = x^2 + y^2 - 2x - 6y + 14$. Then
>
> $$
> f_x(x, y) = 2x - 2 , \qquad f_y(x, y) = 2y - 6 ,
> $$
>
> which are $0$ when $x = 1$ and $y = 3$, so the only critical point is $(1, 3)$. Completing the square,
>
> $$
> f(x, y) = 4 + (x - 1)^2 + (y - 3)^2 .
> $$
>
> Since $(x - 1)^2 \ge 0$ and $(y - 3)^2 \ge 0$, $f(x, y) \ge 4$ for all $x$ and $y$. So $f(1, 3) = 4$ is a local minimum, and in fact the absolute minimum of $f$. The graph is the elliptic paraboloid with vertex $(1, 3, 4)$.
>
> **(b)** Find the extreme values of $f(x, y) = y^2 - x^2$.
>
> Since $f_x = -2x$ and $f_y = 2y$, the only critical point is $(0, 0)$. For points on the $x$-axis, $y = 0$, so $f(x, y) = -x^2 < 0$ if $x \ne 0$. For points on the $y$-axis, $x = 0$, so $f(x, y) = y^2 > 0$ if $y \ne 0$. So every disk with center $(0, 0)$ contains points where $f$ is positive and points where $f$ is negative, and $f(0, 0) = 0$ is not an extreme value: $f$ has no extreme value at all, and $(0, 0)$ is a saddle point. The graph, the hyperbolic paraboloid $z = y^2 - x^2$, has a horizontal tangent plane $z = 0$ at the origin; $f(0, 0) = 0$ is a maximum in the direction of the $x$-axis but a minimum in the direction of the $y$-axis.
>
> *Stewart: Examples 14.7.1 and 14.7.2*

^ex-96-1

![[m233-96-1.svg]]
*The saddle $z = y^2 - x^2$ of Example §96.1(b). Its trace in the plane $y = 0$ is the downward parabola $z = -x^2$ (red), whose top is the origin; its trace in the plane $x = 0$ is the upward parabola $z = y^2$ (blue), whose bottom is the origin. The tangent plane at the origin is horizontal, but $f(0, 0) = 0$ is neither a maximum nor a minimum.*

## The Second Derivatives Test

> [!theorem] Theorem §96.2: Second Derivatives Test
> Suppose the second partial derivatives of $f$ are continuous on a disk with center $(a, b)$, and suppose that $f_x(a, b) = 0$ and $f_y(a, b) = 0$ (so $(a, b)$ is a critical point of $f$). Let
>
> $$
> D = D(a, b) = f_{xx}(a, b)\,f_{yy}(a, b) - [f_{xy}(a, b)]^2 .
> $$
>
> (a) If $D > 0$ and $f_{xx}(a, b) > 0$, then $f(a, b)$ is a local minimum.
>
> (b) If $D > 0$ and $f_{xx}(a, b) < 0$, then $f(a, b)$ is a local maximum.
>
> (c) If $D < 0$, then $(a, b)$ is a saddle point of $f$.
>
> *Stewart: 14.7, Theorem 3*

^thm-96-2

> [!remark] Remark: Using the Test
> **Note 1.** If $D = 0$, the test gives no information: $f$ could have a local maximum or a local minimum at $(a, b)$, or $(a, b)$ could be a saddle point. (For example $x^4 + y^4$, $-x^4 - y^4$ and $x^4 - y^4$ all have $D(0, 0) = 0$.)
>
> **Note 2.** To remember the formula for $D$, write it as a determinant (of the Hessian matrix):
>
> $$
> D = \begin{vmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{vmatrix} = f_{xx} f_{yy} - (f_{xy})^2 ,
> $$
>
> using $f_{xy} = f_{yx}$ (Clairaut's Theorem, [[§92 Partial Derivatives#^thm-92-2|Theorem §92.2]]).
>
> **Why it works.** Along the line through $(a, b)$ in the direction of a unit vector $\mathbf{u} = \langle h, k \rangle$, the second derivative of $f$ is the quadratic expression $f_{xx} h^2 + 2f_{xy} hk + f_{yy} k^2$, the one-variable second derivative test in the direction $\mathbf{u}$. $D > 0$ means that this expression has the same sign as $f_{xx}$ for *every* direction; $D < 0$ means that it is positive in some directions and negative in others.

^rem-96-1

> [!proof]+ Proof
> Stewart proves part (a) and says part (b) "has a similar proof"; part (c) is filled in here.
>
> **Second directional derivatives.** Let $\mathbf{u} = \langle h, k \rangle$ be a unit vector. Since the second partial derivatives are continuous on the disk, $f_x$ and $f_y$ are differentiable there ([[§93 Tangent Planes and Linear Approximations#^thm-93-2|Theorem §93.2]]), hence continuous, so $f$ is differentiable as well (Theorem §93.2 again); and so is $D_{\mathbf{u}} f = f_x h + f_y k$ ([[§95 Directional Derivatives and the Gradient Vector#^thm-95-1|Theorem §95.1]]). Applying Theorem §95.1 a second time,
>
> $$
> D_{\mathbf{u}}^2 f = D_{\mathbf{u}}(D_{\mathbf{u}} f) = \frac{\partial}{\partial x}(D_{\mathbf{u}} f)\,h + \frac{\partial}{\partial y}(D_{\mathbf{u}} f)\,k = (f_{xx} h + f_{yx} k) h + (f_{xy} h + f_{yy} k) k = f_{xx} h^2 + 2f_{xy} hk + f_{yy} k^2 ,
> $$
>
> by Clairaut's Theorem. Where $f_{xx} \ne 0$, completing the square gives
>
> $$
> D_{\mathbf{u}}^2 f = f_{xx} \Big( h + \frac{f_{xy}}{f_{xx}} k \Big)^2 + \frac{k^2}{f_{xx}} \big( f_{xx} f_{yy} - f_{xy}^2 \big) . \qquad (10)
> $$
>
> **Behaviour along a line.** For a unit vector $\mathbf{u}$ let $g(t) = f(a + th, b + tk)$. By the Chain Rule ([[§94 The Chain Rule#^thm-94-1|Theorem §94.1]]), $g'(t) = D_{\mathbf{u}} f(a + th, b + tk)$ and $g''(t) = D_{\mathbf{u}}^2 f(a + th, b + tk)$. Since $(a, b)$ is a critical point, $g'(0) = f_x(a, b) h + f_y(a, b) k = 0$.
>
> **(a)** We are given $f_{xx}(a, b) > 0$ and $D(a, b) > 0$. Since $f_{xx}$ and $D = f_{xx} f_{yy} - f_{xy}^2$ are continuous, there is a disk $B$ with center $(a, b)$ and radius $\delta > 0$ such that $f_{xx}(x, y) > 0$ and $D(x, y) > 0$ whenever $(x, y)$ is in $B$. Looking at Equation (10), $D_{\mathbf{u}}^2 f(x, y) > 0$ whenever $(x, y)$ is in $B$: both terms are $\ge 0$, and they are not both $0$ (if $k = 0$ then $h = \pm 1$ and the first term is $f_{xx} > 0$). So for every unit vector $\mathbf{u}$, $g''(t) > 0$ for $|t| < \delta$: the curve $C$ in which the vertical plane through $P(a, b, f(a, b))$ in the direction of $\mathbf{u}$ cuts the graph of $f$ is concave upward on an interval of length $2\delta$. (Stewart concludes from the concavity; the step is this.) Since $g''> 0$, $g'$ is increasing on $(-\delta, \delta)$, and $g'(0) = 0$, so $g' > 0$ on $(0, \delta)$ and $g$ is increasing on $[0, \delta)$: $g(t) \ge g(0)$ for $0 \le t < \delta$. Every point $(x, y)$ of $B$ is $(a + th, b + tk)$ for some unit vector $\langle h, k \rangle$ and some $0 \le t < \delta$. So $f(x, y) \ge f(a, b)$ for all $(x, y)$ in $B$: the graph of $f$ lies above its horizontal tangent plane at $P$, and $f(a, b)$ is a local minimum.
>
> **(b)** If $D > 0$ and $f_{xx}(a, b) < 0$, apply (a) to $-f$: its second partial derivatives are those of $f$ with the signs changed, so $(-f)_{xx}(a, b) > 0$ and its $D$ is the same as for $f$. So $-f$ has a local minimum at $(a, b)$, that is, $f$ has a local maximum there.
>
> **(c)** Let $Q(h, k) = f_{xx} h^2 + 2f_{xy} hk + f_{yy} k^2$, with the second partials evaluated at $(a, b)$, and suppose $D < 0$. Then $Q$ takes both signs. If $f_{xx} \ne 0$: $Q(1, 0) = f_{xx}$, and by (10), $Q(-f_{xy}, f_{xx}) = f_{xx} \cdot D$, which has the opposite sign. If $f_{xx} = 0$: then $D = -f_{xy}^2 < 0$, so $f_{xy} \ne 0$, and $Q(1, k) = k(2f_{xy} + f_{yy} k)$ has opposite signs for small $k > 0$ and small $k < 0$. Normalizing, there are unit vectors $\mathbf{u}_1$ and $\mathbf{u}_2$ with $D_{\mathbf{u}_1}^2 f(a, b) > 0 > D_{\mathbf{u}_2}^2 f(a, b)$. For $\mathbf{u}_1$, $g''(0) > 0$ and by continuity $g'' > 0$ near $0$; with $g'(0) = 0$ the argument of (a) gives $g(t) > g(0)$ for small $t \ne 0$. So arbitrarily close to $(a, b)$ there are points where $f > f(a, b)$. In the same way the direction $\mathbf{u}_2$ gives points arbitrarily close to $(a, b)$ where $f < f(a, b)$. Hence $f$ has neither a local maximum nor a local minimum at $(a, b)$: it is a saddle point.

^pf-96-2

*Uses:* [[§92 Partial Derivatives#^thm-92-2|§92.2]] (Clairaut), [[§93 Tangent Planes and Linear Approximations#^thm-93-2|§93.2]], [[§95 Directional Derivatives and the Gradient Vector#^thm-95-1|§95.1]], [[§94 The Chain Rule#^thm-94-1|§94.1]], [[§96 Maximum and Minimum Values#^def-96-2|Def. §96.2]], [[§27 What Derivatives Tell Us About the Shape of a Graph#^thm-27-1|§27.1]] (increasing/decreasing test)

> [!remark]- Connections
> - Rigorous treatment: [[§14 Optimization and Lagrange Multipliers#^thm-14-4|452 Thm. §14.4]], in the language of the Hessian matrix [[§14 Optimization and Lagrange Multipliers#^def-14-2|452 Def. §14.2]] and its definiteness [[§14 Optimization and Lagrange Multipliers#^def-14-3|452 Def. §14.3]]: $D > 0$, $f_{xx} > 0$ says that the Hessian is positive definite, $D < 0$ that it is indefinite. The quadratic expression $Q$ is the second-order term of the Taylor expansion, [[§9 Taylor's Theorem for Multivariable Functions#^ex-9-3|452 Ex. §9.3]].
> - See also: [[§49★ Quadratic Forms#^thm-49-4|235 Thm. §49.4]] (a quadratic form $\mathbf{x}^TA\mathbf{x}$ is positive definite, negative definite or indefinite according to the signs of the eigenvalues of $A$; for the Hessian, $D = \lambda_1\lambda_2$), with the method in [[§49★ Quadratic Forms#^rem-49-2|235 Remark: Method — Classifying a Quadratic Form]].

> [!example] Example §96.2: Classifying Three Critical Points
> Find the local maximum and minimum values and saddle points of $f(x, y) = x^4 + y^4 - 4xy + 1$.
>
> **Critical points.** $f_x = 4x^3 - 4y$ and $f_y = 4y^3 - 4x$ exist everywhere, so the critical points are the solutions of
>
> $$
> x^3 - y = 0 \qquad\text{and}\qquad y^3 - x = 0 .
> $$
>
> Substituting $y = x^3$ from the first equation into the second,
>
> $$
> 0 = x^9 - x = x(x^8 - 1) = x(x^4 - 1)(x^4 + 1) = x(x^2 - 1)(x^2 + 1)(x^4 + 1) ,
> $$
>
> so there are three real solutions, $x = 0, 1, -1$, and three critical points: $(0, 0)$, $(1, 1)$, $(-1, -1)$.
>
> **Second derivatives.**
>
> $$
> f_{xx} = 12x^2 , \qquad f_{xy} = -4 , \qquad f_{yy} = 12y^2 , \qquad D(x, y) = f_{xx} f_{yy} - (f_{xy})^2 = 144x^2 y^2 - 16 .
> $$
>
> - $D(0, 0) = -16 < 0$: by (c), the origin is a saddle point.
> - $D(1, 1) = 128 > 0$ and $f_{xx}(1, 1) = 12 > 0$: by (a), $f(1, 1) = 1 + 1 - 4 + 1 = -1$ is a local minimum.
> - $D(-1, -1) = 128 > 0$ and $f_{xx}(-1, -1) = 12 > 0$: $f(-1, -1) = -1$ is also a local minimum.
>
> On a contour map, the level curves near $(1, 1)$ and $(-1, -1)$ are ovals around the two minima, while near the origin they resemble hyperbolas: moving away from $(0, 0)$, where $f = 1$, the values decrease in some directions and increase in others.
>
> *Stewart: Example 14.7.3*

^ex-96-2

When the critical-point equations cannot be solved exactly, they are solved numerically. In Stewart's Example 14.7.4, $f(x, y) = 10x^2 y - 5x^2 - 4y^2 - x^4 - 2y^4$ has $f_x = 2x(10y - 5 - 2x^2)$ and $f_y = 10x^2 - 8y - 8y^3$. The case $x = 0$ gives $-4y(1 + y^2) = 0$, so the critical point $(0, 0)$. The case $x^2 = 5y - 2.5$ gives $4y^3 - 21y + 12.5 = 0$, with roots $y \approx -2.5452$ (no real $x$), $0.6468$ and $1.8984$. So there are five critical points: local maxima at $(0, 0)$ (with $f = 0$) and at $(\pm 2.64, 1.90)$ (with $f \approx 8.50$), and saddle points at $(\pm 0.86, 0.65)$. Since $f \to -\infty$ far from the origin (the dominant terms are $-x^4 - 2y^4$), the highest points of the graph are $(\pm 2.64, 1.90, 8.50)$.

> [!example] Example §96.3: Critical Points from the Exams
> **(a)** Let $f(x, y) = x^2 y - y^2 - 2y - x^2$. Find all the critical points of $f$ and classify them as local maxima, local minima or saddle points.
>
> $$
> f_x = 2xy - 2x = 2x(y - 1) , \qquad f_y = x^2 - 2y - 2 .
> $$
>
> $f_x = 0$ when $x = 0$ or $y = 1$. If $x = 0$, then $f_y = -2y - 2 = 0$ gives $y = -1$. If $y = 1$, then $f_y = x^2 - 4 = 0$ gives $x = \pm 2$. The critical points are $(0, -1)$, $(2, 1)$, $(-2, 1)$. Next,
>
> $$
> f_{xx} = 2y - 2 , \qquad f_{xy} = 2x , \qquad f_{yy} = -2 , \qquad D = (2y - 2)(-2) - 4x^2 = 4 - 4y - 4x^2 .
> $$
>
> - $(0, -1)$: $D = 4 + 4 - 0 = 8 > 0$ and $f_{xx} = -4 < 0$, so $f(0, -1) = 0 - 1 + 2 - 0 = 1$ is a **local maximum**.
> - $(\pm 2, 1)$: $D = 4 - 4 - 16 = -16 < 0$, so these are **saddle points**.
>
> **(b)** Which of the following points is a local maximum of $f(x, y) = xy - x^2 y - xy^2$? (Choices: $(0, 0)$, $(1, 1)$, $(0, 2)$, $(2, 0)$, $(\frac13, \frac13)$, $(\frac12, \frac12)$.)
>
> $\nabla f = \langle y - 2xy - y^2,\ x - x^2 - 2xy \rangle = \langle y(1 - 2x - y),\ x(1 - x - 2y) \rangle$. The first component vanishes when $y = 0$ or $y = 1 - 2x$, the second when $x = 0$ or $x = 1 - 2y$. The four combinations give the critical points $(0, 0)$, $(1, 0)$, $(0, 1)$ and $(\frac13, \frac13)$; of the choices, only $(0, 0)$ and $(\frac13, \frac13)$ are critical. With $f_{xx} = -2y$, $f_{yy} = -2x$, $f_{xy} = 1 - 2x - 2y$,
>
> $$
> D = 4xy - (1 - 2x - 2y)^2 ; \qquad D(0, 0) = -1 < 0 , \qquad D\big(\tfrac13, \tfrac13\big) = \tfrac49 - \tfrac19 = \tfrac13 > 0 , \quad f_{xx}\big(\tfrac13, \tfrac13\big) = -\tfrac23 < 0 .
> $$
>
> So the origin is a saddle point, and **$(\frac13, \frac13)$ is a local maximum**, with value $\frac19 - \frac{1}{27} - \frac{1}{27} = \frac{1}{27}$.
>
> *Source: 233 Midterm 1 Practice Questions, Q32 (= Exam 2 Practice Questions, Q1)*
> *Source: 233 Practice Final Set 1, Part I Q3*

^ex-96-3

> [!remark] Remark: Method — Finding and Classifying Critical Points
> 1. Compute $f_x$ and $f_y$, and solve $f_x = 0$, $f_y = 0$ simultaneously. Factor where possible ($2x(y - 1) = 0$ splits into cases), and in each case substitute into the other equation; keep track of every case. Add the points where $f_x$ or $f_y$ does not exist.
> 2. Compute $f_{xx}$, $f_{xy}$, $f_{yy}$ and $D = f_{xx} f_{yy} - f_{xy}^2$ as functions, then evaluate at each critical point.
> 3. Classify by [[§96 Maximum and Minimum Values#^thm-96-2|Theorem §96.2]]: $D < 0$ saddle; $D > 0$ and $f_{xx} > 0$ minimum; $D > 0$ and $f_{xx} < 0$ maximum. If $D = 0$, examine $f$ directly near the point (complete squares, or compare values along lines).
> 4. For an applied problem with one critical point, physical reasoning often shows that it gives the absolute extremum sought (Example §96.4).

^rem-96-2

> [!example] Example §96.4: Shortest Distances
> **(a)** Find the shortest distance from the point $(1, 0, -2)$ to the plane $x + 2y + z = 4$.
>
> The distance from $(x, y, z)$ to $(1, 0, -2)$ is $d = \sqrt{(x - 1)^2 + y^2 + (z + 2)^2}$. On the plane, $z = 4 - x - 2y$, so $d = \sqrt{(x - 1)^2 + y^2 + (6 - x - 2y)^2}$. We minimize the simpler expression
>
> $$
> d^2 = f(x, y) = (x - 1)^2 + y^2 + (6 - x - 2y)^2 .
> $$
>
> Solving
>
> $$
> f_x = 2(x - 1) - 2(6 - x - 2y) = 4x + 4y - 14 = 0 , \qquad f_y = 2y - 4(6 - x - 2y) = 4x + 10y - 24 = 0
> $$
>
> (subtract: $6y = 10$) gives the only critical point $\big(\frac{11}{6}, \frac53\big)$. Since $f_{xx} = 4$, $f_{xy} = 4$, $f_{yy} = 10$, we have $D = 40 - 16 = 24 > 0$ and $f_{xx} > 0$, so $f$ has a local minimum there. Intuitively it is the absolute minimum, because there must be a point on the plane closest to $(1, 0, -2)$. With $x = \frac{11}{6}$, $y = \frac53$: $x - 1 = \frac56$ and $6 - x - 2y = \frac56$, so
>
> $$
> d = \sqrt{\big(\tfrac56\big)^2 + \big(\tfrac53\big)^2 + \big(\tfrac56\big)^2} = \sqrt{\tfrac{150}{36}} = \tfrac56\sqrt6 .
> $$
>
> (The distance formula of [[§84 Equations of Lines and Planes#^thm-84-8|Theorem §84.8]] gives the same: $\frac{|1 + 0 - 2 - 4|}{\sqrt{1 + 4 + 1}} = \frac{5}{\sqrt6}$.)
>
> **(b)** Find the points on the cone $x^2 + y^2 = z^2$ closest to the point $P = (4, 2, 0)$.
>
> The squared distance from $(x, y, z)$ to $P$ is $(x - 4)^2 + (y - 2)^2 + z^2$, and on the cone $z^2 = x^2 + y^2$. So minimize
>
> $$
> g(x, y) = (x - 4)^2 + (y - 2)^2 + x^2 + y^2 .
> $$
>
> $g_x = 2(x - 4) + 2x = 4x - 8 = 0$ and $g_y = 2(y - 2) + 2y = 4y - 4 = 0$ give the only critical point $(2, 1)$; there $g_{xx} = g_{yy} = 4$, $g_{xy} = 0$, $D = 16 > 0$, a minimum. (Indeed $g = 2(x - 2)^2 + 2(y - 1)^2 + 10$, so it is the absolute minimum.) Then $z^2 = 4 + 1 = 5$: the closest points are $(2, 1, \pm\sqrt5)$, at distance $\sqrt{10}$.
>
> *Stewart: Example 14.7.5*
> *Source: 233 Exam 2 Practice Questions, Q3*

^ex-96-4

Stewart's Example 14.7.6 maximizes the volume $V = xyz$ of an open box made from $12$ m² of cardboard by eliminating $z$ through the constraint $2xz + 2yz + xy = 12$: then $z = (12 - xy)/[2(x + y)]$ and $V = (12xy - x^2 y^2)/[2(x + y)]$, with
$$
\frac{\partial V}{\partial x} = \frac{y^2 (12 - 2xy - x^2)}{2(x + y)^2} , \qquad \frac{\partial V}{\partial y} = \frac{x^2 (12 - 2xy - y^2)}{2(x + y)^2} .
$$
Since $x = 0$ or $y = 0$ gives $V = 0$, a maximum needs $12 - 2xy - x^2 = 0 = 12 - 2xy - y^2$, so $x^2 = y^2$, $x = y$ (both are positive), $12 - 3x^2 = 0$, $x = y = 2$ and $z = 1$. There must be a largest volume, and it occurs at a critical point, so it is $V = 4$ m³. The same answer is rederived by Lagrange multipliers in [[§97 Lagrange Multipliers#^ex-97-2|Example §97.2]].

## Absolute Maximum and Minimum Values

> [!definition] Definition §96.3: Absolute Extreme Values; Closed and Bounded Sets
> Let $(a, b)$ be a point in the domain $D$ of a function $f$ of two variables. Then $f(a, b)$ is the
> - **absolute maximum** value of $f$ on $D$ if $f(a, b) \ge f(x, y)$ for all $(x, y)$ in $D$;
> - **absolute minimum** value of $f$ on $D$ if $f(a, b) \le f(x, y)$ for all $(x, y)$ in $D$.
>
> A **boundary point** of a set $D$ in $\mathbb{R}^2$ is a point $(a, b)$ such that every disk with center $(a, b)$ contains points in $D$ and also points not in $D$. A **closed set** in $\mathbb{R}^2$ is one that contains all its boundary points, and a **bounded set** is one that is contained within some disk.
>
> *Stewart: 14.7, Definition 7 and text*

^def-96-3

For instance, the disk $\{(x, y) \mid x^2 + y^2 \le 1\}$, consisting of all points on or inside the circle $x^2 + y^2 = 1$, is a closed set: it contains all of its boundary points, the points of the circle. If even one point of the boundary circle were omitted, the set would not be closed. A closed set is the two-dimensional analog of a closed interval $[a, b]$, and a bounded set is "finite in extent".

> [!theorem] Theorem §96.3: Extreme Value Theorem for Functions of Two Variables
> If $f$ is continuous on a closed, bounded set $D$ in $\mathbb{R}^2$, then $f$ attains an absolute maximum value $f(x_1, y_1)$ and an absolute minimum value $f(x_2, y_2)$ at some points $(x_1, y_1)$ and $(x_2, y_2)$ in $D$.
>
> *Stewart: 14.7, Theorem 8*

^thm-96-3

*Stewart does not prove the Extreme Value Theorem. A closed bounded subset of $\mathbb{R}^2$ is compact ([[§15 Compact Spaces#^thm-15-12|590 Thm. §15.12]], Heine–Borel), the continuous image of a compact set is compact ([[§15 Compact Spaces#^thm-15-3|590 Thm. §15.3]]), and a compact subset of $\mathbb{R}$ is closed and bounded, so it contains its supremum and infimum.*

> [!remark]- Connections
> - The one-variable case on $[a, b]$, proved from completeness: [[Extreme Value Theorem]] (451). Hub for the higher-dimensional ingredient: [[Heine–Borel Theorem]].
> - Complex-variables version: [[§18 Continuity#^thm-18-6|342 Thm. §18.6]] (the modulus of a continuous complex function on a closed bounded region attains a maximum) and, for analytic functions, [[§59 Maximum Modulus Principle#^cor-59-4|342 Cor. §59.4]] (that maximum is on the boundary).

By Theorem §96.1, if $f$ has an extreme value at $(x_1, y_1)$, then $(x_1, y_1)$ is either a critical point of $f$ or a boundary point of $D$ (at an interior point the extreme value is also a local one). This extends the [[§25 Maximum and Minimum Values#^rem-25-2|Closed Interval Method]] of §25.

> [!remark] Remark: Method — Absolute Extrema on a Closed Bounded Set
> To find the absolute maximum and minimum values of a continuous function $f$ on a closed, bounded set $D$:
> 1. Find the values of $f$ at the critical points of $f$ in $D$.
> 2. Find the extreme values of $f$ on the boundary of $D$.
> 3. The largest of the values from steps 1 and 2 is the absolute maximum value; the smallest of these values is the absolute minimum value.
>
> For step 2, parametrize each piece of the boundary and use one-variable calculus (Example §96.5), or use [[§97 Lagrange Multipliers#^rem-97-2|Lagrange multipliers]] (§97).
>
> *Stewart: 14.7, Box 9*

^rem-96-3

> [!example] Example §96.5: Absolute Extrema on a Rectangle
> Find the absolute maximum and minimum values of $f(x, y) = x^2 - 2xy + 2y$ on the rectangle $D = \{(x, y) \mid 0 \le x \le 3,\ 0 \le y \le 2\}$.
>
> $f$ is a polynomial, hence continuous on the closed, bounded rectangle $D$, so Theorem §96.3 guarantees both an absolute maximum and an absolute minimum.
>
> **Step 1: critical points.** $f_x = 2x - 2y = 0$ and $f_y = -2x + 2 = 0$ give the only critical point $(1, 1)$, which is in $D$, with $f(1, 1) = 1$.
>
> **Step 2: the boundary**, made of four line segments.
> - $L_1$ ($y = 0$, $0 \le x \le 3$): $f(x, 0) = x^2$, increasing; minimum $f(0, 0) = 0$, maximum $f(3, 0) = 9$.
> - $L_2$ ($x = 3$, $0 \le y \le 2$): $f(3, y) = 9 - 4y$, decreasing; maximum $f(3, 0) = 9$, minimum $f(3, 2) = 1$.
> - $L_3$ ($y = 2$, $0 \le x \le 3$): $f(x, 2) = x^2 - 4x + 4 = (x - 2)^2$; minimum $f(2, 2) = 0$, maximum $f(0, 2) = 4$.
> - $L_4$ ($x = 0$, $0 \le y \le 2$): $f(0, y) = 2y$; maximum $f(0, 2) = 4$, minimum $f(0, 0) = 0$.
>
> On the boundary the minimum value of $f$ is $0$ and the maximum is $9$.
>
> **Step 3.** Comparing with $f(1, 1) = 1$: the absolute maximum value of $f$ on $D$ is $f(3, 0) = 9$, and the absolute minimum value is $f(0, 0) = f(2, 2) = 0$.
>
> *Stewart: Example 14.7.7*

^ex-96-5
