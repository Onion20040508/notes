---
type: section
subject: "[[Complex Variables]]"
chapter: 1
section: 4
bc: "4"
aliases: ["B&C 4"]
tags: [complex-variables, math342]
---
← [[§3 Further Algebraic Properties]] · ↑ [[· 1 Complex Numbers]] · [[§5 Triangle Inequality]] →

*Brown–Churchill, Section 4 · MAT 342 HW 1.*

A complex number $z = x + iy$ can be pictured as the point $(x, y)$ or as the vector from the origin to that point. Addition of complex numbers is then addition of vectors, by the parallelogram rule. The length of the vector is the modulus $|z|$, the complex version of the absolute value, and $|z_1 - z_2|$ is the distance between two points. This turns plane geometry into algebra: the circle with center $z_0$ and radius $R$ is the equation $|z - z_0| = R$, and an ellipse is a sum of two moduli. Moduli are what make sense of "size" and "closeness" for complex numbers, since $z_1 < z_2$ means nothing unless both are real.

## Complex Numbers as Vectors

Any nonzero $z = x + iy$ is associated with the directed line segment, or **radius vector**, from the origin to the point $(x, y)$, and one speaks of "the point $z$" or "the vector $z$". If $z_1 = x_1 + iy_1$ and $z_2 = x_2 + iy_2$, the sum $z_1 + z_2 = (x_1 + x_2) + i(y_1 + y_2)$ corresponds to the point $(x_1 + x_2, y_1 + y_2)$ and to the vector with those components: $z_1 + z_2$ is obtained from the vectors $z_1$ and $z_2$ by the parallelogram rule. The product $z_1z_2$ is also represented by a vector in the same plane, so it is neither the scalar nor the vector product of vector analysis.

> [!definition] Definition §4.1: Modulus
> The **modulus**, or absolute value, of $z = x + iy$ is the nonnegative real number
>
> $$
> |z| = \sqrt{x^2 + y^2} . \qquad (1)
> $$
>
> Geometrically, $|z|$ is the distance between the point $(x, y)$ and the origin, or the length of the radius vector representing $z$. When $y = 0$ it is the usual absolute value of the real number $x$. While the inequality $z_1 < z_2$ is meaningless unless both $z_1$ and $z_2$ are real, the statement $|z_1| < |z_2|$ means that the point $z_1$ is closer to the origin than the point $z_2$.
>
> *B&C: Sec. 4, Equation (1)*

^def-4-1

