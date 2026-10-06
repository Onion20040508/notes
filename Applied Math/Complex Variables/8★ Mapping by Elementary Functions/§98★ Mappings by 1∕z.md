---
type: section
subject: "[[Complex Variables]]"
chapter: 8
section: "98★"
bc: "98"
aliases: ["B&C 98"]
tags: [complex-variables, math342, extension]
---
← [[§97★ The Transformation w = 1∕z]] · ↑ [[· 8★ Mapping by Elementary Functions]] · [[§99★ Linear Fractional Transformations]] →

*Brown–Churchill, Section 98.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

This section proves the key geometric fact about $w = 1/z$: **it carries circles and lines to circles and lines**. The proof is pure algebra, because one equation $A(x^2 + y^2) + Bx + Cy + D = 0$ describes every circle and every line, and the substitution $z = 1/w$ turns it into an equation of the same type with the coefficients $A$ and $D$ exchanged. Which of the four cases occurs depends only on whether the original circle or line passes through the origin. With the linear maps of [[§96★ Linear Transformations|§96]], this gives the circle-preserving property of all linear fractional transformations ([[§99★ Linear Fractional Transformations|§99]]).

## Circles and Lines Go to Circles and Lines

> [!theorem] Proposition §98.1: 1/z in Coordinates
> If $w = u + iv$ is the image of a nonzero point $z = x + iy$ under $w = 1/z$, then
>
> $$
> u = \frac{x}{x^2 + y^2}, \qquad v = \frac{-y}{x^2 + y^2} , \qquad (1)
> $$
>
> and conversely
>
> $$
> x = \frac{u}{u^2 + v^2}, \qquad y = \frac{-v}{u^2 + v^2} . \qquad (2)
> $$
>
> *B&C: Sec. 98, Equations (1) and (2)*

^prop-98-1

> [!proof]+ Proof
> $w = \dfrac1z = \dfrac{\bar z}{z\bar z} = \dfrac{\bar z}{|z|^2} = \dfrac{x - iy}{x^2 + y^2}$; taking real and imaginary parts gives (1). Since also $z = 1/w$, the same computation with the roles of $z$ and $w$ exchanged gives (2).

^pf-98-1

