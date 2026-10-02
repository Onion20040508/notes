---
type: section
subject: "[[Complex Variables]]"
chapter: 11
section: 129
bc: "129"
aliases: ["B&C 129"]
tags: [complex-variables, math342, extension]
---
← [[§128★ Schwarz–Christoffel Transformation]] · ↑ [[· 11★ The Schwarz–Christoffel Transformation]] · [[§130★ Degenerate Polygons]] →

*Brown–Churchill, Section 129.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

The Schwarz–Christoffel transformation is written in terms of the prevertices $x_j$, not the vertices, and at most three prevertices can be chosen freely; for a polygon with more than three sides the others must be solved for, which often takes ingenuity; and the integral is rarely elementary. This section works out the two simplest nondegenerate cases. For a triangle all three prevertices are free; for a rectangle the symmetric choice $\pm1$, $\pm a$ leaves one parameter $a$, which fixes the shape. The vertices come out as beta-function and elliptic integrals.

## Triangles

> [!theorem] Corollary §129.1: Mapping onto a Triangle
> If the polygon is a triangle with vertices $w_1, w_2, w_3$ and interior angles $\theta_j$, the transformation can be written
>
> $$
> w = A\int_{z_0}^{z}(s - x_1)^{-k_1}(s - x_2)^{-k_2}(s - x_3)^{-k_3}\,ds + B , \qquad (1)
> $$
>
> where $k_1 + k_2 + k_3 = 2$ and
>
> $$
> k_j = 1 - \frac1\pi\theta_j \qquad (j = 1, 2, 3) ;
> $$
>
> arbitrary real values can be assigned to all three $x_j$, and the complex constants $A$ and $B$ fix the size and position of the triangle. If the vertex $w_3$ is taken as the image of the point at infinity, the transformation becomes
>
> $$
> w = A\int_{z_0}^{z}(s - x_1)^{-k_1}(s - x_2)^{-k_2}\,ds + B , \qquad (2)
> $$
>
> where arbitrary real values can be assigned to $x_1$ and $x_2$.
>
> *B&C: Sec. 129, equations (1)–(2)*

^cor-129-1