> [!remark]- Connections
> - Linear Algebra's absolute value is the same definition, [[§13 Polynomials#^ladr-4-2|LADR 4.2]], with its properties in [[§13 Polynomials#^ladr-4-4|LADR 4.4]].
> - Computational version and the complex plane: [[§53 Complex Numbers#^def-53-4|235 Def. §53.4]], [[§53 Complex Numbers#^def-53-5|235 Def. §53.5]].

> [!theorem] Proposition §4.1: Modulus and the Real and Imaginary Parts
> For every complex number $z$,
>
> $$
> |z|^2 = (\operatorname{Re} z)^2 + (\operatorname{Im} z)^2 , \qquad (2)
> $$
>
> and therefore
>
> $$
> \operatorname{Re} z \le |\operatorname{Re} z| \le |z| \qquad\text{and}\qquad \operatorname{Im} z \le |\operatorname{Im} z| \le |z| . \qquad (3)
> $$
>
> *B&C: Sec. 4, Equations (2)–(3); Sec. 5, Exercise 2*

^prop-4-1

> [!proof]+ Proof
> Squaring (1) gives (2). In (3), $t \le |t|$ holds for every real $t$. For the second inequality, $|x| = \sqrt{x^2} \le \sqrt{x^2 + y^2} = |z|$, since $x^2 \le x^2 + y^2$ and the square root is increasing; likewise $|y| \le |z|$.

^pf-4-1

*Uses:* [[§4 Vectors and Moduli#^def-4-1|Def. §4.1]]

## Distance and Circles

> [!theorem] Proposition §4.2: Distance Between Two Points
> The distance between the points $(x_1, y_1)$ and $(x_2, y_2)$ is $|z_1 - z_2|$:
>
> $$
> |z_1 - z_2| = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2} .
> $$
>
> *B&C: Sec. 4 (text)*

^prop-4-2

> [!proof]+ Proof
> By (5) of §3, $z_1 - z_2 = (x_1 - x_2) + i(y_1 - y_2)$, and (1) gives the formula, which is the Euclidean distance between the two points. Geometrically, $|z_1 - z_2|$ is the length of the vector $z_1 - z_2 = z_1 + (-z_2)$; translated so that it starts at $(x_2, y_2)$, this vector is the directed segment from $(x_2, y_2)$ to $(x_1, y_1)$.

^pf-4-2

*Uses:* [[§3 Further Algebraic Properties#^prop-3-2|§3.2]], [[§4 Vectors and Moduli#^def-4-1|Def. §4.1]]

> [!definition] Definition §4.2: The Circle |z − z0| = R
> The complex numbers $z$ corresponding to the points on the circle with center $z_0$ and radius $R$ are exactly those satisfying
>
> $$
> |z - z_0| = R ,
> $$
>
> and this set of points is referred to simply as **the circle $|z - z_0| = R$**.
>
> *B&C: Sec. 4 (text)*

^def-4-2

By Proposition §4.2, the inequality $|z - z_0| < R$ describes the points inside the circle and $|z - z_0| > R$ the points outside it.

## Examples

> [!example] Example §4.1: Which Point Is Closer to the Origin
> Since $|-3 + 2i| = \sqrt{9 + 4} = \sqrt{13}$ and $|1 + 4i| = \sqrt{1 + 16} = \sqrt{17}$, the point $-3 + 2i$ is closer to the origin than $1 + 4i$ is.
>
> *B&C: Sec. 4, Example 1*

^ex-4-1

> [!example] Example §4.2: Sum and Difference as Vectors
> Locate $z_1 + z_2$ and $z_1 - z_2$ vectorially when $z_1 = 2i$ and $z_2 = \frac23 - i$.
>
> Componentwise,
>
> $$
> z_1 + z_2 = \frac23 + (2 - 1)i = \frac23 + i, \qquad z_1 - z_2 = -\frac23 + (2 + 1)i = -\frac23 + 3i .
> $$
>
> The sum is the diagonal from $0$ of the parallelogram spanned by $z_1$ and $z_2$. The difference is $z_1 + (-z_2)$, the diagonal of the parallelogram spanned by $z_1$ and $-z_2 = -\frac23 + i$; it is also the vector from the tip of $z_2$ to the tip of $z_1$, translated to start at the origin. Its length is the distance between the points $z_1$ and $z_2$: $|z_1 - z_2| = \sqrt{\frac49 + 9} = \frac{\sqrt{85}}{3}$.
>
> *B&C: Sec. 5, Exercise 1(a); Source: 342 HW 1*

^ex-4-2

![[m342-4-1.svg]]
*Example §4.2: the sum $z_1 + z_2$ (blue) is the diagonal of the parallelogram on $z_1 = 2i$ and $z_2 = \frac23 - i$; the difference $z_1 - z_2$ (red) is the diagonal of the parallelogram on $z_1$ and $-z_2$, parallel and equal in length to the dashed segment from $z_2$ to $z_1$.*

> [!example] Example §4.3: Circles and Disks
> **(a)** The equation $|z - 1 + 3i| = 2$ is $|z - (1 - 3i)| = 2$: it represents the circle with center $z_0 = (1, -3)$ and radius $R = 2$.
>
> **(b)** Sketch the set $|z + i| \le 3$. It is $|z - (-i)| \le 3$: the points whose distance from $-i$ is at most $3$, that is, the circle with center $(0, -1)$ and radius $3$ together with its interior (a closed disk). It reaches from $-4i$ to $2i$ along the imaginary axis, and its boundary circle crosses the real axis where $x^2 + 1 = 9$, at $x = \pm 2\sqrt2$.
>
> *B&C: Sec. 4, Example 2; Sec. 5, Exercise 5(b); Source: 342 HW 1 (part (b))*

^ex-4-3

> [!example] Example §4.4: An Ellipse
> Describe the set of points $z = (x, y)$ with $|z - 4i| + |z + 4i| = 10$.
>
> Writing the equation as $|z - 4i| + |z - (-4i)| = 10$ shows that it represents the set of all points $P(x, y)$ the sum of whose distances from the two fixed points $F(0, 4)$ and $F'(0, -4)$ is the constant $10$. This is an ellipse with foci $F$ and $F'$, found without any computation. Its semi-major axis is $a = 5$ (half the constant sum), the focal distance is $c = 4$, and the semi-minor axis is $b = \sqrt{a^2 - c^2} = 3$: the ellipse is $\dfrac{x^2}{9} + \dfrac{y^2}{25} = 1$.
>
> *B&C: Sec. 4, Example 3*

^ex-4-4
