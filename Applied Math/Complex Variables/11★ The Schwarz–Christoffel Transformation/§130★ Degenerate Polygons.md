---
type: section
subject: "[[Complex Variables]]"
chapter: 11
section: "130★"
bc: "130"
aliases: ["B&C 130"]
tags: [complex-variables, math342, extension]
---
← [[§129★ Triangles and Rectangles]] · ↑ [[· 11★ The Schwarz–Christoffel Transformation]] · [[§131★ Fluid Flow in a Channel through a Slit]] →

*Brown–Churchill, Section 130.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

A degenerate polygon has one or more vertices at infinity: a half strip, a strip, a wedge, a half plane with a slit. For these the Schwarz–Christoffel integral is elementary, and the examples recover maps already met in Chapter 8. The derivation treats such a region as a limit of genuine polygons and uses the limiting exterior angles (an angle $\pi$ at a vertex at infinity between parallel sides, $-\pi$ at the tip of a slit) without justifying the limits; the resulting map is then checked directly. These are the maps behind the channel and plate problems of [[§131★ Fluid Flow in a Channel through a Slit|§131★]]–[[§133★ Electrostatic Potential about an Edge of a Conducting Plate|§133★]].

> [!remark] Remark: The Formal Method
> The procedure used in this section is not rigorous, because limiting values of angles and coordinates are not introduced in an orderly way; limiting values are used whenever it seems expedient. But if the mapping obtained is verified, it is not essential that the steps of its derivation be justified. The formal method is shorter and less tedious than rigorous methods. In each example below, the last step is that verification, either directly or by a reference to Chapter 8.

^rem-130-1

