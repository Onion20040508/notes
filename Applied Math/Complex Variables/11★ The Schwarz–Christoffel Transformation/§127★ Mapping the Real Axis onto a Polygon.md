---
type: section
subject: "[[Complex Variables]]"
chapter: 11
section: 127
bc: "127"
aliases: ["B&C 127"]
tags: [complex-variables, math342, extension]
---
← [[§126★ Flows Around a Corner and Around a Cylinder]] · ↑ [[· 11★ The Schwarz–Christoffel Transformation]] · [[§128★ Schwarz–Christoffel Transformation]] →

*Brown–Churchill, Section 127.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Chapter 11 constructs the Schwarz–Christoffel transformation, which maps the $x$ axis and the upper half of the $z$ plane onto a given simple closed polygon and its interior, the kind of boundary that plates, channels and steps present in electrostatics and fluid flow; this section finds what its derivative must be. Along the real axis the image moves in the direction $\arg f'(x)$, so a polygon is traced exactly when $\arg f'(x)$ is constant between certain points $x_j$ and jumps there by the exterior angles of the polygon; a product of powers $(z - x_j)^{-k_j}$ does this. Since the exterior angles of a closed polygon add up to $2\pi$, the exponents must satisfy $k_1 + \cdots + k_n = 2$.

## Direction of the Image of the Real Axis

Let $t$ be the unit tangent vector to a smooth arc $C$ at $z_0$ and $\tau$ the unit tangent to the image of $C$ at $w_0 = f(z_0)$. If $f$ is analytic at $z_0$ and $f'(z_0) \ne 0$, then by [[§112★ Preservation of Angles and Scale Factors#^thm-112-1|Theorem §112.1]]

$$
\arg\tau = \arg f'(z_0) + \arg t . \qquad (1)
$$

If $C$ is a segment of the $x$ axis with positive sense to the right, then $t = 1$ and $\arg t = 0$ at each point $z_0 = x$, and (1) becomes

$$
\arg\tau = \arg f'(x) . \qquad (2)
$$

> [!theorem] Proposition §127.1: Constant Argument Gives a Straight Image
> Let $f$ be continuous on a segment $a \le x \le b$ of the $x$ axis and analytic at each point of $a < x < b$, with $f'(x) \ne 0$ there, and suppose that $\arg f'(x)$ has a constant value $\alpha$ on $a < x < b$. Then, as $x$ increases from $a$ to $b$, the point $w = f(x)$ moves monotonically along a straight line in the direction $e^{i\alpha}$, and the image of the segment is the line segment from $f(a)$ to $f(b)$.
>
> *B&C: Sec. 127 (text)*

^prop-127-1

> [!proof]+ Proof
> B&C reads this off from (2): the tangent to the image has the constant direction $\alpha$, "hence the image is a segment of a straight line." Here is the integral form of that argument. For $a < x < b$ the function $w(x) = f(x)$ of the real variable $x$ has derivative $w'(x) = f'(x)$ (the derivative of $f$ may be computed along the real axis), and $f'$ is continuous since $f$ is analytic. So for $a < x_1 < x < b$, by the fundamental theorem of calculus for complex-valued functions of a real variable,
>
> $$
> f(x) - f(x_1) = \int_{x_1}^{x} f'(t)\,dt = e^{i\alpha}\int_{x_1}^{x}|f'(t)|\,dt .
> $$
>
> The last integral is a strictly increasing real function of $x$, because $|f'(t)| > 0$. Hence $f(x)$ moves along the line through $f(x_1)$ with direction $e^{i\alpha}$, always forward. Letting $x_1 \to a$ and $x \to b$ and using the continuity of $f$ at $a$ and $b$, the image of $a \le x \le b$ is the segment from $f(a)$ to $f(b)$, traced once.

^pf-127-1

