---
type: section
subject: "[[Calculus]]"
chapter: 14
section: 97
stewart: "14.8"
aliases: ["Stewart 14.8"]
tags: [calculus, math233]
---
← [[§96 Maximum and Minimum Values]] · ↑ [[· 14 Partial Derivatives]] · [[§98 Double Integrals Over Rectangles]] →

*Stewart, Section 14.8 · MATH 233 (UMass, Spring 2023): Exam 2 Practice Questions (Q6), Practice Exam 2 (Q2).*

Many optimization problems ask for the extreme values of a function $f$ subject to a side condition $g = k$: the largest volume of a box of given surface area, the point of a sphere nearest to a given point. Lagrange's method replaces the elimination of variables used in [[§96 Maximum and Minimum Values|§96]] by a geometric condition. At a constrained extreme point the level curve or level surface of $f$ touches the constraint curve or surface, so the two gradients are parallel: $\nabla f = \lambda \nabla g$. This turns the problem into a system of equations, which is symmetric in the variables and often easier to solve than the reduced problem. With two constraints, $\nabla f$ is a combination $\lambda \nabla g + \mu \nabla h$.

## Lagrange Multipliers: One Constraint

> [!remark] Remark: Why It Works
> To find the extreme values of $f(x, y)$ subject to $g(x, y) = k$, we look at the values of $f$ when the point $(x, y)$ is restricted to the level curve $g(x, y) = k$. Draw this curve together with level curves $f(x, y) = c$ for several values of $c$. Maximizing $f$ subject to $g(x, y) = k$ means finding the largest $c$ such that the level curve $f(x, y) = c$ still intersects $g(x, y) = k$. This happens when the two curves just touch, that is, have a common tangent line; otherwise $c$ could be increased further. Then their normal lines at the touching point $(x_0, y_0)$ coincide, so the gradient vectors are parallel: $\nabla f(x_0, y_0) = \lambda \nabla g(x_0, y_0)$ for some scalar $\lambda$. For $f(x, y, z)$ subject to $g(x, y, z) = k$ the same argument works with level surfaces: at the maximum value $c$, the level surface $f = c$ is tangent to the level surface $g = k$.

^rem-97-1

> [!theorem] Theorem §97.1: The Lagrange Condition
> Let $f$ and $g$ have continuous first partial derivatives, and suppose that $f$, restricted to the surface $S$: $g(x, y, z) = k$, has an extreme value at the point $P(x_0, y_0, z_0)$ (a maximum or minimum compared with the values of $f$ at the points of $S$ near $P$). If $\nabla g(x_0, y_0, z_0) \ne \mathbf{0}$, then there is a number $\lambda$ such that
>
> $$
> \nabla f(x_0, y_0, z_0) = \lambda\,\nabla g(x_0, y_0, z_0) . \qquad (1)
> $$
>
> The same holds for functions of two variables and a constraint curve $g(x, y) = k$.
>
> *Stewart: 14.8, Equation 1*

^thm-97-1