*Uses:* [[§6 Complex Conjugates#^prop-6-3|§6.3]] ($z\bar z = |z|^2$)

> [!theorem] Proposition §98.2: One Equation for All Circles and Lines
> Let $A$, $B$, $C$, $D$ be real numbers with
>
> $$
> B^2 + C^2 > 4AD . \qquad (3)
> $$
>
> Then the equation
>
> $$
> A(x^2 + y^2) + Bx + Cy + D = 0 \qquad (4)
> $$
>
> represents a circle when $A \ne 0$ and a line when $A = 0$; and every circle and every line has an equation of this form. The circle or line passes through the origin exactly when $D = 0$.
>
> *B&C: Sec. 98 (text)*

^prop-98-2

> [!proof]+ Proof
> **$A \ne 0$.** Divide by $A$ and complete the squares:
>
> $$
> \Big(x + \frac{B}{2A}\Big)^2 + \Big(y + \frac{C}{2A}\Big)^2 = \Big(\frac{\sqrt{B^2 + C^2 - 4AD}}{2A}\Big)^2 .
> $$
>
> The right side is positive exactly because of (3), so this is the circle with center $(-B/2A, -C/2A)$ and radius $\sqrt{B^2 + C^2 - 4AD}/(2|A|)$. (Without (3) the set would be a single point or empty; this is why (3) is needed.)
>
> **$A = 0$.** Then (3) says $B^2 + C^2 > 0$, so $B$ and $C$ are not both zero and $Bx + Cy + D = 0$ is a line.
>
> **Conversely**, the circle with center $(x_0, y_0)$ and radius $R > 0$ is $x^2 + y^2 - 2x_0x - 2y_0y + (x_0^2 + y_0^2 - R^2) = 0$, which is (4) with $A = 1$, $B = -2x_0$, $C = -2y_0$, $D = x_0^2 + y_0^2 - R^2$, and $B^2 + C^2 - 4AD = 4R^2 > 0$. A line $Bx + Cy + D = 0$ with $(B, C) \ne (0, 0)$ is (4) with $A = 0$.
>
> Finally, $(0, 0)$ satisfies (4) if and only if $D = 0$.

^pf-98-2

*Uses:* [[§4 Vectors and Moduli#^prop-4-2|§4.2]], [[§4 Vectors and Moduli#^def-4-2|Def. §4.2]] (the circle $|z - z_0| = R$)

> [!theorem] Theorem §98.3: w = 1/z Maps Circles and Lines onto Circles and Lines
> If $x$ and $y$ satisfy (4), then $u$ and $v$ satisfy
>
> $$
> D(u^2 + v^2) + Bu - Cv + A = 0 , \qquad (5)
> $$
>
> which again represents a circle or a line; and conversely. Hence, under $w = 1/z$:
> - **(a)** a circle ($A \ne 0$) not passing through the origin ($D \ne 0$) is transformed into a circle not passing through the origin;
> - **(b)** a circle ($A \ne 0$) through the origin ($D = 0$) is transformed into a line that does not pass through the origin;
> - **(c)** a line ($A = 0$) not passing through the origin ($D \ne 0$) is transformed into a circle through the origin;
> - **(d)** a line ($A = 0$) through the origin ($D = 0$) is transformed into a line through the origin.
>
> *B&C: Sec. 98 (text)*

^thm-98-3

> [!proof]+ Proof
> Let $z \ne 0$ satisfy (4), and let $w = 1/z$. By (2), $x^2 + y^2 = \dfrac{u^2 + v^2}{(u^2 + v^2)^2} = \dfrac{1}{u^2 + v^2}$, so (4) becomes
>
> $$
> \frac{A}{u^2 + v^2} + \frac{Bu}{u^2 + v^2} - \frac{Cv}{u^2 + v^2} + D = 0 .
> $$
>
> Multiplying by $u^2 + v^2 \ne 0$ gives (5). Conversely, if $w \ne 0$ satisfies (5), the same substitution with (1) in place of (2) turns (5) back into (4) for $z = 1/w$. The coefficients of (5), in the roles of $A, B, C, D$, are $D, B, -C, A$, and
>
> $$
> B^2 + (-C)^2 = B^2 + C^2 > 4AD = 4DA ,
> $$
>
> so (5) satisfies (3) and represents a circle or a line by Proposition §98.2: a circle if $D \ne 0$ and a line if $D = 0$. It passes through $w = 0$ exactly when its constant term $A$ is $0$, that is, when the original curve is a line. This gives (a)–(d).
>
> (The points $z = 0$ and $z = \infty$ are excluded above. In the extended plane, with $T$ of [[§97★ The Transformation w = 1∕z#^def-97-2|Definition §97.2]], a curve through the origin has $0 \mapsto \infty$, which completes its image line, and a line, together with $\infty$, has $\infty \mapsto 0$, which completes its image circle through the origin.)

^pf-98-3

*Uses:* [[§98★ Mappings by 1∕z#^prop-98-1|§98.1]], [[§98★ Mappings by 1∕z#^prop-98-2|§98.2]], [[§97★ The Transformation w = 1∕z#^def-97-2|Def. §97.2]]

> [!remark] Remark: Method — Images of Regions under 1/z
> 1. **Boundary.** Write each boundary circle or line in the form (4) and read off its image from (5); or use the cases (a)–(d) and the images of two or three points.
> 2. **Side.** Decide which side of the image curve is the image of the region: either substitute (2) into the inequality that describes the region (it turns into an inequality in $u$, $v$), or map one interior point.
> 3. **Special points.** $z = 0$ goes to $\infty$ and $z = \infty$ to $0$: an unbounded region has $w = 0$ on its image's boundary, and a region whose boundary passes through $0$ has an unbounded image.

^rem-98-1

## Examples

> [!example] Example §98.1: Vertical and Horizontal Lines
> **(a)** A vertical line $x = c_1$ ($c_1 \ne 0$) is (4) with $A = 0$, $B = 1$, $C = 0$, $D = -c_1$. By (5) its image is $-c_1(u^2 + v^2) + u = 0$, or
>
> $$
> \Big(u - \frac{1}{2c_1}\Big)^2 + v^2 = \Big(\frac{1}{2c_1}\Big)^2 , \qquad (6)
> $$
>
> a circle centered on the $u$ axis and tangent to the $v$ axis. By (1) the image of the point $(c_1, y)$ is
>
> $$
> (u, v) = \Big(\frac{c_1}{c_1^2 + y^2},\ \frac{-y}{c_1^2 + y^2}\Big) .
> $$
>
> If $c_1 > 0$, the circle lies to the right of the $v$ axis. As $y$ increases through negative values to $0$, $v > 0$ and $u$ increases from $0$ to $1/c_1$; as $y$ increases through positive values, $v < 0$ and $u$ decreases to $0$. So as $(c_1, y)$ moves up the entire line, the image traverses the circle once **clockwise**, the point at infinity corresponding to $w = 0$. If $c_1 < 0$, the circle lies to the left of the $v$ axis and is traversed once **counterclockwise**.
>
> **(b)** A horizontal line $y = c_2$ ($c_2 \ne 0$) is (4) with $A = B = 0$, $C = 1$, $D = -c_2$, and (5) gives $-c_2(u^2 + v^2) - v = 0$, or
>
> $$
> u^2 + \Big(v + \frac{1}{2c_2}\Big)^2 = \Big(\frac{1}{2c_2}\Big)^2 , \qquad (7)
> $$
>
> a circle centered on the $v$ axis and tangent to the $u$ axis, below it when $c_2 > 0$ and above it when $c_2 < 0$.
>
> *B&C: Sec. 98, Examples 1 and 2*

^ex-98-1

![[m342-98-1.svg]]
*Lines $x = c_1$ (blue) and $y = c_2$ (red) and their images under $w = 1/z$, the circles (6) and (7), all through $w = 0$, the image of $\infty$. Arrows show corresponding directions: upward along $x = \frac13$ is clockwise around the right-hand circle of radius $\frac32$; upward along $x = -\frac12$ is counterclockwise around the circle of radius $1$ on the left.*

> [!example] Example §98.2: A Half Plane Goes onto a Disk
> Show that $w = 1/z$ maps the half plane $x \ge c_1$ ($c_1 > 0$) onto the disk
>
> $$
> \Big(u - \frac{1}{2c_1}\Big)^2 + v^2 \le \Big(\frac{1}{2c_1}\Big)^2 \qquad (8)
> $$
>
> (with $w = 0$, the image of $\infty$, on its boundary).
>
> **Sweeping by lines (B&C).** By Example §98.1, each line $x = c$ with $c \ge c_1$ goes onto the circle
>
> $$
> \Big(u - \frac{1}{2c}\Big)^2 + v^2 = \Big(\frac{1}{2c}\Big)^2 . \qquad (9)
> $$
>
> As $c$ increases from $c_1$, the lines move to the right and the circles (9), all tangent to the $v$ axis at the origin, shrink. The lines fill the half plane, and the circles fill the disk (8) minus the origin, each point exactly once.
>
> **By an inequality.** By the first of equations (2), for $w \ne 0$,
>
> $$
> x \ge c_1 \iff \frac{u}{u^2 + v^2} \ge c_1 \iff u^2 + v^2 - \frac{u}{c_1} \le 0 \iff \Big(u - \frac{1}{2c_1}\Big)^2 + v^2 \le \Big(\frac{1}{2c_1}\Big)^2 ,
> $$
>
> using $u^2 + v^2 > 0$ and $c_1 > 0$. So $z$ lies in the half plane exactly when $w = 1/z$ lies in the disk (8), $w \ne 0$.
>
> *B&C: Sec. 98, Example 3 and Exercise 1*

^ex-98-2

> [!example] Example §98.3: A Strip
> Find the image of the infinite strip $0 < y < 1/(2c)$, $c > 0$, under $w = 1/z$.
>
> By the second of equations (2), $y = -v/(u^2 + v^2)$. First, $y > 0 \iff v < 0$. Second, for $w \ne 0$,
>
> $$
> y < \frac{1}{2c} \iff \frac{-v}{u^2 + v^2} < \frac{1}{2c} \iff -2cv < u^2 + v^2 \iff u^2 + (v + c)^2 > c^2 .
> $$
>
> The image is the part of the lower half plane outside the circle $u^2 + (v + c)^2 = c^2$:
>
> $$
> u^2 + (v + c)^2 > c^2, \qquad v < 0 .
> $$
>
> This matches Example §98.1(b): the edge $y = 1/(2c)$ goes onto the circle (7) with $c_2 = 1/(2c)$, of radius $c$ centered at $-ic$, and the edge $y = 0$ onto the $u$ axis (case (d)).
>
> *B&C: Sec. 98, Exercise 4*

^ex-98-3

> [!example] Example §98.4: z + 1/z Maps Circles onto Ellipses
> With $z = r_0e^{i\theta}$, the transformation $w = z + \dfrac1z$ gives $w = r_0e^{i\theta} + \dfrac{1}{r_0}e^{-i\theta}$, that is,
>
> $$
> u = \Big(r_0 + \frac1{r_0}\Big)\cos\theta, \qquad v = \Big(r_0 - \frac1{r_0}\Big)\sin\theta \qquad (0 \le \theta \le 2\pi) .
> $$
>
> For $r_0 \ne 1$ this is an ellipse with semi-axes $a = r_0 + 1/r_0$ and $b = |r_0 - 1/r_0|$, and its foci are at $\pm\sqrt{a^2 - b^2} = \pm\sqrt{4} = \pm 2$: all these ellipses are **confocal**. For $r_0 = 1$, $u = 2\cos\theta$, $v = 0$: the circle $|z| = 1$ goes onto the segment $-2 \le u \le 2$, covered twice.
>
> The domain $|z| > 1$ goes one to one onto the rest of the $w$ plane. As $r_0$ increases over $(1, \infty)$, $a = r_0 + 1/r_0$ increases over $(2, \infty)$, so distinct circles give distinct (nested) ellipses, each traversed once. And every $w$ off the segment lies on exactly one of them: an ellipse with foci $\pm2$ and major semi-axis $a$ is $|w - 2| + |w + 2| = 2a$, and $|w - 2| + |w + 2| > 4$ off the segment, so $a$ is determined, and then $r_0 > 1$ is the unique solution of $r_0 + 1/r_0 = a$.
>
> *B&C: Sec. 98, Exercise 13*

^ex-98-4

> [!example] Example §98.5: The Circle Equation in Complex Form
> **(a)** Since $x = \frac12(z + \bar z)$ and $y = \frac1{2i}(z - \bar z)$ ([[§6 Complex Conjugates#^prop-6-2|Proposition §6.2]]), multiplying (4) by $2$ and using $1/i = -i$ gives
>
> $$
> 2Az\bar z + (B - Ci)z + (B + Ci)\bar z + 2D = 0 .
> $$
>
> **(b)** Put $z = 1/w$ and multiply by $w\bar w$:
>
> $$
> 2A + (B - Ci)\bar w + (B + Ci)w + 2Dw\bar w = 0 .
> $$
>
> With $w = u + iv$, $(B + Ci)w + (B - Ci)\bar w = 2\operatorname{Re}\big[(B + Ci)(u + iv)\big] = 2(Bu - Cv)$, so this is $2D(u^2 + v^2) + 2Bu - 2Cv + 2A = 0$, which is (5). This is a second proof of Theorem §98.3, with no division into real and imaginary parts until the end.
>
> *B&C: Sec. 98, Exercise 14*

^ex-98-5

*Chain: the function $1/z$ earlier in [[§59a The Function 1∕z|Chapter 4]] · later in [[§113★ Further Examples (Preservation of Angles and Scale Factors)#^ex-113-4|Chapter 9]]*