*Uses:* [[§42 Definite Integrals of Functions w(t)#^thm-42-2|§42.2]] (fundamental theorem of calculus for $w(t)$), [[§112★ Preservation of Angles and Scale Factors#^thm-112-1|§112.1]]

## The Derivative of the Mapping Function

We want a transformation $w = f(z)$ mapping the whole $x$ axis onto a polygon of $n$ sides, where $x_1, x_2, \ldots, x_{n-1}$ and $\infty$ are the points of the axis whose images are to be the vertices, and

$$
x_1 < x_2 < \cdots < x_{n-1} .
$$

The vertices are the $n$ points $w_j = f(x_j)$ $(j = 1, 2, \ldots, n - 1)$ and $w_n = f(\infty)$. By Proposition §127.1, $f$ should be such that $\arg f'(z)$ jumps from one constant value to another at the points $z = x_j$ as $z$ traces out the $x$ axis.

> [!theorem] Proposition §127.2: The Argument of the Derivative Jumps at the Points x_j
> Let
>
> $$
> f'(z) = A(z - x_1)^{-k_1}(z - x_2)^{-k_2}\cdots(z - x_{n-1})^{-k_{n-1}} , \qquad (3)
> $$
>
> where $A$ is a nonzero complex constant and each $k_j$ is a real constant, the powers being taken with $\arg(x - x_j) = \pi$ for $x < x_j$ and $\arg(x - x_j) = 0$ for $x > x_j$ (the branches of [[§128★ Schwarz–Christoffel Transformation#^def-128-1|Definition §128.1]]). Then on the real axis
>
> $$
> \arg f'(x) = \arg A - k_1\arg(x - x_1) - k_2\arg(x - x_2) - \cdots - k_{n-1}\arg(x - x_{n-1}) . \qquad (4)
> $$
>
> So $\arg f'(x)$ is constant on each of the intervals $x < x_1$, $x_1 < x < x_2$, $\ldots$, $x > x_{n-1}$, and it **increases abruptly by $k_j\pi$** as $x$ moves to the right through $x_j$.
>
> *B&C: Sec. 127, equations (3)–(4)*

^prop-127-2

> [!proof]+ Proof
> On the real axis each factor is $(x - x_j)^{-k_j} = |x - x_j|^{-k_j}\exp\big(-ik_j\arg(x - x_j)\big)$, so
>
> $$
> f'(x) = A\prod_{j=1}^{n-1}|x - x_j|^{-k_j}\cdot\exp\Big(-i\pi\sum_{x_j > x}k_j\Big) ,
> $$
>
> where the sum runs over the $x_j$ to the right of $x$. The product of moduli is positive, so this is (4). For $x < x_1$ every $\arg(x - x_j)$ is $\pi$; for $x_1 < x < x_2$, $\arg(x - x_1) = 0$ and the others are $\pi$; and so on. As $x$ passes through $x_j$, the index $j$ leaves the sum, so the argument increases by exactly $k_j\pi$, and between consecutive $x_j$ nothing changes.

^pf-127-2

*Uses:* [[§128★ Schwarz–Christoffel Transformation#^def-128-1|Def. §128.1]]

By (2) and Proposition §127.1, the unit vector $\tau$ is constant in direction as $z$ moves from $x_{j-1}$ to $x_j$, so $w$ moves in that fixed direction along a straight line; the direction of $\tau$ changes abruptly by the angle $k_j\pi$ at the image point $w_j$ of $x_j$. Those angles are the exterior angles of the polygon described by $w$.

> [!definition] Definition §127.1: Exterior Angle
> Let a polygon be traversed in a given direction. The **exterior angle** at a vertex $w_j$ is the angle $k_j\pi$ through which the direction of travel turns at $w_j$, counted positive counterclockwise and limited to $-\pi < k_j\pi < \pi$, that is, $-1 < k_j < 1$. For a positively oriented polygon with interior angle $\theta_j$ at $w_j$,
>
> $$
> k_j = 1 - \frac{\theta_j}{\pi} .
> $$
>
> *B&C: Sec. 127 (text) and Sec. 129 (text)*

^def-127-1

![[m342-127-1.svg]]
*How the arguments of Proposition §127.2 build a polygon, for $f'(z) = i(z + 1)^{-1/2}z^{-1/2}(z - 1)^{-1/2}$ ([[§127★ Mapping the Real Axis onto a Polygon#^ex-127-2|Example §127.2]]). Each interval of the $x$ axis (left) goes to the side of the same colour (right), traced in the direction of the arrow. At each of $-1$, $0$, $1$ and at $\infty$ the direction turns left by $\pi/2$, the exterior angle of the square.*

> [!theorem] Proposition §127.3: Conditions on the Exponents
> Suppose the sides never cross one another and the polygon is positively (counterclockwise) oriented. Then the exterior angle at the vertex $w_n$, the image of $z = \infty$, is
>
> $$
> k_n\pi = 2\pi - (k_1 + k_2 + \cdots + k_{n-1})\pi ,
> $$
>
> so the numbers $k_j$ must satisfy
>
> $$
> k_1 + k_2 + \cdots + k_{n-1} + k_n = 2, \qquad -1 < k_j < 1 \quad (j = 1, 2, \ldots, n) . \qquad (5)
> $$
>
> In particular $k_n = 0$ if
>
> $$
> k_1 + k_2 + \cdots + k_{n-1} = 2 . \qquad (6)
> $$
>
> Then the direction of $\tau$ does not change at $w_n$: $w_n$ is not a vertex, and the polygon has $n - 1$ sides.
>
> *B&C: Sec. 127, equations (5)–(6)*

^prop-127-3

> [!proof]+ Proof
> B&C uses that the exterior angles of a simple closed polygon, traversed counterclockwise, add up to $2\pi$. (Here is why: a simple polygon with $n$ vertices can be cut by diagonals into $n - 2$ triangles, so its interior angles add up to $(n - 2)\pi$; with $k_j\pi = \pi - \theta_j$ from Definition §127.1, $\sum k_j\pi = n\pi - (n - 2)\pi = 2\pi$. The triangulation is a fact of plane geometry that the vault does not prove.) The turns at $w_1, \ldots, w_{n-1}$ are $k_1\pi, \ldots, k_{n-1}\pi$ by Proposition §127.2, so the turn at $w_n$ is what remains of $2\pi$; this is (5). If (6) holds, the turn at $w_n$ is $0$: the two sides meeting there lie on one line, traced in the same direction, so $w_n$ is not a vertex.

^pf-127-3

*Uses:* [[§127★ Mapping the Real Axis onto a Polygon#^def-127-1|Def. §127.1]], [[§127★ Mapping the Real Axis onto a Polygon#^prop-127-2|§127.2]]

The existence of a mapping function $f$ whose derivative is (3), and the fact that it maps the half plane onto the inside of the polygon, are established in [[§128★ Schwarz–Christoffel Transformation#^thm-128-4|Theorem §128.4]].

## Examples

> [!example] Example §127.1: Reading Off the Exponents
> Find the exponents $k_j = 1 - \theta_j/\pi$ for the polygons used in the next sections, and check (5).
>
> - **Equilateral triangle** ([[§129★ Triangles and Rectangles#^ex-129-1|Example §129.1]]): $\theta_j = \pi/3$, so $k_1 = k_2 = k_3 = 2/3$, and $3 \cdot \frac23 = 2$.
> - **Rectangle** ([[§129★ Triangles and Rectangles#^ex-129-2|Example §129.2]]): $\theta_j = \pi/2$, so every $k_j = 1/2$, and $4 \cdot \frac12 = 2$.
> - **Isosceles right triangle** ([[§129★ Triangles and Rectangles#^ex-129-4|Example §129.4]]): $\theta = \pi/4, \pi/2, \pi/4$, so $k = \frac34, \frac12, \frac34$, with sum $2$.
> - **Regular $n$-gon** ([[§128★ Schwarz–Christoffel Transformation#^ex-128-2|Example §128.2]]): $\theta_j = (n - 2)\pi/n$, so $k_j = 2/n$, with sum $2$.
> - **Half strip** $-\pi/2 \le u \le \pi/2$, $v \ge 0$ ([[§130★ Degenerate Polygons#^ex-130-1|Example §130.1]]): the two corners have $\theta = \pi/2$, $k = \frac12$; the "vertex at infinity" has interior angle $0$, so formally $k_3 = 1$, outside the range $-1 < k < 1$ of (5). Such **degenerate polygons** fall outside Proposition §127.3 and are handled formally in [[§130★ Degenerate Polygons|§130★]].
>
> For a vertex whose interior angle exceeds $\pi$ (a reentrant corner) $k_j$ is negative: the offset channel of [[§132★ Flow in a Channel with an Offset|§132★]] has $k_3 = -\frac12$ at the corner where the wall turns right.
>
> *B&C: Sec. 127 (text), applied to the polygons of Secs. 128–132*

^ex-127-1

> [!example] Example §127.2: Tracing a Square
> Let $f'(z) = i(z + 1)^{-1/2}z^{-1/2}(z - 1)^{-1/2}$, so $A = i$, $x_1 = -1$, $x_2 = 0$, $x_3 = 1$, $k_1 = k_2 = k_3 = \frac12$. Find the direction of the image on each interval of the axis.
>
> By (4), $\arg f'(x) = \frac\pi2 - \frac\pi2\cdot(\text{number of } x_j \text{ to the right of } x)$:
>
> | interval | $x_j$ to the right | $\arg f'(x)$ | direction of $w$ |
> |---|---|---|---|
> | $x < -1$ | 3 | $-\pi$ | west |
> | $-1 < x < 0$ | 2 | $-\pi/2$ | south |
> | $0 < x < 1$ | 1 | $0$ | east |
> | $x > 1$ | 0 | $\pi/2$ | north |
>
> The direction turns left by $\pi/2$ at each of the three images $w_1, w_2, w_3$, and once more, from north to west, at $w_4 = f(\infty)$: $k_4 = 2 - \frac32 = \frac12$ by (5). So the image is a rectangle traversed counterclockwise. That it is the square with vertices $bi, 0, b, b + ib$, $b = \frac12 B\big(\frac14, \frac12\big)$, is computed in [[§129★ Triangles and Rectangles#^ex-129-5|Example §129.5]].
>
> *B&C: Sec. 127, equation (4); the derivative is that of Sec. 130, Exercise 4*

^ex-127-2

> [!example] Example §127.3: The Image of Infinity Need Not Be a Vertex
> Let $f'(z) = (z + 1)^{-2/3}z^{-2/3}(z - 1)^{-2/3}$. Show that the image of the axis has only three vertices.
>
> Here $k_1 + k_2 + k_3 = 3 \cdot \frac23 = 2$, which is (6), so $k_4 = 0$. Directly from (4) with $A = 1$: for $x > 1$, $\arg f'(x) = 0$; for $x < -1$, $\arg f'(x) = -\frac23\pi \cdot 3 = -2\pi$, the same direction. The half lines $x < -1$ and $x > 1$ therefore go to two collinear pieces of one side, joined at $f(\infty)$, which is an ordinary point of that side. The jumps $\frac23\pi$ at $-1$, $0$, $1$ are the exterior angles of an equilateral triangle. This is the form (1) of [[§129★ Triangles and Rectangles#^cor-129-1|Corollary §129.1]] with all three prevertices finite.
>
> *B&C: Sec. 127, equation (6); Sec. 129, equation (1)*

^ex-127-3