> [!proof]+ Proof
> Form (1) is [[§128★ Schwarz–Christoffel Transformation#^cor-128-5|Corollary §128.5]] with $n = 3$, and form (2) is [[§128★ Schwarz–Christoffel Transformation#^thm-128-4|Theorem §128.4]] with $n = 3$. In both cases the number of similarity conditions is $n - 3 = 0$: two triangles with the same angles are similar, so whatever prevertices are chosen, the image is a triangle similar to the given one, and $A$, $B$ then rotate, scale and translate it into place. The relation $k_j = 1 - \theta_j/\pi$ is [[§127★ Mapping the Real Axis onto a Polygon#^def-127-1|Definition §127.1]].

^pf-129-1

*Uses:* [[§128★ Schwarz–Christoffel Transformation#^cor-128-5|§128.5]], [[§128★ Schwarz–Christoffel Transformation#^thm-128-4|§128.4]], [[§127★ Mapping the Real Axis onto a Polygon#^def-127-1|Def. §127.1]]

The integrals in (1) and (2) do not represent elementary functions unless the triangle is degenerate, with one or two vertices at infinity. The integral in (2) becomes an elliptic integral when the triangle is equilateral or when it is a right triangle with one of its angles equal to $\pi/3$ or $\pi/4$. (B&C states these facts without proof.)

> [!example] Example §129.1: An Equilateral Triangle
> For an equilateral triangle $k_1 = k_2 = k_3 = 2/3$. Take $x_1 = -1$, $x_2 = 1$, $x_3 = \infty$ and use (2) with $z_0 = 1$, $A = 1$, $B = 0$:
>
> $$
> w = \int_1^z(s + 1)^{-2/3}(s - 1)^{-2/3}\,ds . \qquad (3)
> $$
>
> **The vertex $w_2$.** The image of $z = 1$ is clearly $w = 0$: $w_2 = 0$.
>
> **The vertex $w_1$.** For $z = -1$, write $s = x$ with $-1 < x < 1$. Then $x + 1 > 0$ and $\arg(x + 1) = 0$, while $|x - 1| = 1 - x$ and $\arg(x - 1) = \pi$. Hence
>
> $$
> w_1 = \int_1^{-1}(x + 1)^{-2/3}(1 - x)^{-2/3}\exp\Big(-\frac{2\pi i}{3}\Big)\,dx = \exp\Big(\frac{\pi i}{3}\Big)\int_0^1\frac{2\,dx}{(1 - x^2)^{2/3}} , \qquad (4)
> $$
>
> using $-e^{-2\pi i/3} = e^{\pi i/3}$ and the evenness of the integrand. With $x = \sqrt t$ the last integral is a beta integral (the beta function of B&C's Exercise 5 of Sec. 91, [[§91★ Integration Along a Branch Cut#^ex-91-4|Example §91.4]]); call its value $b$:
>
> $$
> b = \int_0^1\frac{2\,dx}{(1 - x^2)^{2/3}} = \int_0^1 t^{-1/2}(1 - t)^{-2/3}\,dt = B\Big(\frac12, \frac13\Big) \approx 4.20655 . \qquad (5)
> $$
>
> So $w_1 = b\exp(\pi i/3)$. (6)
>
> **The vertex $w_3$.** It is on the positive $u$ axis, because
>
> $$
> w_3 = \int_1^\infty(x + 1)^{-2/3}(x - 1)^{-2/3}\,dx = \int_1^\infty\frac{dx}{(x^2 - 1)^{2/3}} > 0 .
> $$
>
> But $w_3$ is also the limit of (3) as $z$ tends to infinity along the negative $x$ axis ([[§128★ Schwarz–Christoffel Transformation#^lem-128-3|Lemma §128.3]]). For $x < -1$ both arguments are $\pi$, so the integrand is $(|x + 1||x - 1|)^{-2/3}\exp(-4\pi i/3)$, and
>
> $$
> w_3 = \int_1^{-1}(|x + 1||x - 1|)^{-2/3}e^{-2\pi i/3}\,dx + \int_{-1}^{-\infty}(|x + 1||x - 1|)^{-2/3}e^{-4\pi i/3}\,dx = w_1 + e^{-4\pi i/3}\int_{-1}^{-\infty}\frac{dx}{(x^2 - 1)^{2/3}} .
> $$
>
> In the last integral substitute $x \mapsto -x$: it equals $-\int_1^\infty(x^2 - 1)^{-2/3}\,dx = -w_3$. Since $-e^{-4\pi i/3} = e^{-\pi i/3}$,
>
> $$
> w_3 = b\,e^{\pi i/3} + w_3\,e^{-\pi i/3} , \qquad\text{so}\qquad w_3 = \frac{b\,e^{\pi i/3}}{1 - e^{-\pi i/3}} = \frac{b\,e^{\pi i/3}}{e^{\pi i/3}} = b , \qquad (7)
> $$
>
> because $1 - e^{-\pi i/3} = \frac12 + \frac{\sqrt3}{2}i = e^{\pi i/3}$. So the image of the $x$ axis is the equilateral triangle of side $b$ with vertices $0$, $b$, $be^{\pi i/3}$. Also $w = \frac b2\exp\frac{\pi i}{3}$ when $z = 0$: by symmetry of the integrand, $\int_1^0$ is half of $\int_1^{-1}$.
>
> *Check:* numerical integration of (3) along the axis gives $w_1 = 2.10327 + 3.64298i = b e^{\pi i/3}$ and $w_3 = 4.20655 = b$.
>
> *B&C: Sec. 129, Example 1*

^ex-129-1

![[m342-129-1.svg]]
*The map (3) of Example §129.1, computed by numerical integration. The horizontal lines $y = 0.1, 0.35, 1, 3$ of the upper half plane (blue) become loops that start and end at $w_3 = b$, the image of $z = \infty$; the higher the line, the smaller the loop. The vertical lines $x = -\frac12, 0, \frac12$ (red) run from the side $w_2w_1$ (the image of $-1 < x < 1$) to $w_3$; the imaginary axis goes to the median from the midpoint $\frac b2e^{\pi i/3}$, by symmetry.*

## Rectangles

> [!theorem] Corollary §129.2: Mapping onto a Rectangle
> When the polygon is a rectangle, each $k_j = 1/2$. Choose $\pm1$ and $\pm a$ ($a > 0$, $a \ne 1$) as the prevertices and write
>
> $$
> g(z) = (z + a)^{-1/2}(z + 1)^{-1/2}(z - 1)^{-1/2}(z - a)^{-1/2} , \qquad (8)
> $$
>
> where $0 \le \arg(z - x_j) \le \pi$. Then, except for a transformation $W = Aw + B$ that adjusts size and position, the Schwarz–Christoffel transformation onto a rectangle is
>
> $$
> w = -\int_0^z g(s)\,ds . \qquad (9)
> $$
>
> Integral (9) is a constant times the elliptic integral
>
> $$
> \int_0^z(1 - s^2)^{-1/2}(1 - k^2s^2)^{-1/2}\,ds \qquad \Big(k = \frac1a\Big) .
> $$
>
> *B&C: Sec. 129, equations (8)–(9)*

^cor-129-2

> [!proof]+ Proof
> This is [[§128★ Schwarz–Christoffel Transformation#^cor-128-5|Corollary §128.5]] with $n = 4$, all $k_j = \frac12$ (sum $2$) and $A = -1$, $z_0 = 0$, $B = 0$; the branches with $0 \le \arg(z - x_j) \le \pi$ agree with [[§128★ Schwarz–Christoffel Transformation#^def-128-1|Definition §128.1]] on $y \ge 0$. The image is a polygon with four right angles, a rectangle; here $n - 3 = 1$ condition (the ratio of the sides) is governed by the single parameter $a$, which is how one fits a given rectangle up to similarity ([[§129★ Triangles and Rectangles#^ex-129-2|Example §129.2]] computes the sides).
>
> **The elliptic integral.** (B&C asserts this; here is why.) Let $h(s) = \frac1a(1 - s^2)^{-1/2}\big(1 - \frac{s^2}{a^2}\big)^{-1/2}$ with principal branches; on the half disk $H$: $|s| < \min(1, a)$, $\operatorname{Im} s \ge 0$, the numbers $1 - s^2$ and $1 - s^2/a^2$ have positive real part, so $h$ is continuous there. Both $-g$ and $h$ have square $\big[(s^2 - 1)(s^2 - a^2)\big]^{-1}$, so $-g/h$ is continuous on $H$ with values $\pm1$; since $H$ is connected, it is constant. At $s = 0$, $g(0) = a^{-1/2}\cdot 1\cdot e^{-i\pi/2}\cdot a^{-1/2}e^{-i\pi/2} = -\frac1a = -h(0)$. Hence $-g = h$ on $H$, that is,
>
> $$
> -g(s) = \frac1a(1 - s^2)^{-1/2}\Big(1 - \frac{s^2}{a^2}\Big)^{-1/2} \qquad (s \in H) ,
> $$
>
> and (9) is $\frac1a$ times the elliptic integral with $k = 1/a$ (beyond $H$, its analytic continuation into the upper half plane); the form (8) of the integrand shows more clearly which branches are involved.

^pf-129-2

*Uses:* [[§128★ Schwarz–Christoffel Transformation#^cor-128-5|§128.5]], [[§128★ Schwarz–Christoffel Transformation#^def-128-1|Def. §128.1]]

> [!example] Example §129.2: The Vertices of the Rectangle When a > 1
> Locate the vertices of the rectangle (9) when $a > 1$, with $x_1 = -a$, $x_2 = -1$, $x_3 = 1$, $x_4 = a$.
>
> All four vertices can be described by two positive numbers depending on $a$:
>
> $$
> b = \int_0^1|g(x)|\,dx = \int_0^1\frac{dx}{\sqrt{(1 - x^2)(a^2 - x^2)}} , \qquad (10) \qquad\qquad c = \int_1^a|g(x)|\,dx = \int_1^a\frac{dx}{\sqrt{(x^2 - 1)(a^2 - x^2)}} . \qquad (11)
> $$
>
> **The phase of $g$ on the axis.** Each factor with $x < x_j$ contributes $e^{-\pi i/2} = -i$. So $g(x) = (-i)^m|g(x)|$, where $m$ is the number of prevertices to the right of $x$:
>
> | interval | $m$ | $g(x)$ |
> |---|---|---|
> | $-a < x < -1$ | 3 | $i\,\lvert g(x)\rvert$ |
> | $-1 < x < 1$ | 2 | $-\lvert g(x)\rvert$ |
> | $1 < x < a$ | 1 | $-i\,\lvert g(x)\rvert$ |
>
> **The vertices.** Since $|g|$ is even, $\int_{-1}^0|g| = \int_0^1|g| = b$ and $\int_{-a}^{-1}|g| = \int_1^a|g| = c$. Then
>
> $$
> w_1 = -\int_0^{-a}g(x)\,dx = -\int_0^{-1}g(x)\,dx - \int_{-1}^{-a}g(x)\,dx = \int_0^{-1}|g(x)|\,dx - i\int_{-1}^{-a}|g(x)|\,dx = -b + ic ;
> $$
>
> $$
> w_2 = -\int_0^{-1}g(x)\,dx = \int_0^{-1}|g(x)|\,dx = -b, \qquad w_3 = -\int_0^1g(x)\,dx = \int_0^1|g(x)|\,dx = b ,
> $$
>
> $$
> w_4 = w_3 - \int_1^a g(x)\,dx = b + i\int_1^a|g(x)|\,dx = b + ic . \qquad (12)
> $$
>
> So the rectangle has vertices $-b + ic$, $-b$, $b$, $b + ic$: width $2b$, height $c$, symmetric about the $v$ axis. In terms of the complete elliptic integral $K(k) = \int_0^1\big[(1 - t^2)(1 - k^2t^2)\big]^{-1/2}dt$, the substitutions $x = t$ and $x = \sqrt{a^2 - (a^2 - 1)t^2}$ give $b = K(1/a)/a$ and $c = K(k')/a$ with $k' = \sqrt{1 - 1/a^2}$. For $a = 2$: $b = 0.842875$ and $c = 1.078258$ (both by direct quadrature of (10)–(11) and from $K$), and numerical integration of (9) along the axis reproduces $w_1 = -0.842875 + 1.078258i$ and $w_4 = 0.842875 + 1.078258i$.
>
> *B&C: Sec. 129, Example 2; Sec. 130, Exercise 2*

^ex-129-2

> [!example] Example §129.3: The Case 0 < a < 1
> Show that when $0 < a < 1$ in (8) the vertices are again $-b + ic$, $-b$, $b$, $b + ic$, where now
>
> $$
> b = \int_0^a|g(x)|\,dx , \qquad c = \int_a^1|g(x)|\,dx .
> $$
>
> Now the prevertices in increasing order are $-1, -a, a, 1$, and $w_1, w_2, w_3, w_4$ are the images of $-1, -a, a, 1$. The phase count of Example §129.2 is unchanged: $g = -|g|$ on $-a < x < a$ (two prevertices to the right), $g = i|g|$ on $-1 < x < -a$, $g = -i|g|$ on $a < x < 1$. Hence, exactly as before,
>
> $$
> w_2 = -\int_0^{-a}g = -b, \quad w_3 = -\int_0^{a}g = b, \quad w_1 = w_2 - \int_{-a}^{-1}g = -b + ic, \quad w_4 = w_3 - \int_a^1 g = b + ic .
> $$
>
> For $a = \frac12$, numerical integration gives $b = 1.685750$, $c = 2.156516$, and $w(\pm1) = \pm1.685750 + 2.156516i$. These are exactly twice the values for $a = 2$, as they must be: the substitution $s = a\sigma$ turns the integral for $a$ into $\frac1a$ times the integral for $1/a$.
>
> *B&C: Sec. 130, Exercise 3*

^ex-129-3

> [!example] Example §129.4: An Isosceles Right Triangle
> In transformation (1) write $z_0 = 0$, $B = 0$, and
>
> $$
> A = \exp\frac{3\pi i}{4}, \quad x_1 = -1, \quad x_2 = 0, \quad x_3 = 1, \quad k_1 = \frac34, \quad k_2 = \frac12, \quad k_3 = \frac34 .
> $$
>
> Show that the image of the axis is the isosceles right triangle with vertices $w_1 = bi$, $w_2 = 0$, $w_3 = b$, where $b = \int_0^1(1 - x^2)^{-3/4}x^{-1/2}\,dx$, and that $2b = B\big(\frac14, \frac14\big)$.
>
> **$w_2$.** $w(0) = 0$ since $z_0 = 0$.
>
> **$w_3$.** For $0 < x < 1$, only $\arg(x - 1) = \pi$, so the integrand is $(x + 1)^{-3/4}x^{-1/2}(1 - x)^{-3/4}e^{-3\pi i/4}$, and
>
> $$
> w_3 = e^{3\pi i/4}e^{-3\pi i/4}\int_0^1 x^{-1/2}(1 - x^2)^{-3/4}\,dx = b .
> $$
>
> **$w_1$.** For $-1 < x < 0$, $\arg x = \arg(x - 1) = \pi$, so the integrand is $|x|^{-1/2}(1 - x^2)^{-3/4}e^{-i\pi/2}e^{-3\pi i/4} = |x|^{-1/2}(1 - x^2)^{-3/4}e^{-5\pi i/4}$. With $x = -t$,
>
> $$
> w_1 = e^{3\pi i/4}\int_0^{-1}(\ldots)\,dx = -e^{3\pi i/4}e^{-5\pi i/4}\int_0^1 t^{-1/2}(1 - t^2)^{-3/4}\,dt = -e^{-\pi i/2}\,b = bi .
> $$
>
> **The beta function.** With $t = x^2$, $dx = \frac12t^{-1/2}dt$,
>
> $$
> b = \int_0^1 t^{-1/4}(1 - t)^{-3/4}\cdot\frac12t^{-1/2}\,dt = \frac12\int_0^1 t^{-3/4}(1 - t)^{-3/4}\,dt = \frac12B\Big(\frac14, \frac14\Big) \approx 3.70815 .
> $$
>
> The angles: $k = \frac34$ at $w_1$ and $w_3$ (interior angle $\pi/4$) and $k = \frac12$ at $w_2 = 0$ (right angle), consistent with the vertices found.
>
> *B&C: Sec. 130, Exercise 1*

^ex-129-4

> [!example] Example §129.5: A Square
> Show that the special case
>
> $$
> w = i\int_0^z(s + 1)^{-1/2}(s - 1)^{-1/2}s^{-1/2}\,ds
> $$
>
> of (7) in [[§128★ Schwarz–Christoffel Transformation#^thm-128-4|Theorem §128.4]] maps the $x$ axis onto the square with vertices $w_1 = bi$, $w_2 = 0$, $w_3 = b$, $w_4 = b + ib$, where $2b = B\big(\frac14, \frac12\big)$.
>
> Let $b = \int_0^1 x^{-1/2}(1 - x^2)^{-1/2}\,dx$; with $t = x^2$ this is $\frac12\int_0^1 t^{-3/4}(1 - t)^{-1/2}\,dt = \frac12B\big(\frac14, \frac12\big) \approx 2.62206$.
>
> - **$w_3$.** On $0 < x < 1$ only $\arg(x - 1) = \pi$: the integrand is $-i\,x^{-1/2}(1 - x^2)^{-1/2}$, and $w_3 = i \cdot (-i)\,b = b$.
> - **$w_1$.** On $-1 < x < 0$, $\arg x = \arg(x - 1) = \pi$: the integrand is $(-i)^2|\ldots| = -|x|^{-1/2}(1 - x^2)^{-1/2}$, and $\int_0^{-1}\big(-|\ldots|\big)\,dx = \int_{-1}^0|\ldots|\,dx = b$, so $w_1 = ib$.
> - **$w_4$.** On $x > 1$ all arguments are $0$, so $w_4 = w_3 + i\int_1^\infty x^{-1/2}(x^2 - 1)^{-1/2}\,dx$. The substitution $x = 1/u$ turns the integral into $\int_0^1 u^{-1/2}(1 - u^2)^{-1/2}\,du = b$, so $w_4 = b + ib$.
>
> Four equal sides and four right angles: a square. Numerical integration along the axis gives $w(1) = 2.622058$ and $w(-1) = 2.622058\,i$.
>
> *B&C: Sec. 130, Exercise 4*

^ex-129-5