> [!proof]+ Proof
> **$\nabla f(P)$ is orthogonal to every curve on $S$ through $P$.** Let $C$ be a curve with vector equation $\mathbf{r}(t) = \langle x(t), y(t), z(t) \rangle$ ($x$, $y$, $z$ differentiable) that lies on $S$ and passes through $P$, with $\mathbf{r}(t_0) = \langle x_0, y_0, z_0 \rangle$. The composite function $h(t) = f(x(t), y(t), z(t))$ represents the values that $f$ takes on $C$. Since $f$ has an extreme value on $S$ at $P$, $h$ has a local extreme value at $t_0$, so $h'(t_0) = 0$ by Fermat's Theorem ([[§25 Maximum and Minimum Values#^thm-25-2|Theorem §25.2]]). By the Chain Rule ([[§94 The Chain Rule#^thm-94-3|Theorem §94.3]]; $f$ is differentiable by the three-variable form of [[§93 Tangent Planes and Linear Approximations#^thm-93-2|Theorem §93.2]]),
>
> $$
> 0 = h'(t_0) = f_x(x_0, y_0, z_0)\,x'(t_0) + f_y(x_0, y_0, z_0)\,y'(t_0) + f_z(x_0, y_0, z_0)\,z'(t_0) = \nabla f(x_0, y_0, z_0) \cdot \mathbf{r}'(t_0) .
> $$
>
> **$\nabla g(P)$ is orthogonal to the same vectors**, by [[§95 Directional Derivatives and the Gradient Vector#^thm-95-5|Theorem §95.5]]. Stewart concludes that the two gradients "must be parallel". (Stewart asserts this; here is why.) The tangent vectors $\mathbf{r}'(t_0)$ of curves on $S$ through $P$ fill the whole plane through the origin perpendicular to $\nabla g(P)$. Indeed, $\nabla g(P) \ne \mathbf{0}$, say $g_z(P) \ne 0$ (otherwise exchange the roles of the variables). By the Implicit Function Theorem ([[§94 The Chain Rule#^thm-94-6|Theorem §94.6]]), near $P$ the surface $S$ is the graph $z = \varphi(x, y)$ of a differentiable function. For any numbers $a$, $b$, the curve $\mathbf{r}(t) = \langle x_0 + ta,\ y_0 + tb,\ \varphi(x_0 + ta, y_0 + tb) \rangle$ lies on $S$, passes through $P$ at $t = 0$, and has $\mathbf{r}'(0) = \langle a, b, \varphi_x a + \varphi_y b \rangle$. These vectors, for all $a$ and $b$, form a plane (they are combinations of $\langle 1, 0, \varphi_x \rangle$ and $\langle 0, 1, \varphi_y \rangle$), and all of them are perpendicular to $\nabla g(P)$, so they form exactly the plane perpendicular to $\nabla g(P)$. Now $\nabla f(P)$ is perpendicular to this whole plane, so it lies on its normal line, the line spanned by $\nabla g(P)$: $\nabla f(P) = \lambda \nabla g(P)$ for some $\lambda$.
>
> For two variables the argument is the same one dimension down: the tangent vectors of the curve $g(x, y) = k$ at $P$ fill the line perpendicular to $\nabla g(P)$, and $\nabla f(P)$ is perpendicular to it.

^pf-97-1

*Uses:* [[§94 The Chain Rule#^thm-94-3|§94.3]], [[§94 The Chain Rule#^thm-94-6|§94.6]] (Implicit Function Theorem), [[§95 Directional Derivatives and the Gradient Vector#^thm-95-5|§95.5]], [[§93 Tangent Planes and Linear Approximations#^thm-93-2|§93.2]], [[§25 Maximum and Minimum Values#^thm-25-2|§25.2]] (Fermat's Theorem)

> [!remark]- Connections
> - Rigorous treatment: [[§14 Optimization and Lagrange Multipliers#^thm-14-2|452 Thm. §14.2]], with the hypothesis $\nabla g \ne \mathbf{0}$ as the "constraint qualification" and the proof through the Implicit Function Theorem; hub [[Method of Lagrange Multipliers]].
> - See also: [[§50★ Constrained Optimization#^thm-50-1|235 Thm. §50.1]] (the extremes of $\mathbf{x}^TA\mathbf{x}$ on the unit sphere are the largest and smallest eigenvalues of $A$; the Lagrange condition $\nabla f = \lambda\nabla g$ reads $A\mathbf{x} = \lambda\mathbf{x}$, though 235 proves it without calculus), worked in [[§50★ Constrained Optimization#^ex-50-2|235 Ex. §50.2]].

> [!definition] Definition §97.1: Lagrange Multiplier
> The number $\lambda$ in Equation (1) is called a **Lagrange multiplier**.
>
> *Stewart: 14.8 (text)*

^def-97-1

> [!remark] Remark: Method — Lagrange Multipliers
> To find the maximum and minimum values of $f(x, y, z)$ subject to the constraint $g(x, y, z) = k$ [assuming that these extreme values exist and $\nabla g \ne \mathbf{0}$ on the surface $g(x, y, z) = k$]:
> 1. Find all values of $x$, $y$, $z$ and $\lambda$ such that
>
> $$
> \nabla f(x, y, z) = \lambda\,\nabla g(x, y, z) \qquad\text{and}\qquad g(x, y, z) = k .
> $$
>
> 2. Evaluate $f$ at all the points $(x, y, z)$ that result from step 1. The largest of these values is the maximum value of $f$; the smallest is the minimum value of $f$.
>
> In components, step 1 is a system of four equations in the four unknowns $x$, $y$, $z$, $\lambda$:
>
> $$
> f_x = \lambda g_x , \qquad f_y = \lambda g_y , \qquad f_z = \lambda g_z , \qquad g(x, y, z) = k .
> $$
>
> All solutions must be found, but the values of $\lambda$ are not needed for the conclusion. A solution with $\lambda = 0$ has $\nabla f = \mathbf{0}$: it is a critical point of $f$, a possible local extreme value of $f$ on its domain and hence also a possible constrained one. For two variables, solve $f_x = \lambda g_x$, $f_y = \lambda g_y$, $g(x, y) = k$: three equations in three unknowns. There are no general rules for solving such systems; useful tricks are to solve each equation for $\lambda$ and equate, to multiply equations so that their left sides agree (Example §97.2), or to solve for the variables in terms of $\lambda$ and substitute into the constraint (Example §97.3). In each example one checks that $\nabla g \ne \mathbf{0}$ at all points with $g = k$.
>
> *Stewart: 14.8, Method of Lagrange Multipliers and text*

^rem-97-2

> [!example] Example §97.1: On a Circle and on a Disk
> **(a)** Find the extreme values of $f(x, y) = x^2 + 2y^2$ on the circle $x^2 + y^2 = 1$.
>
> With $g(x, y) = x^2 + y^2$ (and $\nabla g = \langle 2x, 2y \rangle \ne \mathbf{0}$ on the circle), the equations $f_x = \lambda g_x$, $f_y = \lambda g_y$, $g = 1$ are
>
> $$
> 2x = 2x\lambda \quad (2) \qquad 4y = 2y\lambda \quad (3) \qquad x^2 + y^2 = 1 \quad (4)
> $$
>
> From (2), $2x(1 - \lambda) = 0$, so $x = 0$ or $\lambda = 1$. If $x = 0$, then (4) gives $y = \pm 1$. If $\lambda = 1$, then (3) gives $4y = 2y$, so $y = 0$, and (4) gives $x = \pm 1$. So the possible extreme points are $(0, 1)$, $(0, -1)$, $(1, 0)$, $(-1, 0)$, and
>
> $$
> f(0, \pm 1) = 2 , \qquad f(\pm 1, 0) = 1 .
> $$
>
> The maximum value of $f$ on the circle is $f(0, \pm 1) = 2$ and the minimum value is $f(\pm 1, 0) = 1$. Geometrically: these are the highest and lowest points of the curve on the paraboloid $z = x^2 + 2y^2$ directly above the circle, and on a contour map they are where the level curves of $f$ (ellipses) just touch the circle.
>
> **(b)** Find the extreme values of $f(x, y) = x^2 + 2y^2$ on the disk $x^2 + y^2 \le 1$.
>
> Use the method of [[§96 Maximum and Minimum Values#^rem-96-3|§96 (Box 9)]]. Since $f_x = 2x$ and $f_y = 4y$, the only critical point is $(0, 0)$, with $f(0, 0) = 0$. On the boundary circle, by (a), the extreme values are $1$ and $2$. Comparing, the maximum value of $f$ on the disk is $f(0, \pm 1) = 2$ and the minimum value is $f(0, 0) = 0$.
>
> *Stewart: Examples 14.8.1 and 14.8.4*

^ex-97-1

![[m233-97-1.svg]]
*Example §97.1(a): the level curves $x^2 + 2y^2 = c$ of $f$ (ellipses, green) and the constraint circle $x^2 + y^2 = 1$ (red). The ellipse $c = 1$ touches the circle from inside at $(\pm 1, 0)$, the ellipse $c = 2$ from outside at $(0, \pm 1)$; at these four points the gradients of $f$ and $g$ are parallel (arrows). Ellipses with $1 < c < 2$ cross the circle, so $f$ takes all values between $1$ and $2$ on it.*

> [!example] Example §97.2: The Box Without a Lid
> A rectangular box without a lid is to be made from $12$ m² of cardboard. Find the maximum volume of such a box.
>
> Let $x$, $y$, $z$ be the length, width and height of the box in meters. We maximize $V = xyz$ subject to $g(x, y, z) = 2xz + 2yz + xy = 12$ (the area of the four sides and the bottom). The equations $\nabla V = \lambda \nabla g$, $g = 12$ are
>
> $$
> yz = \lambda(2z + y) \quad (5) \qquad xz = \lambda(2z + x) \quad (6) \qquad xy = \lambda(2x + 2y) \quad (7) \qquad 2xz + 2yz + xy = 12 \quad (8)
> $$
>
> Multiply (5) by $x$, (6) by $y$ and (7) by $z$, so that the left sides become identical:
>
> $$
> xyz = \lambda(2xz + xy) \quad (9) \qquad xyz = \lambda(2yz + xy) \quad (10) \qquad xyz = \lambda(2xz + 2yz) \quad (11)
> $$
>
> Here $\lambda \ne 0$: $\lambda = 0$ would give $yz = xz = xy = 0$ by (5)–(7), contradicting (8). From (9) and (10), $2xz + xy = 2yz + xy$, so $xz = yz$; and $z \ne 0$ (since $z = 0$ would give $V = 0$), so $x = y$. From (10) and (11), $2yz + xy = 2xz + 2yz$, so $xy = 2xz$, and since $x \ne 0$, $y = 2z$. Putting $x = y = 2z$ into (8):
>
> $$
> 4z^2 + 4z^2 + 4z^2 = 12 .
> $$
>
> Since $x$, $y$, $z$ are positive, $z = 1$, $x = 2$, $y = 2$. This is the only point where $V$ can have an extreme value, and there must be a maximum volume (as in Stewart's Example 14.7.6, where the same answer is found by eliminating $z$), so the maximum volume is $V = 2 \cdot 2 \cdot 1 = 4$ m³.
>
> *Stewart: Example 14.8.2*

^ex-97-2

> [!example] Example §97.3: Nearest and Farthest Points on a Sphere
> Find the points on the sphere $x^2 + y^2 + z^2 = 4$ that are closest to and farthest from the point $(3, 1, -1)$.
>
> The algebra is simpler for the square of the distance, $f(x, y, z) = (x - 3)^2 + (y - 1)^2 + (z + 1)^2$, with constraint $g(x, y, z) = x^2 + y^2 + z^2 = 4$. The equations $\nabla f = \lambda \nabla g$, $g = 4$ are
>
> $$
> 2(x - 3) = 2x\lambda \quad (12) \qquad 2(y - 1) = 2y\lambda \quad (13) \qquad 2(z + 1) = 2z\lambda \quad (14) \qquad x^2 + y^2 + z^2 = 4 \quad (15)
> $$
>
> Solve for $x$, $y$, $z$ in terms of $\lambda$. From (12), $x - 3 = x\lambda$, so $x(1 - \lambda) = 3$ and $x = \frac{3}{1 - \lambda}$; here $1 - \lambda \ne 0$, since $\lambda = 1$ would make (12) read $-3 = 0$. Similarly $y = \frac{1}{1 - \lambda}$ and $z = -\frac{1}{1 - \lambda}$. Substituting into (15),
>
> $$
> \frac{3^2}{(1 - \lambda)^2} + \frac{1^2}{(1 - \lambda)^2} + \frac{(-1)^2}{(1 - \lambda)^2} = 4 , \qquad (1 - \lambda)^2 = \frac{11}{4} , \qquad 1 - \lambda = \pm\frac{\sqrt{11}}{2} .
> $$
>
> The corresponding points are
>
> $$
> \Big( \frac{6}{\sqrt{11}}, \frac{2}{\sqrt{11}}, -\frac{2}{\sqrt{11}} \Big) \qquad\text{and}\qquad \Big( -\frac{6}{\sqrt{11}}, -\frac{2}{\sqrt{11}}, \frac{2}{\sqrt{11}} \Big) .
> $$
>
> $f$ is smaller at the first, which is therefore the closest point; the second is the farthest. (Without calculus: the closest point is where the ray from the center $O$ toward $(3, 1, -1)$ meets the sphere, namely $\frac{2}{\sqrt{11}}\langle 3, 1, -1 \rangle$; the distances are $\sqrt{11} - 2$ and $\sqrt{11} + 2$.)
>
> *Stewart: Example 14.8.3*

^ex-97-3

> [!example] Example §97.4: Extreme Values from the Exams
> **(a)** Find the minimum and maximum values of $f(x, y) = e^{xy}$ over the region $D$ given by $x^2 + 4y^2 \le 2$.
>
> $D$ is closed and bounded and $f$ is continuous, so both extremes exist ([[§96 Maximum and Minimum Values#^thm-96-3|Theorem §96.3]]).
>
> **Interior.** $\nabla f = e^{xy}\langle y, x \rangle = \mathbf{0}$ only at $(0, 0)$, where $f = 1$.
>
> **Boundary** $g(x, y) = x^2 + 4y^2 = 2$, with $\nabla g = \langle 2x, 8y \rangle \ne \mathbf{0}$ there. The Lagrange equations are
>
> $$
> ye^{xy} = 2\lambda x , \qquad xe^{xy} = 8\lambda y , \qquad x^2 + 4y^2 = 2 .
> $$
>
> If $x = 0$, the first equation gives $y = 0$, but $(0, 0)$ is not on the boundary; similarly $y = 0$ forces $x = 0$. So $x, y \ne 0$, and then $\lambda \ne 0$. Multiplying the first equation by $8y$, the second by $2x$, and comparing: $8y^2 e^{xy} = 16\lambda xy = 2x^2 e^{xy}$, so $x^2 = 4y^2$. Then $x^2 + x^2 = 2$: $x = \pm 1$, $y = \pm\frac12$ (all four sign combinations). There $xy = \pm\frac12$, so $f = e^{1/2}$ at $(1, \frac12)$ and $(-1, -\frac12)$, and $f = e^{-1/2}$ at $(1, -\frac12)$ and $(-1, \frac12)$.
>
> **Compare** with the interior value $1$: the maximum value is $\sqrt e$ and the minimum value is $1/\sqrt e$, both on the boundary.
>
> **(b)** Let $f(x, y) = x + y$ and let $E$ be the ellipse $x^2 + \frac{y^2}{8} = 1$. Find the minimum and maximum values of $f$ on $E$.
>
> With $g(x, y) = x^2 + y^2/8$, $\nabla f = \lambda \nabla g$ reads $\langle 1, 1 \rangle = \lambda \langle 2x, y/4 \rangle$. In particular $\lambda \ne 0$, and $2\lambda x = 1 = \lambda y/4$ gives $y = 8x$. Substituting into the constraint, $x^2 + 8x^2 = 9x^2 = 1$, so $x = \pm\frac13$ and $(x, y) = (\frac13, \frac83)$ or $(-\frac13, -\frac83)$. The maximum value is $f(\frac13, \frac83) = 3$ and the minimum value is $f(-\frac13, -\frac83) = -3$. (The ellipse is closed and bounded, so these extremes exist.)
>
> *In the posted solution of (b), the line "By $y = 2x$" should read $y = 8x$; the points and the values $\pm 3$ are correct.*
>
> *Source: 233 Exam 2 Practice Questions, Q6; 233 Practice Exam 2, Q2*

^ex-97-4

## Lagrange Multipliers: Two Constraints

> [!theorem] Theorem §97.2: Lagrange Multipliers with Two Constraints
> Suppose $f$ has an extreme value at $P(x_0, y_0, z_0)$ subject to two constraints $g(x, y, z) = k$ and $h(x, y, z) = c$, that is, on the curve of intersection $C$ of these two level surfaces. If the gradient vectors $\nabla g(x_0, y_0, z_0)$ and $\nabla h(x_0, y_0, z_0)$ are not zero and not parallel, then there are numbers $\lambda$ and $\mu$ (both called Lagrange multipliers) such that
>
> $$
> \nabla f(x_0, y_0, z_0) = \lambda\,\nabla g(x_0, y_0, z_0) + \mu\,\nabla h(x_0, y_0, z_0) . \qquad (16)
> $$
>
> In components, extreme values are sought among the solutions of five equations in the five unknowns $x$, $y$, $z$, $\lambda$, $\mu$:
>
> $$
> f_x = \lambda g_x + \mu h_x , \quad f_y = \lambda g_y + \mu h_y , \quad f_z = \lambda g_z + \mu h_z , \quad g(x, y, z) = k , \quad h(x, y, z) = c .
> $$
>
> *Stewart: 14.8, Equation 16*

^thm-97-2

> [!proof]+ Proof
> *Stewart gives this as a sketch.* As at the beginning of the section, $\nabla f$ is orthogonal to $C$ at $P$: if $\mathbf{r}(t)$ parametrizes $C$ with $\mathbf{r}(t_0) = P$, then $t \mapsto f(\mathbf{r}(t))$ has an extreme value at $t_0$, so $\nabla f(P) \cdot \mathbf{r}'(t_0) = 0$. Also $\nabla g$ is orthogonal to the level surface $g = k$ and $\nabla h$ to $h = c$ ([[§95 Directional Derivatives and the Gradient Vector#^thm-95-5|Theorem §95.5]]); since $C$ lies on both, $\nabla g(P)$ and $\nabla h(P)$ are both orthogonal to $\mathbf{r}'(t_0)$. This means that $\nabla f(P)$ lies in the plane determined by $\nabla g(P)$ and $\nabla h(P)$, so $\nabla f(P) = \lambda \nabla g(P) + \mu \nabla h(P)$.
>
> (What makes this a sketch: the last step needs $\mathbf{r}'(t_0) \ne \mathbf{0}$, so that the vectors orthogonal to it form a plane, which then must be the plane spanned by the two independent vectors $\nabla g(P)$ and $\nabla h(P)$; and it needs a curve $\mathbf{r}$ through $P$ along $C$ at all. Both come from the Implicit Function Theorem for two equations, which uses that $\nabla g(P)$ and $\nabla h(P)$ are not parallel.)

^pf-97-2

*Uses:* [[§95 Directional Derivatives and the Gradient Vector#^thm-95-5|§95.5]], [[§94 The Chain Rule#^thm-94-3|§94.3]], [[§97 Lagrange Multipliers#^thm-97-1|§97.1]] (same argument)

> [!remark]- Connections
> - Rigorous treatment: [[§14 Optimization and Lagrange Multipliers#^thm-14-3|452 Thm. §14.3]] ($k$ constraints with linearly independent gradients); "not zero and not parallel" is linear independence of two vectors.

> [!example] Example §97.5: Two Constraints
> Find the maximum value of the function $f(x, y, z) = x + 2y + 3z$ on the curve of intersection of the plane $x - y + z = 1$ and the cylinder $x^2 + y^2 = 1$.
>
> We maximize $f$ subject to $g(x, y, z) = x - y + z = 1$ and $h(x, y, z) = x^2 + y^2 = 1$. The gradients $\nabla g = \langle 1, -1, 1 \rangle$ and $\nabla h = \langle 2x, 2y, 0 \rangle$ are never parallel and never zero on the curve. The Lagrange condition $\nabla f = \lambda \nabla g + \mu \nabla h$ gives
>
> $$
> 1 = \lambda + 2x\mu \quad (17) \qquad 2 = -\lambda + 2y\mu \quad (18) \qquad 3 = \lambda \quad (19) \qquad x - y + z = 1 \quad (20) \qquad x^2 + y^2 = 1 \quad (21)
> $$
>
> Putting $\lambda = 3$ from (19) into (17) gives $2x\mu = -2$, so $x = -1/\mu$; similarly (18) gives $2y\mu = 5$, so $y = 5/(2\mu)$. Substituting in (21),
>
> $$
> \frac{1}{\mu^2} + \frac{25}{4\mu^2} = 1 , \qquad \mu^2 = \frac{29}{4} , \qquad \mu = \pm\frac{\sqrt{29}}{2} .
> $$
>
> Then $x = \mp\frac{2}{\sqrt{29}}$, $y = \pm\frac{5}{\sqrt{29}}$, and from (20), $z = 1 - x + y = 1 \pm \frac{7}{\sqrt{29}}$. The corresponding values of $f$ are
>
> $$
> \mp\frac{2}{\sqrt{29}} + 2\Big( \pm\frac{5}{\sqrt{29}} \Big) + 3\Big( 1 \pm \frac{7}{\sqrt{29}} \Big) = 3 \pm \frac{29}{\sqrt{29}} = 3 \pm \sqrt{29} .
> $$
>
> The curve (an ellipse) is closed and bounded, so the maximum exists: it is $3 + \sqrt{29}$ (and the minimum is $3 - \sqrt{29}$).
>
> *Stewart: Example 14.8.5*

^ex-97-5