> [!example] Example §130.1: A Half Strip and the Sine Function
> Map the half plane $y \ge 0$ onto the semi-infinite strip
>
> $$
> -\frac\pi2 \le u \le \frac\pi2, \qquad v \ge 0 .
> $$
>
> **Angles.** Consider the strip as the limiting form of a triangle with vertices $w_1 = -\pi/2$, $w_2 = \pi/2$ and $w_3$, as the imaginary part of $w_3$ tends to infinity. The limiting [[§127★ Mapping the Real Axis onto a Polygon#^def-127-1|exterior angles]] are
>
> $$
> k_1\pi = k_2\pi = \frac\pi2 \qquad\text{and}\qquad k_3\pi = \pi .
> $$
>
> **Derivative.** Choose $x_1 = -1$, $x_2 = 1$, $x_3 = \infty$ as the points whose images are the vertices. Then
>
> $$
> \frac{dw}{dz} = A(z + 1)^{-1/2}(z - 1)^{-1/2} = A'(1 - z^2)^{-1/2} ,
> $$
>
> since $(z + 1)(z - 1) = -(1 - z^2)$ and the resulting constant factor of modulus one is absorbed into $A'$.
>
> **Integrate.** Hence $w = A'\sin^{-1}z + B$. Writing $A' = 1/a$ and $B = b/a$, this is
>
> $$
> z = \sin(aw - b) .
> $$
>
> **Constants.** The conditions $z = -1$ when $w = -\pi/2$ and $z = 1$ when $w = \pi/2$ are satisfied with $a = 1$ and $b = 0$: $\sin(\mp\pi/2) = \mp1$. The transformation is
>
> $$
> z = \sin w .
> $$
>
> **Verification.** With the $z$ and $w$ planes interchanged, this is the map of [[§104★ Mapping Vertical Line Segments by w = sin z#^ex-104-1|Example §104.1]], which takes the half strip $-\pi/2 \le x \le \pi/2$, $y \ge 0$ one to one onto the half plane $v \ge 0$.
>
> *B&C: Sec. 130, Example 1*

^ex-130-1

*Chain: the sine half strip earlier in [[§111a Three Linear Fractional Maps, the Sine Half Strip and ((z − 1)∕(z + 1))^(1∕2)#The Sine Half Strip|Chapter 8]] · [[§113★ Further Examples (Preservation of Angles and Scale Factors)#^ex-113-3|Chapter 9]] · [[§126a The Heated Segment, the Quadrant, the Sine Half Strip and Flow Around a Corner#The Sine Half Strip|Chapter 10]]*

> [!example] Example §130.2: A Strip and the Logarithm
> Map the half plane $y > 0$ onto the strip $0 < v < \pi$.
>
> **Angles.** Consider the strip as the limiting form of a rhombus with vertices $w_1 = \pi i$, $w_2$, $w_3 = 0$, $w_4$, as $w_2$ and $w_4$ are moved infinitely far to the left and right, respectively. In the limit the exterior angles become
>
> $$
> k_1\pi = 0, \qquad k_2\pi = \pi, \qquad k_3\pi = 0, \qquad k_4\pi = \pi .
> $$
>
> **Derivative.** Leave $x_1$ to be determined and choose $x_2 = 0$, $x_3 = 1$, $x_4 = \infty$. Then
>
> $$
> \frac{dw}{dz} = A(z - x_1)^0z^{-1}(z - 1)^0 = \frac Az , \qquad\text{so}\qquad w = A\operatorname{Log}z + B .
> $$
>
> **Constants.** $B = 0$ because $w = 0$ when $z = 1$. The constant $A$ must be real, because $w$ lies on the real axis when $z = x > 0$. The point $w = \pi i$ is the image of $z = x_1$, a negative number, so
>
> $$
> \pi i = A\operatorname{Log}x_1 = A\ln|x_1| + A\pi i .
> $$
>
> Identifying real and imaginary parts, $|x_1| = 1$ and $A = 1$. So $w = \operatorname{Log}z$, and $x_1 = -1$.
>
> **Verification.** By [[§102★ Examples (Mappings of the Upper Half Plane)#^ex-102-3|Example §102.3]] (B&C's Example 3 of Sec. 102), $w = \operatorname{Log}z$ maps the half plane $y > 0$ one to one onto the strip $0 < v < \pi$.
>
> *B&C: Sec. 130, Example 2*

^ex-130-2

> [!example] Example §130.3: A Wedge
> Use the [[§128★ Schwarz–Christoffel Transformation#^thm-128-4|Schwarz–Christoffel transformation]] to arrive at $w = z^m$ ($0 < m < 1$), which maps the half plane $y \ge 0$ onto the wedge $|w| \ge 0$, $0 \le \arg w \le m\pi$, and transforms $z = 1$ into $w = 1$.
>
> **Angles.** B&C views the wedge as a limit of triangles with one vertex at $w = 0$ and a side along the positive $u$ axis (its Fig. 186). In the limit the only finite vertex is $w_1 = 0$, with interior angle $m\pi$, so $k_1 = 1 - m$; the other vertex has gone to infinity, and the point $w = 1$ is an ordinary point of a side.
>
> **Derivative.** Choose $x_1 = 0$ as the prevertex of $w_1 = 0$ and let $z = \infty$ go to the vertex at infinity. Then
>
> $$
> \frac{dw}{dz} = Az^{-(1 - m)} = Az^{m - 1}, \qquad w = \frac Am z^m + B .
> $$
>
> **Constants.** $w = 0$ at $z = 0$ gives $B = 0$, and $w = 1$ at $z = 1$ gives $A = m$. So $w = z^m$.
>
> **Verification.** With $z = re^{i\theta}$, $0 \le \theta \le \pi$, the image is $w = r^me^{im\theta}$: the ray $\theta = 0$ goes onto the ray $\arg w = 0$, the ray $\theta = \pi$ onto $\arg w = m\pi$, and the half plane one to one onto the wedge, since $r \mapsto r^m$ and $\theta \mapsto m\theta$ are one to one. The exterior angle at $w = 0$ is $(1 - m)\pi$, as the derivative requires: $\arg f'(x) = (m - 1)\pi$ for $x < 0$ and $0$ for $x > 0$, a jump of $(1 - m)\pi$.
>
> *B&C: Sec. 130, Exercise 5*

^ex-130-3

> [!example] Example §130.4: A Half Plane with a Horizontal Slit
> As $z$ moves to the right along the negative real axis, its image $w$ is to move to the right along the entire $u$ axis. As $z$ describes the segment $0 \le x \le 1$, $w$ is to move to the left along the half line $v = \pi$, $u \ge 1$; and as $z$ moves to the right along $x \ge 1$, $w$ is to move to the right along the same half line (B&C's Fig. 26 in Appendix 2). Obtain formally the mapping function, and verify it on the boundary.
>
> **Angles and derivative.** At $z = 0$ the image jumps from $u = +\infty$ on the $u$ axis to $u = +\infty$ on the line $v = \pi$, a vertex at infinity between parallel lines: exterior angle $\pi$, $k = 1$. At $z = 1$ the direction reverses at the tip $1 + \pi i$ of the slit: exterior angle $-\pi$, $k = -1$. This suggests
>
> $$
> f'(z) = A(z - 0)^{-1}(z - 1)^{1} = A\Big(1 - \frac1z\Big), \qquad f(z) = A(z - \operatorname{Log}z) + B .
> $$
>
> **Constants.** For $x > 0$, $f(x) = A(x - \ln x) + B$ must lie on $v = \pi$ with smallest $u$ equal to $1$ at $x = 1$. Since $x - \ln x$ is real, decreasing on $(0, 1)$, increasing on $(1, \infty)$, with minimum $1$ at $x = 1$, take $A = 1$, $B = \pi i$:
>
> $$
> w = \pi i + z - \operatorname{Log}z .
> $$
>
> **Verification on the boundary.** For $x > 0$: $w = (x - \ln x) + \pi i$, which runs left from $+\infty + \pi i$ to $1 + \pi i$ as $x$ goes from $0$ to $1$, then right again to $+\infty + \pi i$. For $x < 0$: $\operatorname{Log}x = \ln|x| + \pi i$, so $w = x - \ln|x|$, real, with derivative $1 - 1/x > 0$; it increases from $-\infty$ to $+\infty$ as $x$ goes from $-\infty$ to $0$. These are the motions prescribed above.
>
> *B&C's exercise says the map is one of "the half plane $\operatorname{Re} z > 0$"; the boundary motion it describes, and its Fig. 26, concern the upper half plane $\operatorname{Im} z > 0$.*
>
> *B&C: Sec. 130, Exercise 6*

^ex-130-4

> [!example] Example §130.5: A Half Plane with a Vertical Slit
> As $z$ moves to the right along $x \le -1$, its image is to move to the right along the negative real axis; as $z$ moves along $-1 \le x \le 0$ and then $0 \le x \le 1$, $w$ is to move up the segment $0 \le v \le 1$ of the $v$ axis and then back down; for $x \ge 1$, $w$ moves to the right along the positive real axis. Obtain formally $w = \sqrt{z^2 - 1}$, $0 < \arg\sqrt{z^2 - 1} < \pi$, and verify that it maps the upper half plane onto the half plane $\operatorname{Im} w > 0$ with a cut along $0 < v \le 1$.
>
> **Angles and derivative.** At $z = \pm1$ (image $w = 0$) the direction turns by $+\pi/2$ ($k = \frac12$); at $z = 0$ (the tip $w = i$) it reverses, exterior angle $-\pi$ ($k = -1$). So
>
> $$
> f'(z) = A(z + 1)^{-1/2}(z - 0)^{1}(z - 1)^{-1/2} = \frac{Az}{(z^2 - 1)^{1/2}}, \qquad f(z) = A(z^2 - 1)^{1/2} + B .
> $$
>
> **Constants.** $f(\pm1) = 0$ gives $B = 0$, and $f(0) = A(-1)^{1/2} = Ai$ must be $i$, so $A = 1$: $w = (z^2 - 1)^{1/2}$ with $0 < \arg w < \pi$.
>
> **Verification by successive mappings.** $Z = z^2$ maps the half plane $\operatorname{Im} z > 0$ one to one onto the $Z$ plane cut along the nonnegative real axis ($\arg Z = 2\arg z \in (0, 2\pi)$). Then $W = Z - 1$ gives the $W$ plane cut along the ray $W \ge -1$ of the real axis, with $0 < \arg W < 2\pi$. Finally $w = \sqrt W$ with $0 < \arg w < \pi$ halves the arguments and takes square roots of the moduli, one to one. Its image is the set of $w$ with $\operatorname{Im} w > 0$ whose squares avoid the cut; the only such squares on the cut are $w^2 \in [-1, 0)$, that is, $w = it$ with $0 < t \le 1$. So the image is the upper half plane with a cut along $0 < v \le 1$. The two edges of the cut $-1 \le W < 0$ come from $-1 < x < 0$ and $0 < x < 1$ (approached from $y > 0$, $z^2$ lies just below, respectively just above, the real axis), and they go to the left and right sides of the slit.
>
> *B&C's exercise asks for a map of "the right half plane $\operatorname{Re} z > 0$"; the boundary motion it describes, and the successive mappings, concern the upper half plane $\operatorname{Im} z > 0$.*
>
> *B&C: Sec. 130, Exercise 7*

^ex-130-5
